#encoding=utf-8
#from HTMLParser import HTMLParser
from lxml import etree
from lxml import html
import urllib
from collections import OrderedDict
from product_info import product
import json
import sys
import re,os
import json
class myparser:
	hrefs=None
	href=None
	filePath=None
	filename=None
	file=None
	def __init__(self,file_name):
		#file_object=open(file_name,"rb")
		#strDoc=file_object.read().decode('utf-8')
		file_object=open(file_name,"r")
		strDoc=file_object.read()
		#print(strDoc)
		page = etree.HTML(strDoc)

		self.hrefs = page.xpath(u"//a")
		#print("self.hrefs : "+str(self.hrefs[0].attrib))
		pass

	def __init__(self):
	#file_object=open(file_name,"rb")
	#strDoc=file_object.read().decode('utf-8')
		
		#print("self.hrefs : "+str(self.hrefs[0].attrib))
		pass

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
	def getPrice(self,skuId):

		reqURL = 'https://p.3.cn/prices/mgets?skuIds=J_'+skuId
		resultJSON=None
		try:
			resultJSON = urllib.urlopen(reqURL).read().decode("utf-8")
		except Exception as e:
			print(" Erro url is "+reqURL)
			time.sleep(1)
			print("Exception: attemp to try again... to fetch "+reqURL)
			try:
				resultJSON=urllib.urlopen(reqURL).read().decode("utf-8")
				print("successfully fetch "+reqURL)
			except Exception as e:
				print(" Erro url is "+reqURL)
				print("Faild to fetch "+reqURL)
		print('tmpJSONDic = '+tmpJSONDic)
		# tmpJSONDic = json.loads(resultJSON)
		# pricetmp = tmpJSONDic[0][u'p']
		# price = pricetmp[0:]
		price='0'
		return price

	def getFinalArg(self,lis):
		file=self.file
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
		
		# print(file)
		for i in range(3,pNum):

			pskuHTML=str(etree.tostring(psku[i],encoding='utf-8',pretty_print=True,method='html'))
			pskuId=re.compile(pskuPattern,re.S).findall(pskuHTML)
			if(len(pskuId)>0):
				#print('pskuId'+str(i)+' : '+pskuId[0])
				print >>file,'pskuId'+str(i)+' : '+pskuId[0]
				price=self.getPrice(pskuId[0])
				# print('price'+str(i)+' : '+price)
				print >>file,'price'+str(i)+' : '+price


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
		print(file_name)
		lis=self.getPlist(file_name)
		self.getProductList(lis)
		pass

	def runDemo(self):
		fileHTMLPath=self.getFilePath()
		# print(filePath)
		fileFolder='/data/html-res/'
		filePath=fileFolder+self.filename
		if os.path.isdir(fileFolder):
			self.file=open(filePath,"w")
		else:
			os.makedirs(fileFolder)
			self.file=open(filePath,"w")
		print >>self.file,filePath
		lis=self.getPlist(fileHTMLPath)
		self.getProductList(lis)
		pass
# file_name = str(sys.argv[1])
# parser=myparser(file_name)
# parser.run(file_name)
#parser.show_result()
