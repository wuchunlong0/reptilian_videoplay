# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http.response import HttpResponseRedirect, HttpResponse
from myAPI.videoURL import video_url_list
from blog.models import Video, Browse
from myAPI.pageAPI import djangoPage,PAGE_NUM

#观看视频网站 http://localhost:8000/blog/videoplay
def videoplay(request):
    url = ''
    line_list = video_url_list
    Browse.objects.filter().update(computer=str(int(Browse.objects.get().computer)+1))
    if request.method != 'POST':        
        l = 1
        lineroad = line_list[0]
        
        return render(request, 'blog/videoplay.html', context=locals()) 
    cleanData = request.POST.dict()
    url = cleanData.get('url','').strip()
    lineroad = cleanData.get('lineroad','').strip()
    name = cleanData.get('name','').strip()
    l = line_list.index(lineroad) + 1
    return render(request, 'blog/videoplay.html', context=locals())

# http://localhost:8000/blog/vipplay
def vipplay(request, page):
    if request.method == 'POST':
        Browse.objects.filter().update(mobilephone=str(int(Browse.objects.get().mobilephone)+1))
        cleanData = request.POST.dict()
        url = cleanData.get('url','').strip()
        name = cleanData.get('name','').strip()
        tvname = cleanData.get('tvname','').strip()
        if '央视网' in tvname:
            lineroad = video_url_list[4] #线路5       
        elif '土豆' in tvname  or '56我乐' in tvname or 'KU6.com' in tvname\
          or '网易视频' in tvname  or '新浪视频' in tvname  or '6.CN' in tvname\
          or '酷狗音乐' in tvname or '爆米花网' in tvname or '凤凰视频' in tvname\
          or '看看新闻' in tvname or '时光网' in tvname:
            return HttpResponseRedirect(url)
        elif '华数TV' in tvname or '1905' in tvname:
            lineroad = video_url_list[1] #线路2
        elif '音悦Tai' in tvname or '糖豆' in tvname:
            lineroad = video_url_list[7] #线路8        
        else:    
            lineroad = video_url_list[0] #线路1 
    line_list = video_url_list
    videos = Video.objects.values().order_by('-date', '-id') 
    cleanData = request.GET.dict()
    queryString = '?'+'&'.join(['%s=%s' % (k,v) for k,v in cleanData.items()]) 
    videos, pageList, num_pages, page = djangoPage(videos,page,PAGE_NUM)  #调用分页函数       
    offset = PAGE_NUM * (page - 1)            
    return render(request, 'blog/vipplay.html', context=locals())
