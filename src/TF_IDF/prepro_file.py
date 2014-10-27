# -*- coding: utf-8 -*-
'''
Created on 2014-10-26
@author: zhanghb
'''
#这个函数用于预处理文件处理过程中采用unicode编码
import os
from str_replace import str_replace
from TF_IDF.StrToUni import StrToUni
import GrobalParament
def prepro_file(fl_in_url,re_out_url,*wd_be_re):
    in_url=fl_in_url.replace('\\','/')
    out_url=re_out_url.replace('\\','/')
    try:
        try:
            fl_in=os.listdir(in_url)
        except WindowsError:
            print "您输入的预处理文档目录有误"
        try:
            re_out=open(out_url+'/'+'pro_res.txt')
        except WindowsError:
            print "您输入的结果文档输出目录有误"
    except NameError:
        pass
    else:
        for file in fl_in:
            afile_url=fl_in_url+'/'+file
            if os.path.isfile(afile_url):
                afile=open(afile_url,"r")
                content_temp=afile.readlines()
                content=str_replace(content_temp, '',*wd_be_re)
                con_unicode=StrToUni(content,GrobalParament.CodeFormatList)
                
        