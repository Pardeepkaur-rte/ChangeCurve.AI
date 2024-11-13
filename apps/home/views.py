# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django import template
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse

from .models import *
from .forms import *

from django.contrib import messages
from django.shortcuts import redirect


# @login_required(login_url="/login/")
def index(request):
    context = {'segment': 'index'}

    html_template = loader.get_template('home/index.html')
    return HttpResponse(html_template.render(context, request))


# @login_required(login_url="/login/")
def pages(request):
    context = {}
    # All resource paths end in .html.
    # Pick out the html file name from the url. And load that template.
    try:

        load_template = request.path.split('/')[-1]

        if load_template == 'admin':
            return HttpResponseRedirect(reverse('admin:index'))
        context['segment'] = load_template

        html_template = loader.get_template('home/' + load_template)
        return HttpResponse(html_template.render(context, request))

    except template.TemplateDoesNotExist:

        html_template = loader.get_template('home/page-404.html')
        return HttpResponse(html_template.render(context, request))

    except:
        html_template = loader.get_template('home/page-500.html')
        return HttpResponse(html_template.render(context, request))
    


# @login_required(login_url="/login/")
def generate_plan(request):  
    try:
        # Fetch a single instance instead of a queryset
        prompt_obj = Prompt.objects.get(_id='1')

        form = UpdatePromptForm(request.POST or None,instance=prompt_obj) 
        if request.POST:
            print("post")
           
            if form.is_valid():
                # Save the form data if valid
                form.save()
                messages.success(request, "Prompt updated successfully!")
                return redirect('generate_plan')  # Redirect to avoid resubmission

            else:
                # Display error message if form is invalid
                messages.error(request, "There was an error updating the prompt. Please try again.")
        # else:
        #     # Pass the instance to the form
        # form = UpdatePromptForm(instance=prompt_obj)

        print("form:::",form)
        
        context = {'segment': 'generate_plan', "form": form}

        html_template = loader.get_template('home/generate_plan.html')
        return HttpResponse(html_template.render(context, request))
    
    except Prompt.DoesNotExist:
        print("Error: Prompt with id 1 does not exist.")
        html_template = loader.get_template('home/page-500.html')
        return HttpResponse(html_template.render({}, request))
    
    except Exception as e:
        print("Error loading the page:", e)
        html_template = loader.get_template('home/page-500.html')
        return HttpResponse(html_template.render({}, request))
    




# @login_required(login_url="/login/")
def analyze_plan(request):  
    try:
        print("hi........................................", Prompt.objects.values())
        # Fetch a single instance instead of a queryset
        prompt_obj = Prompt.objects.get(_id='2')

        form = UpdatePromptForm(request.POST or None,instance=prompt_obj) 
        if request.POST:
            print("post")
           
            if form.is_valid():
                # Save the form data if valid
                form.save()
                messages.success(request, "Prompt updated successfully!")
                return redirect('analyze_plan')  # Redirect to avoid resubmission

            else:
                # Display error message if form is invalid
                messages.error(request, "There was an error updating the prompt. Please try again.")
        # else:
        #     # Pass the instance to the form
        # form = UpdatePromptForm(instance=prompt_obj)

        print("form:::",form)
        
        context = {'segment': 'analyze_plan', "form": form}

        html_template = loader.get_template('home/analyze_plan.html')
        return HttpResponse(html_template.render(context, request))
    
    except Prompt.DoesNotExist:
        print("Error: Prompt with id 1 does not exist.")
        html_template = loader.get_template('home/page-500.html')
        return HttpResponse(html_template.render({}, request))
    
    except Exception as e:
        print("Error loading the page:", e)
        html_template = loader.get_template('home/page-500.html')
        return HttpResponse(html_template.render({}, request))
    


# @login_required(login_url="/login/")
def reference_excel(request):  
    try:
        context = {'segment': 'reference_excel'}

        html_template = loader.get_template('home/reference_excel.html')
        return HttpResponse(html_template.render(context, request))
   
    
    except Exception as e:
        print("Error loading the page:", e)
        html_template = loader.get_template('home/page-500.html')
        return HttpResponse(html_template.render({}, request))

