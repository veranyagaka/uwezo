from django.shortcuts import render
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.backends import default_backend
from cryptography import x509
# Create your views here./home/vera/community/certs
import requests
from requests.auth import HTTPBasicAuth
from django.conf import settings
import base64
from datetime import datetime
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
print(settings.ALLAN)
def encrypt_security_credential(security_credential):
    # Load the certificate
    with open('/home/vera/community/certs/SandboxCertificate.cer', 'rb') as f:
        cert_data = f.read()
    certificate = x509.load_pem_x509_certificate(cert_data, default_backend())

    # Encrypt the security credential
    public_key = certificate.public_key()
    encrypted_credential = public_key.encrypt(
        security_credential.encode(),
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )

    # Base64 encode the encrypted credential
    encoded_credential = base64.b64encode(encrypted_credential).decode('utf-8')
    return encoded_credential

def get_mpesa_token():
    consumer_key = settings.MPESA_CONSUMER_KEY
    consumer_secret = settings.MPESA_CONSUMER_SECRET
    API_URL = f"{settings.MPESA_BASE_URL}/oauth/v1/generate?grant_type=client_credentials"

    response = requests.get(API_URL, auth=HTTPBasicAuth(consumer_key, consumer_secret))
    if response.status_code == 200:
        json_response = response.json()
    else:
        return f"Error: Received status code {response.status_code}"
    print(response.text)
    print(f"Response Status Code: {response.status_code}") 
    json_response = response.json()
    return json_response['access_token']

def lipa_na_mpesa(phone_number, amount):
    encrypted_credential = encrypt_security_credential(settings.MPESA_SECURITY_CREDENTIAL)

    access_token = get_mpesa_token()
    API_URL = f"{settings.MPESA_BASE_URL}/mpesa/stkpush/v1/processrequest"
    headers = {
        "Authorization": f"Bearer {access_token}",
        "Content-Type": "application/json"
    }
    timestamp = datetime.now().strftime('%Y%m%d%H%M%S')
    password = base64.b64encode(f"{settings.MPESA_SHORTCODE}{settings.MPESA_PASSKEY}{timestamp}".encode()).decode('utf-8')
    print(settings.MPESA_SHORTCODE)
    print(settings.MPESA_PASSKEY)
    print(password)
    print(timestamp)
    print(settings.MPESA_CALLBACK_URL)

    payload = {
        "BusinessShortCode": settings.MPESA_SHORTCODE,
        "Password": password,
        "Timestamp": timestamp,
        "TransactionType": "CustomerPayBillOnline",
        "Amount": amount,
        "PartyA": phone_number,
        "PartyB": settings.MPESA_SHORTCODE,
        "PhoneNumber": phone_number,
        "CallBackURL": settings.MPESA_CALLBACK_URL,
        "AccountReference": "123456",
        "TransactionDesc": "Pay school fees"
        #"SecurityCredential": encrypted_credential 
    }
    print("API URL:", API_URL)
    print("Headers:", headers)
    print("Payload:", payload)
    response = requests.post(API_URL, json=payload, headers=headers)
    print(f"Token response: {response.text}") 
    return response.json()

@csrf_exempt
def mpesa_callback(request):
    print('callback')
    if request.method =='POST':
        data = json.loads(request.body.decode('utf-8'))
        print(data)
        return JsonResponse({"ResultDesc": "Success", "ResultCode": "0"})
    return JsonResponse({"ResultDesc": "Failed", "ResultCode": "1"}, status=400)

print('Hi vera')
def mpesa(request):
    return render(request, 'mpesa.html')
response = lipa_na_mpesa('254759626842', 1)
print(response)