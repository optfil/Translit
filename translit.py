# -*- coding: utf-8 -*-
"""
Created on Thu Jul 7 18:04:17 2016

@author: dergachev
"""

dict_ = {
    u'à': 'a' ,
    u'á': 'b' ,
    u'â': 'v' ,
    u'ã': 'g' ,
    u'ä': 'd' ,
    u'å': 'e' ,
    u'¸': 'yo' ,
    u'æ': 'hz' ,
    u'ç': 'z' ,
    u'è': 'i' ,
    u'é': 'j' ,
    u'ê': 'k' ,
    u'ë': 'l' ,
    u'ì': 'm' ,
    u'í': 'n' ,
    u'î': 'o' ,
    u'ï': 'p' ,
    u'ð': 'r' ,
    u'ñ': 's' ,
    u'ò': 't' ,
    u'ó': 'u' ,
    u'ô': 'f' ,
    u'õ': 'x' ,
    u'ö': 'c' ,
    u'÷': 'hc' ,
    u'ø': 'w' ,
    u'ù': 'hw' ,
    u'ú': 'hq' ,
    u'û': 'yi' ,
    u'ü': 'q' ,
    u'ý': 'ye' ,
    u'þ': 'yu' ,
    u'ÿ': 'ya'
}

def rus2latin(str):
    res = ""
    for c in str:
        print dict_[c]
    return res

def latin2rus(str):
    pass