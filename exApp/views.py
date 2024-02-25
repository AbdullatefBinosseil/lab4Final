from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
tax_rate=15
def index(request):
    return render(request, "exApp/index.html")
def anyNumber(request,number):
    
    numAfterTax=(number * (tax_rate/100))+number
    
    return render(request, "exApp/anyNumber.html",{
        "numAfterTax":numAfterTax, "number":number
    })
def taxrate(request):
    return render(request, "exApp/taxrate.html",{
        "tax_rate":tax_rate
    })