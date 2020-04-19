# coding=utf-8
from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from tools.tasks import send_email
from tools.lib import Error_log

def summit_email(request):
    successCallback=request.GET.get("successCallback")
    name=request.GET.get("name")
    phone=request.GET.get("phone")
    product=request.GET.get("product")
    types=request.GET.get("type")
    send_email.delay(address="1050603353@qq.com",content=f"姓名:{name}\n联系方式:{phone}\n产品:{product}\n类型:{types}")
    Error_log(name=name,phone=phone,product=product,types=types)
    return HttpResponse('successCallback({"code":200})')



