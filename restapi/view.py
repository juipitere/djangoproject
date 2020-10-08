def home(request):
    return HttpResponse("Hello, Django!")

def taskstring(request):
    result='Rest Api string!'
    return HttpResponse(result, content_type="text/plain")

