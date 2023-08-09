from django.http import HttpResponse


def index(request):
    abc = "Debug values testing" + 'Hello World!'
    print(abc)
    return HttpResponse(abc)