# -*- coding: utf-8 -*-
'''
Created on 2014-10-26
@author: zhanghb
'''
#多字符串替换函数，对于str_source中的某些字符（从*words传入）用char代替
def str_replace(str_source,char,*words):
    str_temp=str_source    
    for word in words:
        str_temp=str_temp.replace(word,char)
    return str_temp