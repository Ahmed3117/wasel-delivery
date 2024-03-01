# from .models import Category, Product, Client, Pill, SellOperation, Paid
import datetime
from django.shortcuts import render,redirect
from django.urls import reverse
from django.http import HttpResponse,JsonResponse
import json
from admin_interface.models import Theme
from companyinfo.models import CompanyInfo
from maindata.models import ChargeOperation, Client, Package, User


def getselectedclientaddress(request, pk):
    client = User.objects.get(id = pk)
    client_address = ''
    if client.address:
        client_address= client.address
    return JsonResponse(client_address, safe=False)


def invoice(request, pk):
    obj = ChargeOperation.objects.get(id = pk)
    package = Package.objects.filter(chargeoperation = obj)[0]
    outdate = datetime.datetime.now()
    #------------------------------------
    companyinfo = CompanyInfo.objects.last()
    #------------------------------------
    theme = Theme.objects.get(active = 1)
    logo_url = None
    if theme.logo:
        logo = theme.logo
        logo_url = logo.url
    #-----------------------------------
    context = {

            'chargeprocess_id' : pk,
            'chargeprocess' : obj,
            'outdate' : outdate,
            'package' : package,
            'logo_url' : logo_url,
            'companyinfo' : companyinfo,
        }
    return render(request,'maindata/invoice.html' ,context)
