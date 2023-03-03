from django.shortcuts import render

def index(request):
    data =  {
        'title': 'Главная страница сайта',
        'values': ['some', 'hello', 123]
    }
    return render(request, "main/index.html", data)

def acts(request):
    data = {
        'title': 'Акты!!!',
        'values': ['some', 'hello', 123]

    }
    return render(request, "main/acts_home.html", data)