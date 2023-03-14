from django.shortcuts import render

# Create your views here.

def if_else(request):
    x={'a':20,'b':10}
    return render(request,'if_else_condtion.html',x)
