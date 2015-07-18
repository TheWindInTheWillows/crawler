# -*- coding: utf-8 -*-
import re
import urllib2
import thread
import time
import Crawler
import HTML_Tool

def main():
    first_url = raw_input(u"""请输入首地址：""")
    deepth = int(raw_input(u"""请输入层数："""))
    examlpe_url = raw_input(u"""请输入示例下载链接""")

    crawler_model = Crawler(first_url,deepth,examlpe_url)
    crawler_model.start()
    for items in crawler_model.final_url_list:
        print items + '\n'

        
    
    

if __name__ == "__main__":
    print u""" 
    --------------------------------------- 
       程序：Crawler 
       版本：version 1.0 
       作者：224
       日期：2015-07-11
       语言：Python 2.7 
       操作： 
       功能：
    --------------------------------------- 
    """ 
    main()