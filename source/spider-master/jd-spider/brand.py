# -*- coding: UTF-8 -*- 
import urllib
import urllib
import re
import os,time,sys
from lxml import etree
from lxml import html
import redisoperate
import json
class brandspider(object):
	"""docstring for brandspider"""
	start_url=""
	def __init__(self, url):
		super(brandspider, self).__init__()
		self.start_url=url
		reload(sys) 
		sys.setdefaultencoding('utf8')

	def getSource(self,url):
		source_html=""
		try:
			source_html=urllib.urlopen(url).read().decode("utf-8")
		except Exception as e:
			print(" Erro url is "+url)
			time.sleep(1)
			print("Exception: attemp to try again... to fetch "+url)
			try:
				source_html=urllib.urlopen(url).read().decode("utf-8")
				print("successfully fetch "+url)
			except Exception as e:
				print(" Erro url is "+url)
				print("Faild to fetch "+url)
		return source_html

	def getbrandlist(self,url):
		url = self.start_url
		source=self.getSource(url)
		page = etree.HTML(source.decode('utf-8'))
		uls=page.xpath(u"//ul[@class='J_valueList v-fixed']")
		ulsHTML = str(etree.tostring(uls[0],encoding='utf-8',pretty_print=True,method='html'))
		# print(ulsHTML)
		uls = etree.HTML(ulsHTML.decode('utf-8'))
		lis=uls[0].xpath(u"//li")
		brandnamePattern = 'title="(.*?)"'
		brandIdPattern = 'id="brand-(.*?)" data-initial="'
		pingpai = "品牌".encode('utf-8')
		baseBrandURL ="https://list.jd.com/list.html?cat=9987,653,655&ev=exbrand%5F"
		brandproNumPattern ='<span>(.*?)</span>'
		brandjson={}
		brandlist=[]
		brandnamelist=[]
		for i in range(0,len(lis)):
			lisHTML=str(etree.tostring(lis[i],encoding='utf-8',pretty_print=True,method='html'))
			brandname =re.compile(brandnamePattern,re.S).findall(lisHTML)
			brandId = re.compile(brandIdPattern,re.S).findall(lisHTML)
			# print(lisHTML)
			# print(brandId[0])
			# print(brandname[0])
			brandURL = baseBrandURL + brandId[0] + "&sort=sort_rank_asc&trans=1&JL=3_"+pingpai+"_"+brandname[0]
			# brandURL = baseBrandURL+brandname[0]
			# print(brandURL)
			brandSource = self.getSource(brandURL)
			brandSource = brandSource.decode('utf-8')
			brandSourcepage = etree.HTML(brandSource.decode('utf-8'))
			brand_st_ext=brandSourcepage.xpath(u"//div[@class='st-ext']")
			brand_st_extHTML = str(etree.tostring(brand_st_ext[0],encoding='utf-8',pretty_print=True,method='html'))
			# print(brand_st_extHTML)
			brandpronum = re.compile(brandproNumPattern,re.S).findall(brand_st_extHTML)
			brandnum = brandpronum[0]
			# print('name:'+brandname[0]+' '+'value:'+brandnum)
			brandjson.setdefault('value',int(brandnum))
			brandjson.setdefault('name',brandname[0].encode('utf-8'))
			# brandjson = json.dumps(brandjson, sort_keys=True, indent=0, ensure_ascii=False)
			# print(brandjson)
			brandlist.append(brandjson)
			brandnamelist.append(brandname[0])
			brandjson = {}
			# print('value:'+brandnum)
			# brand_ext = re.compile('')
		# brandlist = json.dumps(brandlist, sort_keys=True, indent=0, ensure_ascii=False)
		# print(brandlist)
		rdb = redisoperate.Database()
		rdb.add_brandlist(brandlist,brandnamelist)
		# rdb.get_brandlist()
		pass

# start_url = "https://list.jd.com/list.html?cat=9987,653,655"
# brandspiderDemo = brandspider(start_url)
# brandspiderDemo.getbrandlist(start_url)
