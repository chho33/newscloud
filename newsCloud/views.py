#!/usr/bin/python
# -*- coding: utf8 -*-
from django.shortcuts import render, get_object_or_404
from .models import Keywords, News2
from django.utils import timezone
from playhouse.djpeewee import translate
from peewee import fn
from django.db import connection
from pytagcloud import create_tag_image, make_tags,create_html_data
from operator import itemgetter

NEWSTABLE='news2'
FIN=u'國際'
POL=u'兩岸'
SQL_TODAY='select term, weight from keywords where keyid in (select newsid from %s where newsDate in\
    (select MAX(newsDate) from %s));'%(NEWSTABLE,NEWSTABLE)
SQL_WEEK='select term, weight from keywords where keyid in (select newsid from %s where newsDate between\
 (select ADDDATE(MAX(newsDate),-7) from %s) and (select MAX(newsDate) from %s))'%(NEWSTABLE,NEWSTABLE,NEWSTABLE)
SQL_MONTH='select term, weight from keywords where keyid in (select newsid from %s where newsDate between\
 (select ADDDATE(MAX(newsDate),-30) from %s) and (select MAX(newsDate) from %s))'%(NEWSTABLE,NEWSTABLE,NEWSTABLE)
SQL_P='select term, weight from keywords where keyid in (select newsid from %s where newsDate in\
    (select MAX(newsDate) from %s)and reclass =%s)'%(NEWSTABLE,NEWSTABLE,POL)
SQL_P_WEEK='select term, weight from keywords where keyid in (select newsid from %s where newsDate between\
 (select ADDDATE(MAX(newsDate),-7) from %s) and (select MAX(newsDate) from %s where reclass =%s))'%(NEWSTABLE,NEWSTABLE,NEWSTABLE,POL)
SQL_P_MONTH='select term, weight from keywords where keyid in (select newsid from %s where newsDate between\
 (select ADDDATE(MAX(newsDate),-30) from %s) and (select MAX(newsDate) from %s where reclass =%s))'%(NEWSTABLE,NEWSTABLE,NEWSTABLE,POL)
SQL_F=''
SQL_F_WEEK=''
SQL_F_MONTH=''




def create_cloud(sql):
    #p=translate(News2)
    #P=p.News2
    #query = (P.select(P.newsid).where(P.newsdate)==P.select(fn.MAX(P.newsdate)))
    cursor = connection.cursor()
    cursor.execute(sql)
    allterm=cursor.fetchall()
    alltermlist=list(allterm)
    alltermdic={}
    checklist=[]
    while not len(alltermlist) == 0:
        popone=alltermlist.pop()
        key=popone[0]
        value=popone[1]
        checklist.append(key)
        if key in [a[0] for a in checklist]:
            alltermdic[key]+=value
        else:
            alltermdic[key]=value
    swd = sorted(alltermdic.iteritems(), key=itemgetter(1), reverse=True)
    swd = [w for w in swd[1:50]]
    tags = make_tags(swd, maxsize=120)
    data = create_html_data(tags,
                            size=(600, 400),
                            layout=3,
                            fontname="Simhei",
                            rectangular=False)
    from string import Template
    context = {}
    with open('/Users/jojotenya/Documents/Django/News/newsCloud/template.html') as f:
        html_template = Template(f.read())
    tags_template = '<li class="cnt" style="top: %(top)dpx; left: %(left)dpx; \
        height: %(height)dpx;"><a class="tag \
        %(cls)s" href="/to_sec/%(tag)s" style="top: %(top)dpx;\
            left: %(left)dpx; font-size: %(size)dpx; height: %(height)dpx; \
        line-height:%(lh)dpx;">%(tag)s</a></li>'
    context['tags'] = ''.join([tags_template % link for link in data['links']])
    context['width'] = data['size'][0]
    context['height'] = data['size'][1]
    context['css'] = "".join("a.%(cname)s{color:%(normal)s;}\
                             a.%(cname)s:hover{color:%(hover)s;}" %
                             {'cname': k,
                              'normal': v[0],
                              'hover': v[1]}
                             for k, v in data['css'].items())
    html_text = html_template.substitute(context)
    return html_text


def get_cloud_today(request,sql=SQL_TODAY):
    html_text=create_cloud(sql)   
    return render(request, 'newsCloud/cloud_for_first.html', {'html_text':html_text})   

def get_cloud_week(request,sql=SQL_WEEK):
    html_text=create_cloud(sql)   
    return render(request, 'newsCloud/cloud_for_first.html', {'html_text':html_text})   

def get_cloud_month(request,sql=SQL_MONTH):
    html_text=create_cloud(sql)   
    return render(request, 'newsCloud/cloud_for_first.html', {'html_text':html_text})   

def get_cloud_politic(request,sql=SQL_P):
    html_text=create_cloud(sql)   
    return render(request, 'newsCloud/cloud_for_first_P.html', {'html_text':html_text})   

def get_cloud_politic_week(request,sql=SQL_P_WEEK):
    html_text=create_cloud(sql)   
    return render(request, 'newsCloud/cloud_for_first_P.html', {'html_text':html_text})   

def get_cloud_politic_month(request,sql=SQL_P_MONTH):
    html_text=create_cloud(sql)   
    return render(request, 'newsCloud/cloud_for_first_P.html', {'html_text':html_text})   





def get_second_page(request,urltag):
    sql="select term, weight from keywords where keyid in (select newsID from news2 where content like '%%%s%%')"%(urltag);
    html_text=create_cloud(sql)   
    return render(request, 'newsCloud/cloud_for_first_P.html', {'html_text':html_text}) 

def get_second_page_get(request):
    keyword=request.GET['keyword']
    sql="select term, weight from keywords where keyid in (select newsID from news2 where content like '%%%s%%')"%(keyword);
    html_text=create_cloud(sql)   
    return render(request, 'newsCloud/cloud_for_first_P.html', {'html_text':html_text}) 






