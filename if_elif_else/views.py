from django.shortcuts import render

# Create your views here.

def if_elif_else(request):
    x={'a':100,'b':200,'c':300}
    return render(request,'if_elif_else.html',x)
