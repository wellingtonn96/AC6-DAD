from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect

# Create your views here.

def form1(request):
    if request.method == 'POST':
        return redirect('/form2')
    return render(request,'form1.html')

def form2(request):
    if request.method == 'POST':
        return redirect('/form3')
    return render(request, 'form2.html')

def form3(request):
    if request.method == 'POST':
        return redirect('/fim')
    return render(request, 'form3.html')

def fim(request):
    return render(request, 'fim.html')

