#!usr/bin/env python  
#-*- coding:utf-8 _*-  
""" 
@author:binbinzhang
@file: lib.py 
@version:3.6
@time: 2020/04/19 
@email:Avvwang@qq.com
@function： 
"""
def Error_log(**kwargs):
    with open("./log.log", mode="a+")as f:
            f.write(f"{kwargs}-申请数据 请检查\n")