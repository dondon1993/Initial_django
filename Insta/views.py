from django.views.generic import TemplateView

# HellowWorld is a TemplateView

class HelloWorld(TemplateView):
    template_name = 'test.html'
