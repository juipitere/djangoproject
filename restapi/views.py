from django.shortcuts import render

# Create your views here.

def home(request):
  return HttpResponse("Hello, Django!")

def taskstring(request):
  result = 'Rest API stinrg!'
  return HttpResponse(result, content_type="text/plain")
