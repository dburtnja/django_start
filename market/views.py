from django.http import HttpResponse
import requests


# Create your views here.


def market(request):
    proxies = {"http": "http://61.233.25.166:80"}
    result = requests.get("https://booking.uz.gov.ua/", proxies=proxies)
    return HttpResponse(result.content)
