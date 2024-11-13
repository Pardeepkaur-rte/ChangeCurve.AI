# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.urls import path, re_path
from apps.home import views

urlpatterns = [

    # The home page
    # path('', views.index, name='home'),
    path('', views.generate_plan, name='home'),
    path('generate-plan/', views.generate_plan, name='generate_plan'),
    path('analyze-plan/', views.analyze_plan, name='analyze_plan'),
    path('reference-excel/', views.reference_excel, name='reference_excel'),

    # Matches any html file
    re_path(r'^.*\.*', views.pages, name='pages'),

]
