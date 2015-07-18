# _*_coding:utf-8_*_
import base64
class ThunderTransfer():

	def __init__(self,normal_url,thunder_url):
		#thunder_url = NomalToThunder(normal_url)
		#normal_url = ThunderToNomal(thunder_url)
           pass


	def ThunderToNomal(thunder_url):
          normal_url = base64.decodestring(thunder_url[10:])
          return normal_url

	def NomalToThunder(normal_url):
          url = 'AA'+normal_url+'ZZ'
          thunder_url = "thunder://"+base64.encodestring(url)
          return thunder_url
thunder_transfer = ThunderTransfer()
s="thunder://QUFodHRwOi8vc3MuZHg1Ny50YW8zMC5jb206MjAxNi8xNTA3LyU2MDEzL+Wkp+Wco+W9kuadpVRTJTIwW+mrmOa4hV1bNzA2MC5sYV0ubXA0Wlo="
print thunder_transfer.ThunderToNomal(s)
