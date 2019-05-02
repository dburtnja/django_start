from django.http import HttpResponse
import requests

# Create your views here.


def market(request):
    result = requests.get("https://www.eps.org.ua/ternopil/account/view/Ib5pfc9lw4mLbkI3cqKfrg")
    return HttpResponse(result.content)
