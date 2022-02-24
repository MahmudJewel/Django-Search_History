from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib.auth.models import User
from django.db.models import Count
from .models import history

# Create your views here.

class history_view(TemplateView):
    template_name = "home.html"
    # def get(self, request):
    #     history_obj = history.objects.all()
    #     return history_obj
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        users= User.objects.all()
        keywords = history.objects.values("keyword").distinct().annotate(key_count=Count("keyword")).order_by('-key_count')
        all_Data = history.objects.all().order_by('-time')
        context['users'] = list(users)
        context['all_Data'] = list(all_Data)
        context['keywords'] = list(keywords)
        return context
