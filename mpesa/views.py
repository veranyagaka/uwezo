from django.shortcuts import render

# Create your views here.
import requests
from requests.auth import HTTPBasicAuth
from django.conf import settings
import base64
from datetime import datetime
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
print(settings.ALLAN)
def get_mpesa_token():
    consumer_key = settings.MPESA_CONSUMER_KEY
    consumer_secret = settings.MPESA_CONSUMER_SECRET
    API_URL = f"{settings.MPESA_BASE_URL}/oauth/v1/generate?grant_type=client_credentials"
    print(settings.MPESA_CONSUMER_KEY)
    print(settings.MPESA_CONSUMER_SECRET)

    print(API_URL)
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
    access_token = get_mpesa_token()
    API_URL = f"{settings.MPESA_BASE_URL}/mpesa/stkpush/v1/processrequest"
    headers = {
        "Authorization": f"Bearer {access_token}"
    }
    timestamp = datetime.now().strftime('%Y%m%d%H%M%S')
    password = base64.b64encode(f"{settings.MPESA_SHORTCODE}{settings.MPESA_PASSKEY}{timestamp}".encode()).decode('utf-8')
    payload = {
        "BusinessShortCode": settings.MPESA_SHORTCODE,
        "Password": password,
        "Timestamp": timestamp,
        "TransactionType": "CustomerPayBillOnline",
        "Amount": amount,
        "PartyA": phone_number,
        "PartyB": settings.MPESA_SHORTCODE,
        "PhoneNumber": 254708374149,
        "CallBackURL": settings.MPESA_CALLBACK_URL,
        "AccountReference": "123456",
        "TransactionDesc": "Pay school fees"
    }
    response = requests.post(API_URL, json=payload, headers=headers)
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
response = lipa_na_mpesa('254759626842', 1)
print(response)