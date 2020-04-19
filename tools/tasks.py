#!usr/bin/env python  
#-*- coding:utf-8 _*-  
""" 
@author:binbinzhang
@file: tasks.py 
@version:3.6
@time: 2020/04/19 
@email:Avvwang@qq.com
@function： 
"""
from __future__ import absolute_import, unicode_literals
from celery import shared_task
import smtplib
from email.mime.text import MIMEText
from email.utils import formataddr

from tools.lib import Error_log
@shared_task
def send_email(*args,**kwargs):
    content = kwargs.get("content")
    address=kwargs.get("address")
    my_sender = '1050603353@qq.com'  # 发件人邮箱账号
    my_pass = 'amhuejclmqgnbcea'  # 发件人邮箱密码
    my_user = address  # 收件人邮箱账号，我这边发送给自己
    try:
        msg = MIMEText(content, 'plain', 'utf-8')
        msg['From'] = formataddr(["FromRunoob", my_sender])  # 括号里的对应发件人邮箱昵称、发件人邮箱账号
        msg['To'] = formataddr(["zctianluo", my_user])  # 括号里的对应收件人邮箱昵称、收件人邮箱账号
        msg['Subject'] = "zctianluo - 申请信息"  # 邮件的主题，也可以说是标题
        server = smtplib.SMTP_SSL("smtp.qq.com", 25)  # 发件人邮箱中的SMTP服务器，端口是25
        server.login(my_sender, my_pass)  # 括号中对应的是发件人邮箱账号、邮箱密码
        server.sendmail(my_sender, [my_user, ], msg.as_string())  # 括号中对应的是发件人邮箱账号、收件人邮箱账号、发送邮件
        server.quit()  # 关闭连接
    except Exception as f:  # 如果 try 中的语句没有执行，则会执行下面的 ret=False
        print(f,"有问题啊")
    return True