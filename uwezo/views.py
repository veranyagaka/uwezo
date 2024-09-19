from django.shortcuts import render,redirect
from django.http import HttpResponse

# Create your views here.
def index(request):
    #return HttpResponse("Welcome to the Community Accountability Platform")
    return render(request, 'index.html')  
# geotagging/views.py
from .forms import ReportForm

def map(request):
    if request.method == 'POST':
        form = ReportForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('report_list')  # Redirect to a list of reports
    else:
        form = ReportForm()
    return render(request, 'result.html', {'form': form})
def map_view(request):
    return render(request, 'maps.html')
