#-*- coding:utf8 -*-
'''
Created on 2017年12月26日

@author: liuyazhuang
'''
import os

def run(**args):
    print "[*] In dirlister module."
    files = os.listdir(".")
    return str(files)