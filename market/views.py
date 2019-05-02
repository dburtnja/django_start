from django.http import HttpResponse
import requests

# Create your views here.


def market(request):
    result = requests.get("https://booking.uz.gov.ua/")
    return HttpResponse(result.content)
