#encoding=utf-8
#from HTMLParser import HTMLParser
from lxml import etree
from lxml import html
import urllib2
import urllib
from collections import OrderedDict
from product_info import product
import json
import sys,time
import re,os
import json,random
class myparser:
	hrefs=None
	href=None
	filePath=None
	filename=None
	file=None
	jsonfile=None
	user_agent = 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'
	send_headers = {
		'Accept' : 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
		# 'Accept-Encoding': 'gzip, deflate, sdch, br',
		# 'Accept-Language': 'zh-CN,zh;q=0.8',
		# 'Cache-Control' : 'max-age=0',
		# 'Connection' : 'keep-alive',
		# 'Host' : 'p.3.cn',
		# 'Upgrade-Insecure-Requests' : 1,
		'User-Agent' : 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'
	}
	proxies = {
		'http': '123.165.125.168:8118',
		'http': '1.196.235.12:808',
		'http': '112.234.52.97:24688',
		'http': '117.65.3.71:9649',
		'http': '117.69.12.90:22667',
		'http': '122.237.40.24:808',
		'http': '171.13.37.194:808',
		'http': '223.153.104.190:13919',
		'http': '175.7.149.211:28826'
	}

	def __init__(self):
		# file_object=open(file_name,"rb")
		# strDoc=file_object.read().decode('utf-8')

		# print("self.hrefs : "+str(self.hrefs[0].attrib))
		pass

	# def __init__(self,file_name):
	# 	#file_object=open(file_name,"rb")
	# 	#strDoc=file_object.read().decode('utf-8')
	# 	print file_name
	# 	if(len(file_name)!=0):
	# 		file_object=open(file_name,"r")
	# 		strDoc=file_object.read()
	# 		# print(strDoc)
	# 		page = etree.HTML(strDoc)

	# 		self.hrefs = page.xpath(u"//a")
	# 	#print("self.hrefs : "+str(self.hrefs[0].attrib))
	# 	pass

	#def __init__(self):
	#file_object=open(file_name,"rb")
	#strDoc=file_object.read().decode('utf-8')

		#print("self.hrefs : "+str(self.hrefs[0].attrib))
		#pass

	def setFilePath(self,folderPath,file_name):
		filePath=folderPath+file_name
		self.filePath=filePath
		self.filename=file_name
		file_object=open(filePath,"r")
		strDoc=file_object.read()
		#print(strDoc)
		page = etree.HTML(strDoc)

		self.hrefs = page.xpath(u"//a")
		pass

	def getFilePath(self):
		return self.filePath

	def split_out_http(self,orginal_string):
		domain_url="https://list.jd.com"
		#pattern="'href': '(.*?)((', ')|('}))"
		pattern="'href': '(.*?)'}"
		orginal_res=re.compile(pattern,re.S).findall(orginal_string)
		#if(orginal_res!=None):
		orginal_res=orginal_res[0]
		print("orginal_res : "+orginal_res)
		if(len(orginal_res)>3):
			return domain_url+orginal_res
		else:
			return len(orginal_res)
		"""
		orginal_temp=orginal_string.strip()
		orginal_res=orginal_temp.split("\'",5)
		if(len(orginal_res)>3):
			if "http://" in orginal_res[3]:
				return orginal_res[3]
			else:
				return ''
		else:
			return len(orginal_res)
		"""

	def show_result(self):
		for href in self.hrefs:
			line=str(href.attrib)
			print("line : "+line)
			temp_split_res=self.split_out_http(line)
			if(len(temp_split_res)!=0):
				print(self.split_out_http(line))
		return ''

	def getPlist(self,file_name):
		file_object=open(file_name,"rb")
		strDoc=file_object.read().decode('utf-8')
		#print(str(strDoc))
		page = etree.HTML(strDoc)
		#print("page : "+str(page.text)+str(etree.tostring(page)))
		pattern='<ul class="gl-warp clearfix ">(.*?)</ul>'
		uls=page.xpath(u"//ul[@class='gl-warp clearfix ']")
		lis=uls[0].xpath(u"//li[@class='gl-item']")
		return lis
		#print("li : "+str(etree.tostring(lis[0],pretty_print=True)))
		#for ul in uls:
		#	print("ul : "+str(etree.tostring(ul,pretty_print=True)))

		#return uls
		#Plist=re.compile(pattern,re.S).findall()
	def getProductList(self,lis):
		self.getFinalArg(lis)
		#plist=[]
		#p.append()
		#return list
		pass
	def getPrice(self,prices,skuId):
		price = ''
		prices = json.loads(str(prices))
		for item in prices:
			# item = json.loads(str(item))
			# print("item-price : "+str(item))
			# print("price['p'] : "+item['p'])
			break
			# if(item['id']=='J_'+skuId)
		return price

	def getPrices(self,skuIds):
		callback = 'callback=jQuery'+str(7148011)
		# reqURL = 'https://p.3.cn/prices/mgets?'+callback+'&skuIds='+skuIds
		# reqURL = 'https://p.3.cn/prices/mgets?skuIds='+skuIds
		reqURL = "https://p.3.cn/prices/mgets?type=1&area=1&pdtk=&pduid=630457320&pdpin=&pdbp=0&source=item-pc&skuIds="+skuIds
		print('reqURL : '+reqURL)
		resultJSON=''
		# reqJSON=None
		try:
			# print self.headers
			# req = urllib2.Request(reqURL,header=send_headers)
			# resultJSON = urllib2.urlopen(req).read().decode("utf-8")
			resultJSON = urllib.urlopen(reqURL).read().decode("utf-8")
			# reqJSON = urllib.urlopen(url=reqURL,proxies=self.proxies,timeout=3000)
			# reqJSON = urllib.urlopen(url=reqURL)
			# print(reqJSON.info())
		except Exception as e:
			print(" Erro url is "+resultJSON)
			time.sleep(random.random()*5)
			print("Exception: attemp to try again... to fetch ")
			try:
				resultJSON=urllib.urlopen(reqURL).read().decode("utf-8")
				# req = urllib2.Request(reqURL,header=send_headers)
				# resultJSON = urllib2.urlopen(req).read().decode("utf-8")
				# reqJSON = urllib.urlopen(url=reqURL)
				# print(reqJSON.info())
				print("successfully fetch ")
			except Exception as e:
				print(" Erro url is ")
				print("Faild to fetch ")
		# print(' skuId is : '+skuId+' resultJSON is :'+resultJSON)
		# tmpJSONDic = json.loads(resultJSON)
		# pricetmp = tmpJSONDic[0][u'p']
		# price = pricetmp[0:]
		# prices='0'
		prices=resultJSON
		return prices

	def getCommentSummary(self,summaries,skuId):
		summary = ''
		summaries = json.loads(str(summaries))
		summaries = summaries['CommentsCount']
		for item in summaries:
			# item = json.loads(str(item))
			# print("item-summary : "+str(item))
		#	print("summary['ShowCountStr'] : "+item['ShowCountStr'])
			break
		return summary


	def getCommentSummaries(self,referenceIds):
		# callback = 'callback=jQuery'+str(7148011)
		# reqURL = 'https://p.3.cn/prices/mgets?'+callback+'&skuIds='+skuIds
		reqURL = 'https://club.jd.com/comment/productCommentSummaries.action?my=pinglun2&referenceIds='+referenceIds+'&_=1491955601224'
		print('getCommentSummaries --- reqURL :'+reqURL)
		resultJSON=''
		# reqJSON=None
		try:
			# print self.headers
			resultJSON = urllib.urlopen(reqURL).read().decode('gbk')
			# reqJSON = urllib.urlopen(url=reqURL,proxies=self.proxies,timeout=3000)
			# reqJSON = urllib.urlopen(url=reqURL)
			# print(reqJSON.info())
		except Exception as e:
			print e
			print(" Erro url is "+resultJSON)
			time.sleep(random.random()*5)
			print("Exception: attemp to try again... to fetch ")
			try:
				# resultJSON=urllib.urlopen(reqURL).read().decode("utf-8")
				# resultJSON = urllib.urlopen(reqURL).read().decode("utf8")
				resultJSON = urllib.urlopen(reqURL).read().decode('gbk')
				# reqJSON = urllib.urlopen(url=reqURL)
				# print(reqJSON.info())
				print("successfully fetch ")
			except Exception as e:
				print(" Erro url is ")
				print("Faild to fetch ")
		# print(' skuId is : '+skuId+' resultJSON is :'+resultJSON)
		# tmpJSONDic = json.loads(resultJSON)
		# pricetmp = tmpJSONDic[0][u'p']
		# price = pricetmp[0:]
		# prices='0'
		summaries=resultJSON
		return summaries

	def getFinalArg(self,lis):
		file=self.file
		jsonfile=self.jsonfile
		pskuPattern='data-sku="(.*?)"'
		psku=lis[0].xpath(u"//div[@class='gl-i-wrap j-sku-item']")

		#pImgPattern='src="(.*?)">'
		pImgPattern='(src|data-lazy-img)="(.*?)">'
		pImg=lis[0].xpath(u"//div[@class='p-img']")

		pNamePattern='<em>(.*?)</em>'
		pName=lis[0].xpath(u"//div[@class='p-name']")

		pShopPattern='data-shop_name="(.*?)"'
		pShop=lis[0].xpath(u"//div[@class='p-shop']")
		pNum=len(pImg)
		# print("pImg len : "+str(len(pImg)))
		print >>file,"pImg len : "+str(len(pImg))


		skuIds=''
		referenceIds=''
		for i in range(3,pNum):
			pskuHTML=str(etree.tostring(psku[i],encoding='utf-8',pretty_print=True,method='html'))
			pskuId=re.compile(pskuPattern,re.S).findall(pskuHTML)
			if(len(pskuId)>0):
				skuIds=skuIds+'J_'+pskuId[0]+'%2C'
				referenceIds=referenceIds+pskuId[0]+','
		prices=self.getPrices(skuIds)
		summaries=self.getCommentSummaries(referenceIds)
		print('prices = '+prices)
	#	print('summaries = '+summaries)
		print >>jsonfile,prices
		print >>file,'summaries='+' : '+summaries
		# pricesJSON = json.loads(prices)

		# print(file)
		for i in range(3,pNum):
			pskuHTML=str(etree.tostring(psku[i],encoding='utf-8',pretty_print=True,method='html'))
			pskuId=re.compile(pskuPattern,re.S).findall(pskuHTML)
			if(len(pskuId)>0):
				# print('pskuId'+str(i)+' : '+pskuId[0])
				# print >>file,'pskuId'+str(i)+' : '+pskuId[0]
				# price=self.getPrice(prices,pskuId[0])
	#			summary=self.getCommentSummary(summaries,pskuId[0])
				# print('price'+str(i)+' : '+price)
				# print >>file,'price'+str(i)+' : '+price
				pass


			pImgHTML=str(etree.tostring(pImg[i],encoding='utf-8',pretty_print=True,method='html'))
			pImgSrc=re.compile(pImgPattern,re.S).findall(pImgHTML)
			#print('pImgHTML : '+pImgHTML)
			# if(i>3):
			# 	print('pImg'+str(i)+' : '+etree.tostring(pImg[i],encoding='utf-8',pretty_print=True,method='html'))
			if(len(pImgSrc)>0):
				#print('pImgSrc'+str(i)+' : '+pImgSrc[0])
				# print('pImgSrc'+str(i)+' : '+pImgSrc[0][1])
				print >>file,'pImgSrc'+str(i)+' : '+pImgSrc[0][1]

			pNameHTML=str(etree.tostring(pName[i],encoding='utf-8',pretty_print=True,method='html'))
			pNameTemp=re.compile(pNamePattern,re.S).findall(pNameHTML)
			if(len(pNameTemp)>0):
				# print('pName'+str(i)+' : '+pNameTemp[0])
				print >>file,'pName'+str(i)+' : '+pNameTemp[0]

			pShopHTML=str(etree.tostring(pShop[i],encoding='utf-8',pretty_print=True,method='html'))
			pShopName=re.compile(pShopPattern,re.S).findall(pShopHTML)
			if(len(pShopName)>0):
				# print('pShopName'+str(i)+' : '+pShopName[0])
				print >>file,'pShopName'+str(i)+' : '+pShopName[0]
			#print('pName'+' : '+pNameTemp)
			# print('-----------------------------------------------------------------------------')
			print >>file,'-----------------------------------------------------------------------------'
		# for i in range(3,pNum+1):
		# 	pImgHTML=str(etree.tostring(pImg[i],encoding='utf-8',pretty_print=True,method='html'))
		# 	pImgSrc=re.compile(pImgPattern,re.S).findall(pImgHTML)
		# 	print('pImgSrc'+str(i)+' : '+pImgSrc[0])

		# 	pNameHTML=str(etree.tostring(pName[i],encoding='utf-8',pretty_print=True,method='html'))
		# 	pName=re.compile(pNamePattern,re.S).findall(pNameHTML)
		# 	print('pName'+str(i)+' : '+pName[0])

		# 	pShopHTML=str(etree.tostring(pShop[i],encoding='utf-8',pretty_print=True,method='html'))
		# 	pShopName=re.compile(pShopPattern,re.S).findall(pShopHTML)
		# 	print('pShopName'+str(i)+' : '+pShopName[0])

		# 	print('-----------------------------------------------------------------------------')
		# pImgHTML=str(etree.tostring(pImg[4],encoding='utf-8',pretty_print=True,method='html'))
		# pImgSrc=re.compile(pImgPattern,re.S).findall(pImgHTML)
		# print('pImgSrc : '+pImgSrc[0])

		# pNameHTML=str(etree.tostring(pName[2],encoding='utf-8',pretty_print=True,method='html'))
		# pName=re.compile(pNamePattern,re.S).findall(pNameHTML)
		# print('pName : '+pName[0])

		# pShopHTML=str(etree.tostring(pShop[4],encoding='utf-8',pretty_print=True,method='html'))
		# pShopName=re.compile(pShopPattern,re.S).findall(pShopHTML)
		# print('pShopName : '+pShopName[0])

		#print('pImgHTML : '+pImgHTML)

		#print(etree.tostring(pImg[0],encoding='utf-8',pretty_print=True,method='html').decode())

		#pPrice=lis[0].xpath(u"//div[@class='p-price']")
		#pPrice=pPrice[0].xpath(u"//strong[@class='J_price']")
		#pPrice=pPrice[0].xpath(u"//i")


		#pName=pName[0].xpath(u"//em")
		#pCommit=lis[0].xpath(u"//div[@class='p-commit']")


		#print HTMLParser().unescape('&#20013;&#22269;')
		#h=html.html5parser.HTMLParser()
		#print("pImg : "+etree.tostring(pImg[0],encoding='utf-8',pretty_print=True,method='html').decode())
		#print("pPrice : "+etree.tostring(pPrice[0],encoding='utf-8',pretty_print=True,method='html').decode())
		#print("pName : "+etree.tostring(pName[0],encoding='utf-8',pretty_print=True,method='html').decode())
		#print("pCommit : "+etree.tostring(pCommit[0],encoding='utf-8',pretty_print=True,method='html').decode())
		#print("pShop : "+etree.tostring(pShop[0],encoding='utf-8',pretty_print=True,method='html').decode())
		file.close()
		print(self.filename+'res is ok')
		pass

	def run(self,file_name):
		self.setfile()
		print(file_name)
		lis=self.getPlist(file_name)
		self.getProductList(lis)
		pass

	def setfile(self):
		fileFolder='/data/html-res/'
		filePath=fileFolder+self.filename
		jsonFilePath=filePath+'.json'
		if os.path.isdir(fileFolder):
			self.file=open(filePath,"w")
			self.jsonfile=open(jsonFilePath,"w")
		else:
			os.makedirs(fileFolder)
			self.file=open(filePath,"w")
			self.jsonfile=open(jsonFilePath,"w")

	def runDemo(self):
		fileHTMLPath=self.getFilePath()
		# print(filePath)
		self.setfile()
		lis=self.getPlist(fileHTMLPath)
		self.getProductList(lis)
		pass
# file_name = str(sys.argv[1])
# parser=myparser(file_name)
# folderPath="/data/html-source-code/"
# filename=str(1)+'.html'
# parser.setFilePath(folderPath,filename)
# parser.run(file_name)
#parser.show_result()
