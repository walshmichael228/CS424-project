from django.http import HttpResponse

def index(request,name):
    return HttpResponse('Hello %s'%name)