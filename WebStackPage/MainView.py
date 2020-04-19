# coding=utf-8

from django.http import HttpResponseRedirect,JsonResponse,HttpResponse
from django.shortcuts import render
from WebStackPage.models import menu,content
from django.views.decorators.cache import cache_page

def Index(request):
    if request.method=="POST":
        req_type=request.GET.get("type")
        if req_type=="Get_content":
            select=request.POST.get("select")
            obj=menu.objects.get(title=select).content.values()
            return JsonResponse({"code":200,"data":list(obj)})
        else:
            obj=menu.objects.values().order_by("-create_time")
            return JsonResponse({"code":200,"data":list(obj)})
    else:
        t_id=list(menu.objects.filter(id=1).values())[0]
        t_contnet=list(content.objects.filter(type_id=t_id["id"]).values())
        frist_content={"id":t_id["title"],"content":t_contnet}
        return render(request,"en/index.html",context={"main":frist_content})
    return render(request,"en/index.html")



def about(request):
    return  render(request,"en/about.html")


def Edit(request):
    if request.method=="POST":
        req_type=request.GET.get("type")
        if req_type=="edit":
            obj=content.objects.values()
            return  JsonResponse({"code":0,"data":list(obj),"count":obj.count()})
        elif req_type=="add_website":
            params = eval(request.POST.get("data"))
            select_type=params.pop("select")
            if select_type=="add":
                params=eval(request.POST.get("data"))
                content.objects.create(**params)
            elif select_type=="update":
                content.objects.filter(id=params.pop("id")).update(**params)
            return JsonResponse({"code":200})


    m=list(menu.objects.values())
    return render(request,"include/System.html",context={"main":m})

@cache_page(60 * 30)
def video(request):
    return render(request,"include/video.html")


def test(request):
    return  render(request,"include/test.html")