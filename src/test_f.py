# -*- coding: utf-8 -*-
'''
Created on 2014-10-26
@author: zhanghb
'''
from TF_IDF.str_replace import str_replace
from TF_IDF.StrToUni import StrToUni
from jieba.analyse import extract_tags
from TF_IDF import GrobalParament
from jieba import cut
from TF_IDF.half_word_cut import halfcut
"""
def str_replace(str_source,char,*words):    
    for word in words:
        str_temp=str_source.replace(word,char)
    return str_temp
    """
s=str_replace("a\ta\nb\tc\n","\t","\n")
print s
s="中文"
k=StrToUni(s,'GBK','gb2312','utf-8')
print k
S=u"中文"
print S
K=S.encode("UTF-8")
#cut_content = extract_tags("随着各级政府逐步加大对环保基础设施的投资，截至2008年12月，中国城镇污水处理设施已经达到了1521座。但遗憾的是，目前整体处理能力仍难以满足需求，而且有超过四分之一的污水处理能力实际上处于闲置状态。　　6月22日，国家环境保护部（下称环保部）在第30号《关于公布全国城镇污水处理设施和燃煤电厂脱硫设施的公告》（下称《公告》）中称，全国投运的城镇污水处理设施总设计处理能力9092万吨/日，但实际平均日处理水量为6693万吨/日。也就是说，整个负荷率只有73.6%。　　注意到，这份清单显示，全国各城镇已投入运行的污水处理设施，除了有少部分污水处理厂的平均日处理水量符合或超过设计处理能力，相当大的一部分城镇污水处理厂，由于种种原因，其平均日处理水量远远未达到其设计目标。　　例如，2008年7月刚投产不久的内蒙古集宁区污水处理厂，其设计处理能力为3万吨/日，但实际上该污水处理厂目前每日仅能“消化”3000吨污水。此外，实际处理污水量仅为设计目标的一半甚至以下的，更是比比皆是。", GrobalParament.n)
#print list(cut_content)
cut_result=halfcut("随着各级政府逐步加大对环保基础设施的投资，截至2008年12月，中国城镇污水处理设施已经达到了1521座。但遗憾的是，目前整体处理能力仍难以满足需求，而且有超过四分之一的污水处理能力实际上处于闲置状态。　　6月22日，国家环境保护部（下称环保部）在第30号《关于公布全国城镇污水处理设施和燃煤电厂脱硫设施的公告》（下称《公告》）中称，全国投运的城镇污水处理设施总设计处理能力9092万吨/日，但实际平均日处理水量为6693万吨/日。也就是说，整个负荷率只有73.6%。　　注意到，这份清单显示，全国各城镇已投入运行的污水处理设施，除了有少部分污水处理厂的平均日处理水量符合或超过设计处理能力，相当大的一部分城镇污水处理厂，由于种种原因，其平均日处理水量远远未达到其设计目标。　　例如，2008年7月刚投产不久的内蒙古集宁区污水处理厂，其设计处理能力为3万吨/日，但实际上该污水处理厂目前每日仅能“消化”3000吨污水。此外，实际处理污水量仅为设计目标的一半甚至以下的，更是比比皆是。")
print cut_result
#print cut_content