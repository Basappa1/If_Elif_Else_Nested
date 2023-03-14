from django.shortcuts import render

# Create your views here.


def nested_if(request):
    x={'a':100,'b':200,'c':50}
    return render(request,'nested_if.html',x)