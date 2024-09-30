from django.shortcuts import render
from django.views.generic import TemplateView
# Create your views here.



class index1(TemplateView):
    template_name = 'second task/class_template.html'

def index2(request):
    return render(request, 'second task/func_template.html')