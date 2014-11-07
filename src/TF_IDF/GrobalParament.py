# -*- coding: utf-8 -*-
'''
Created on 2014-10-26
@author: zhanghb
'''
InputFormatList=['utf-8'] #输入文件的编码列表
OutputFormatList=['utf-8']#输出文件的编码列表
pattern="full"      #搜索模式:"full"为全文搜索模式,"keys"为关键词搜索模式
n=10                #关键词搜索时的关键词数量
ruler_list=[]       #不需要的字符
result_file_num=50  #需要查找多少个相关文档
out_to_file=True    #是否需要输出为txt
PreprocessResultDir="E:\\EclipseProjection\\Python\\TF_IDF\\test"#预处理文件目录
PreprocessResultName="pro_res.txt"                               #预处理文件名
ResultFileNameDir="E:\\EclipseProjection\\Python\\TF_IDF\\test"  #搜索结果文件目录
ResultFileName="result.txt"                                      #搜索结果文件名