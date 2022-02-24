from django.shortcuts import render
# from django.views.generic import TemplateView
from django.views.generic import ListView
from django.contrib.auth.models import User
from django.db.models import Count
from .models import history
from datetime import datetime, timedelta



class history_view(ListView):
    template_name = "home.html"
    model=history
    context_object_name = 'all_Data'
    paginate_by = 200
    
    def get_queryset(self):
        all_Data = history.objects.all().order_by('-time')
        keyword_checkbox = self.request.GET.getlist('keyword_checkbox', '')
        user_checkbox = self.request.GET.getlist('user_checkbox', '')
        time_checkbox = self.request.GET.getlist('time_checkbox', '')
        start_date = self.request.GET.get('start_date', '')
        end_date = self.request.GET.get('end_date', '')
        # print('Start Date: ', type(start_date))
        # keyword filter 
        if len(keyword_checkbox)>0:
            all_Data = history.objects.filter(keyword__in=keyword_checkbox)
            # print('all data: ', all_Data.count())
        
        # users filter 
        if len(user_checkbox)>0:
            all_Data = history.objects.filter(user__username__in=user_checkbox)
        
        # fixed time filter 
        if len(time_checkbox)>0:
            now = datetime.now().date()
            str_date= datetime.now().date()
            if time_checkbox[0]=="30":
                date = datetime.now() - timedelta(30)
                str_date= date.date()
            if time_checkbox[0]=="7":
                date = datetime.now() - timedelta(7)
                str_date= date.date()
            if time_checkbox[0]=="1":
                date = datetime.now() - timedelta(1)
                str_date= date.date()
            all_Data=history.objects.filter(time__range=[str_date, now])
        # date range 
        if start_date != '' and end_date != '':
            all_Data=history.objects.filter(time__range=[start_date, end_date])
        return all_Data
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        users= User.objects.all()
        keywords = history.objects.values("keyword").distinct().annotate(key_count=Count("keyword")).order_by('-key_count')
        context['users'] = list(users)
        context['keywords'] = list(keywords)
        return context
    
