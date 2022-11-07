from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView


from datetime import datetime


class AuthorizedViews(LoginRequiredMixin, TemplateView):
    template_name = 'home/authorized.html'
    login_url = '/admin'


# Create your views here.
def home(request):
    return render(request, 'home/welcome.html', {'today': datetime.today()})
