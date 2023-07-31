from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View,TemplateView,CreateView,UpdateView,DeleteView,DetailView,ListView,FormView
# Create your views here.
#function based view
def function(request):
    return HttpResponse('<h1>function based view</h1>')

def function_page(request):
    return render(request,'function.html')

class Class(View):
    def get(self,request):
        return HttpResponse('<h1>Class based view</h1>')

class Class_page(TemplateView):
    template_name='Class_page.html'