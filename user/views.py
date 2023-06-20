from django.shortcuts import render
from django.views.generic.edit import FormView  # form을 활용할수 있게 해주는 클래스에요

def index(request):
    return render(request, 'index.html')

class RegisterView(FormView):
    template_name = 'register.html'
    # template_name이라고 하면 html파일이조? 이게 부모인 FormView에서 가져온거에요.

