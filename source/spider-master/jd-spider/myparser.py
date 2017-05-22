#encoding=utf-8
#from HTMLParser import HTMLParser
from lxml import etree
from lxml import html
import urllib2
import urllib
from collections import OrderedDict
from productInfo import product
import redisoperate
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
		'User-Agent' : 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2924.87 Safari/537.36'
		# '':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2661.102 Safari/537.36'
	}
	proxies = {
		'http': '222.85.50.90:808',
		'http': '222.85.39.168:808',
		'http': '121.232.144.48:9000',
		'http': '220.248.87.214:8080',
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
		# https://p.3.cn/prices/mgets?callback=jQuery9741103&type=1&area=1&pdtk=&pduid=630457320&pdpin=&pdbp=0&skuIds=J_4835534%2CJ_3478880%2CJ_3846673%2CJ_3129274%2CJ_11384140980%2CJ_11301207840&source=item-pc
		# reqURL = "https://p.3.cn/prices/mgets?type=1&area=1&pdtk=&pduid=630457320&pdpin=&pdbp=0&source=item-pc&skuIds="+skuIds
		#reqURL = "https://p.3.cn/prices/mgets?type=1&area=1_72_4137_0&pdtk=&pduid=14931164980011724710239&pdpin=&pdbp=0&source=item-pc&skuIds="+skuIds

		# reqURL = "https://p.3.cn/prices/mgets?type=1&area=1&pdtk=&pduid=630457320&pdpin=&pdbp=0&skuIds="+skuIds
		# reqURL = "https://p.3.cn/prices/mgets?type=1&area=1_72_4137_0&pdtk=&pduid=14931164980011724710239&pdpin=&pdbp=0&source=item-pc&skuIds="+skuIds
		# reqURL = "https://p.3.cn/prices/mgets?type=1&area=1_72_4137_0&pdtk=&pduid=1831729587&pdpin=&pdbp=0&source=item-pc&skuIds="+skuIds
		# reqURL = "https://p.3.cn/prices/mgets?type=1&area=1_72_4137_0&pdtk=&pduid=1831729587&pdpin=&pdbp=0&source=item-pc&skuIds="+skuIds
		# reqURL = "https://p.3.cn/prices/mgets?type=1&area=1_72_4137_0&pdtk=&pduid=1831729587&pdpin=&pdbp=0&source=item-pc&skuIds="+skuIds
		reqURL = "https://p.3.cn/prices/mgets?type=1&area=1_72_4137_0&pdtk=&pduid=1831729587&pdpin=&pdbp=0&source=item-pc&skuIds="+skuIds
		# reqURL = "https://p.3.cn/prices/mgets?type=1&area=1_72_4137_0&pdtk=&pduid=14851498348671083659200&pdpin=&pdbp=0&source=item-pc&skuIds="+skuIds
		print('reqURL : '+reqURL)
		resultJSON=''
		# reqJSON=None
		try:
			# print self.headers
			# req = urllib2.Request(reqURL,header=send_headers)
			# resultJSON = urllib2.urlopen(req).read().decode("utf-8")
			resultJSON = urllib.urlopen(reqURL).read().decode("utf-8")
			# print("resultJSON : "+resultJSON)
			# reqJSON = urllib.urlopen(url=reqURL,proxies=self.proxies,timeout=3000)
			# reqJSON = urllib.urlopen(url=reqURL)
			# print(reqJSON.info())
		except Exception as e:
			print(" Erro url is "+resultJSON)
			time.sleep(random.random()*5)
			print("Exception: attemp to try again... to fetch ")
			try:
				resultJSON=urllib.urlopen(reqURL).read().decode("utf-8")
				# print("resultJSON : "+resultJSON)
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
		# print('------------prices start----------')
		# print(prices)
		# print('------------prices end----------')
		return prices

	# def getCommentSummary(self,summaries,skuId):
	# 	summary = ''
	# 	summaries = json.loads(str(summaries))
	# 	summaries = summaries['CommentsCount']
	# 	for item in summaries:
	# 		# item = json.loads(str(item))
	# 		# print("item-summary : "+str(item))
	# 	#	print("summary['ShowCountStr'] : "+item['ShowCountStr'])
	# 		break
	# 	return summary


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

	def getPJSON(self,prices):
		pricesJSON = json.loads(prices)
		# key-value id-p
		pJSON = {}
		# print("pricesJSON : "+str(pricesJSON))
		for i in range(0,len(pricesJSON)):
			#print("pricesJSON[ "+str(i) +" ] :"+str(pricesJSON[i]))
			pid = str(pricesJSON[i][u'id'])
			pprice = str(pricesJSON[i][u'p'])
			pJSON.setdefault(pid,pprice)
			pass
		return pJSON

	def getSJSON(self,summaries):
		summariesJSON = json.loads(summaries)
		# key-value id-p
		summariesJSON = summariesJSON['CommentsCount']
		sJSON = {}
		# print("pricesJSON : "+str(pricesJSON))
		for i in range(0,len(summariesJSON)):
			#print("pricesJSON[ "+str(i) +" ] :"+str(pricesJSON[i]))
			productId = str(summariesJSON[i][u'ProductId'])
			commentCount = str(summariesJSON[i][u'CommentCount'])
			commentCountStr = str(summariesJSON[i][u'CommentCountStr'])
			averageScore = str(summariesJSON[i][u'AverageScore'])
			generalCount = str(summariesJSON[i][u'GeneralCount'])
			generalRate = str(summariesJSON[i][u'GeneralRate'])
			goodCount = str(summariesJSON[i][u'GoodCount'])
			goodRate = str(summariesJSON[i][u'GoodRate'])
			poorCount = str(summariesJSON[i][u'PoorCount'])
			poorRate = str(summariesJSON[i][u'PoorRate'])
			tmpJSON = {}
			tmpJSON.setdefault("productId",productId)
			tmpJSON.setdefault("commentCount",commentCount)
			tmpJSON.setdefault("commentCountStr",commentCountStr)
			tmpJSON.setdefault("averageScore",averageScore)
			tmpJSON.setdefault("generalCount",generalCount)
			tmpJSON.setdefault("generalRate",generalRate)
			tmpJSON.setdefault("goodCount",goodCount)
			tmpJSON.setdefault("goodRate",goodRate)
			tmpJSON.setdefault("poorCount",poorCount)
			tmpJSON.setdefault("poorRate",poorRate)
			sJSON.setdefault(productId,tmpJSON)
			pass
		return sJSON

	def getFinalArg(self,lis):
		file=self.file
		jsonfile=self.jsonfile
		pskuPattern='data-sku="(.*?)"'
		psku=lis[0].xpath(u"//div[@class='gl-i-wrap j-sku-item']")
		# lislen = len(lis)
		# lis0HTML=str(etree.tostring(lis[0],encoding='utf-8',pretty_print=True,method='html'))
		# lis1HTML=str(etree.tostring(lis[1],encoding='utf-8',pretty_print=True,method='html'))
		# print('lislen : '+str(lislen))
		# print('lis0HTML : '+lis0HTML)
		# print('lis1HTML : '+lis1HTML)

		#pImgPattern='src="(.*?)">'
		# pImgPattern='(src|data-lazy-img)="(.*?)">'
		# pImg=lis[0].xpath(u"//div[@class='p-img']")

		# pNamePattern='<em>(.*?)</em>'
		# pName=lis[0].xpath(u"//div[@class='p-name']")

		# pShopPattern='data-shop_name="(.*?)"'
		# pShop=lis[0].xpath(u"//div[@class='p-shop']")
		# pNum=len(pImg)
		# print("pImg len : "+str(len(pImg)))
		# print >>file,"pImg len : "+str(len(pImg))

		skuIds=''
		referenceIds=''
		for i in range(0,len(lis)):
			pskuHTML=str(etree.tostring(psku[i],encoding='utf-8',pretty_print=True,method='html'))
			print >>jsonfile,'sku+summaries : '+pskuHTML
			# print('pskuHTML'+str(i)+" : "+pskuHTML)
			pskuId=re.compile(pskuPattern,re.S).findall(pskuHTML)
			if(len(pskuId)>0):
				skuIds=skuIds+'J_'+pskuId[0]+'%2C'
				referenceIds=referenceIds+pskuId[0]+','
		prices=self.getPrices(skuIds)
		summaries=self.getCommentSummaries(referenceIds)
		# print('prices = '+prices)
	#	print('summaries = '+summaries)
		print >>jsonfile,prices
		print >>file,'summaries='+' : '+summaries

		# pricesJSON = json.loads(prices)
		# key-value id-p
		# pJSON = {}
		pJSON = self.getPJSON(prices)
		sJSON = self.getSJSON(summaries)
		# for i in range(0,len(pricesJSON)):
		# 	#print("pricesJSON[ "+str(i) +" ] :"+str(pricesJSON[i]))
		# 	pid = str(pricesJSON[i][u'id'])
		# 	pprice = str(pricesJSON[i][u'p'])
		# 	pJSON.setdefault(pid,pprice)
		# 	pass
		# print('pJSON keys : '+str(pJSON.keys()))
		# print(file)
		for i in range(0,len(lis)):
			pInfo = product()
			lisHTML=str(etree.tostring(lis[i],encoding='utf-8',pretty_print=True,method='html'))
			listmp = etree.HTML(lisHTML.decode('utf-8'))
			# listmp0HTML=str(etree.tostring(listmp[0],encoding='utf-8',pretty_print=True,method='html'))
			# print('listmp0HTML : '+listmp0HTML)
			#pImgPattern='src="(.*?)">'
			pImgPattern='(src|data-lazy-img)="(.*?)">'
			pImg=listmp[0].xpath(u"//div[@class='p-img']")

			pNamePattern='<em>(.*?)</em>'
			pName=listmp[0].xpath(u"//div[@class='p-name']")

			pShopPattern='data-shop_name="(.*?)"'
			pShop=listmp[0].xpath(u"//div[@class='p-shop']")
			pNum=len(pImg)

			psku=listmp[0].xpath(u"//div[@class='gl-i-wrap j-sku-item']")
			pskuHTML=str(etree.tostring(psku[0],encoding='utf-8',pretty_print=True,method='html'))
			print >>jsonfile,"getprice : "+pskuHTML
			pskuId=re.compile(pskuPattern,re.S).findall(pskuHTML)
			if(len(pskuId)>0):
				# print('pskuId'+str(i)+' : '+pskuId[0])
				# print >>file,'pskuId'+str(i)+' : '+pskuId[0]
				skuId = 'J_'+pskuId[0]
				pInfo.productId=pskuId[0]

				price=pJSON[skuId]
				pInfo.pPrice=pJSON[skuId]

				commentCount=sJSON[pskuId[0]]['commentCount']
				pInfo.commentCount=commentCount

				commentCountStr=sJSON[pskuId[0]]['commentCountStr']
				pInfo.commentCountStr=commentCountStr

				averageScore=sJSON[pskuId[0]]['averageScore']
				pInfo.averageScore=averageScore

				generalCount=sJSON[pskuId[0]]['generalCount']
				pInfo.generalCount=generalCount

				generalRate=sJSON[pskuId[0]]['generalRate']
				pInfo.generalRate=generalRate

				goodCount=sJSON[pskuId[0]]['goodCount']
				pInfo.goodCount=goodCount

				goodRate=sJSON[pskuId[0]]['goodRate']
				pInfo.goodRate=goodRate

				poorCount=sJSON[pskuId[0]]['poorCount']
				pInfo.poorCount=poorCount

				poorRate=sJSON[pskuId[0]]['poorRate']
				pInfo.poorRate=poorRate

				# price -
				# averageScore +
				# commentCount +
				# goodRate +
				pInfo.result = float(goodRate)*float(averageScore)*float(commentCount)/float(price)
				pInfo.resultpop = float(goodRate)*float(averageScore)*float(commentCount)
				# pInfo.result = float(goodRate)*float(averageScore)*float(commentCount)
				# summary=self.getCommentSummary(summaries,pskuId[0])
				# print('price'+str(i)+' : '+price)
				# print >>file,'price'+str(i)+' : '+price
				pass


			pImgHTML=str(etree.tostring(pImg[0],encoding='utf-8',pretty_print=True,method='html'))
			pImgSrc=re.compile(pImgPattern,re.S).findall(pImgHTML)
			# <a target="_blank" href="//item.jd.com/3719293.html">
			pURLPattern = 'target="_blank" href="(.*?)"'
			pURL = re.compile(pURLPattern,re.S).findall(pImgHTML)
			#print('pImgHTML : '+pImgHTML)
			# if(i>3):
			# 	print('pImg'+str(i)+' : '+etree.tostring(pImg[i],encoding='utf-8',pretty_print=True,method='html'))
			if(len(pURL)>0):
				# pURLtmp = pURL[0]
				pInfo.pURL = pURL[0]

			if(len(pImgSrc)>0):
				# print('pImgSrc'+str(i)+' : '+pImgSrc[0])
				# print('pImgSrc'+str(i)+' : '+pImgSrc[0][1])
				pImgurl = pImgSrc[0][1]
				pos = pImgurl.find('/jfs')
				pos = pos+4
				pInfo.pImg = pImgurl[pos:]
				print >>file,'pImgSrc'+str(i)+' : '+pImgSrc[0][1]

			pNameHTML=str(etree.tostring(pName[0],encoding='utf-8',pretty_print=True,method='html'))
			pNameTemp=re.compile(pNamePattern,re.S).findall(pNameHTML)
			if(len(pNameTemp)>0):
				# print('pName'+str(i)+' : '+pNameTemp[0])
				pInfo.pName = pNameTemp[0]
				print >>file,'pName'+str(i)+' : '+pNameTemp[0]

			pShopHTML=str(etree.tostring(pShop[0],encoding='utf-8',pretty_print=True,method='html'))
			pShopName=re.compile(pShopPattern,re.S).findall(pShopHTML)
			if(len(pShopName)>0):
				# print('pShopName'+str(i)+' : '+pShopName[0])
				pInfo.pShop = pShopName[0]
				print >>file,'pShopName'+str(i)+' : '+pShopName[0]
			#print('pName'+' : '+pNameTemp)
			# print('-----------------------------------------------------------------------------')
			# print("pInfo : "+pInfo.pName)
			rdb = redisoperate.Database()
			rdb.add_productInfo(pInfo)
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
