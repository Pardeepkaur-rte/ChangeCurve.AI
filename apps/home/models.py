# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Prompt(models.Model):
    _id=models.CharField(max_length=10,blank=False,null=False, primary_key=True)
    name = models.CharField(max_length=150, blank=False, null=False)
    instructions = models.TextField(blank=False, null=False) 
    updated_at = models.DateTimeField(auto_now=True,db_column="updatedAt")

    class Meta:
        db_table = "prompts"

