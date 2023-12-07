from django.shortcuts import render
from django.http import HttpResponse
from .forms import UserForm, NewsForm


def index(request):
    if request.method == 'POST':
        name = request.POST.get('name', 'Noname')
        age = request.POST.get('age',0)
        return HttpResponse(f'Пользователь: {name},возраст: {age}')
    else:
        form = UserForm()
        return render(request, 'app/index.html', context={'form': form})

def appointmentForm(request):
    return render(request, 'app/appointment.html')



# def postuser(request):
#     name = request.POST.get('name','Noname')
#     age = request.POST.get('age',0)
#     agree = request.POST.get('agree',False)
#     return HttpResponse(f'Пользователь: {name},возраст: {age},согласие: {agree}')


def news(request):
    if request.method == 'POST':
        return HttpResponse('Новая новость')
    else:
        form = NewsForm()
        return render(request,'app/news.html',context={'form':form})