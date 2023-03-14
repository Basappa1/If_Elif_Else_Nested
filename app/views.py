from django.shortcuts import render

# Create your views here.

def else1(request):
    x={'a':290}
    return render(request,'condtion_statements.html',x)
