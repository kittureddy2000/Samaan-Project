from django.http import HttpResponse
import os

def index(request):
    os_key = SECRET_KEY = os.environ.get("DJANGO_SECRET_KEY")
    print("Environment variable vlaue", os_key)

    return HttpResponse("Hello, world. You're at the polls index. This is transferred to new project" )