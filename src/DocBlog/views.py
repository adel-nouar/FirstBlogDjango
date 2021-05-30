from datetime import datetime
from django.shortcuts import render


def index(request):
    # return HttpResponse("<h1> Hello, welcome to my website </h1>")
    date = datetime.today()
    return render(request, "index.html", context={'prenom': 'ana', 'date': date})
