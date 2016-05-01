#!/usr/bin/python
# -*- coding: utf-8 -*-

from django.contrib import admin
from .models import Post

class PostAdmin(admin.ModelAdmin):
	list_display = ('Title', 'Text', 'Created_Date', 'Author')

admin.site.register(Post, PostAdmin)