# -*- coding: utf-8 -*-
from django.contrib import admin
from blog.models import Video, Browse
@admin.register(Video)
class VideoAdmin(admin.ModelAdmin):    
    list_display = ('id','tvname','name','url','date')

@admin.register(Browse)
class BrowseAdmin(admin.ModelAdmin):    
    list_display = ('id','computer','mobilephone')
