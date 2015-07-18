#_*_coding:utf-8_*_

import urllib2
import re
import time
import thread

s1 = "http://so.zuiben.com/?q=%E6%88%90%E9%BE%99&c=1&fields=&page=1"
s2 = "http://www.zuiben.com/down/1_212909_1/hdmp4"

class Movie:
	def __init__(self):
		# self.first_url = raw_input(u"""请输入要爬取的页面地址:""")
		# self.example_url = raw_input(u"""请输入含有示例下载链接的地址:""")
		self.first_url = s1
		self.example_url = s2
		self.error_msg = u"""服务暂时不可用，请重试"""
		#self.first_url_list = []
		self.last_url_list = []
		self.thunder_href_list =[]
	
	def getHTMLtext(self,url):
		try:
			return urllib2.urlopen(url).read()
		except:
			print self.error_msg
			exit()

	def getLastURLList(self,text):#返回含有迅雷下载链接的url列表
		num_list = re.findall('<h1><a href="http://www.zuiben.com/movie/(.*?)"',text,re.S)
		for num in num_list:
			self.last_url_list.append("http://www.zuiben.com/down/1_"+num+"_1/hdmp4")
		#print self.last_url_list
		if len(self.last_url_list) == 0:
			print self.error_msg
			exit()

	def getThunderHref(self,url):
		text = self.getHTMLtext(url)
		thunderlist = re.findall('value="(thunder://.*?)" />(.*?)</li>',text,re.S) #元素由二元组组成 href+title
		return thunderlist

	def getAllThunderHref(self):
		if(len(self.last_url_list)==0):
			print self.error_msg
			exit()
		else:
			for url in self.last_url_list:
				self.thunder_href_list+=self.getThunderHref(url)
				
	def _start(self):
		text = self.getHTMLtext(self.first_url)
		self.getLastURLList(text)
		self.getAllThunderHref()
		for url in self.thunder_href_list:
			print url[0]+'\n'
		
if __name__ == '__main__':
	A67_model = Movie()
	A67_model._start()
	raw_input(u"""按下回车结束：""")



