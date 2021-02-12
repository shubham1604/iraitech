from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth.decorators import login_required
from .forms import MyForm
from .fuctions import calculate_without_recursion
# Create your views here.


def home(request):
    return render (request, "index.html", {})

@login_required
def api_view(request):
    result = None
    if request.method == 'POST':
        form = MyForm(request.POST)
        if form.is_valid():
            print("19")
            n = form.cleaned_data.get('n')
            x = form.cleaned_data.get('x')
            result = calculate_without_recursion(n,x)
    else:
        form = MyForm()
    return render(request,"api.html" ,{'form':form, 'result':result})
