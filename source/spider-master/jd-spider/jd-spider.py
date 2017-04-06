import urllib.request
import urllib.error
import re
import os

class product(object):
	"""docstring for product"""
	pName="";
	pImgPath="";
	def __init__(self, arg):
		pName="";
		pImgPath="";
		super(product, self).__init__()
		self.arg = arg
		pName="";
		pImgPath="";
	def setpName(name):
		self.pName=name
	def setImgPath(path):
		self.pImgPath=paht
	def getpName():
		return self.pName
	def getImgPath():
		return self.pImgPath

def getSource(url):
	source_html=""
	try:
		source_html=urllib.request.urlopen(url).read().decode("utf-8")
	except Exception as e:
		print(str(e.reason)+" Erro url is "+url)
	return source_html

def getplist(partten,source):

	pass

def getproductInfo(partten,plist):
	pass

def saveImgAndpName(product):
	pass

def getlastPageNum(start_url):
	partten_lastPageNumContent='<b class="pn-break "> …</b>(.*?)<a class="pn-next"'
	partten_lastPageNum='class="">(.*?)</a>'
	source_html=getSource(start_url)
	lastPageNumContent=re.compile(partten_lastPageNumContent,re.S).findall(source_html)
	lastPageNumContent=lastPageNumContent[0]
	lastPageNum=re.compile(partten_lastPageNum,re.S).findall(lastPageNumContent)
	lastPageNum=lastPageNum[0]
	return lastPageNum

def getAmdSaveHtml(start_url):
	lastPageNum=getlastPageNum(start_url)
	print(lastPageNum)
	#for i in range (1,2):
	for i in range (1,int(lastPageNum)+1):
		url=start_url+'&page='+str(i)
		#print(url+'------------'+str(i))
		source=getSource(url)
		fileFolder="data/html-source-code/"
		filePath=fileFolder+str(i)+".html"
		if os.path.isdir(fileFolder):
			file=open(filePath,"w")
			file.write(source)
			file.close()
		else:
			os.mkdir(fileFolder)
			file=open(filePath,"w")
			file.write(source)
			file.close()
		if len(source) > 3:
			print(str(i)+".html"+' is ok! o-o')
		else:
			print(str(i)+".html"+' is error!')


#start_url="https://list.jd.com/list.html?cat=9987,653,655"
#getAmdSaveHtml(start_url)

#lastPageNum=getlastPageNum(start_url)
#print(lastPageNum)
#for i in range (1,2):
#for i in range (1,int(lastPageNum)+1):
	#url=start_url+'&page='+str(i)
	#print(url+'------------'+str(i))
	#source=getSource(url)
	#filePath="data/html-source-code/"+str(i)+".html"
	#file=open(filePath,"w")
	#file.write(source)
	#file.close()
	#print(str(i)+".html"+' is ok!')
