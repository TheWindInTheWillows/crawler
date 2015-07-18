#_*_coding:utf-8_*_

import re
import urllib2
import time

s1 = "http://so.zuiben.com/?q=%E6%88%90%E9%BE%99&c=1&fields="
s2 = "http://www.zuiben.com/down/1_212909_1/hdmp4"

last_page_patten = '<h1><a href="http://www.zuiben.com/movie/(.*?)"'
Thunder_url_patten = 'value="(thunder://.*?)" />(.*?)</li>'
MAX_PAGE = 10
#MAX_PAGE = raw_input()

class A67():
    def __init__(self):
        self.first_url_list = []
        self.last_url_num_list = []
        self.last_url_list = []
        self.Thunder_url_list = []
        for i in range(1,MAX_PAGE):
            self.first_url_list.append(s1+"&page="+str(i))
        #print self.first_url_list
    def getThunderHref(self):
        for first_url in self.first_url_list:
           # try:

            text = urllib2.urlopen(first_url).read()
            self.last_url_num_list += re.findall(last_page_patten,text,re.S)
                
                #print self.last_url_num_list

        for last_url_num in self.last_url_num_list:
            self.last_url_list.append("http://www.zuiben.com/down/1_"+str(last_url_num)+"_1/hdmp4")

        for last_url in self.last_url_list:
            text = urllib2.urlopen(last_url).read()

            self.Thunder_url_list += re.findall(Thunder_url_patten,text,re.S)
        #print self.Thunder_url_list
        for thunder_url in self.Thunder_url_list:
            print thunder_url[0]+'\n'

if __name__ == '__main__':
    crawler = A67()
    crawler.getThunderHref()





