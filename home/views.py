from django.shortcuts import render
from django.views.generic import TemplateView


class HomeView(TemplateView):
    "Home page"
    
    template_name="home/home.html"


class Error404View(TemplateView):
    "Error 404"
    
    template_name="home/404.html"


class Error500View(TemplateView):
    "Error 500"
    
    template_name="home/500.html"

    @classmethod
    def as_error_view(cls):
        v=cls.as_view()
        def view(request):
            r=v(request)
            r.render()
            return r
        return view
