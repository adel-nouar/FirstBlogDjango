from django.shortcuts import render


def index(request):
    # return HttpResponse("<h1> Hello, welcome to my website </h1>")
    return render(request, "index.html")
