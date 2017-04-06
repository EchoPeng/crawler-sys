import urllib
import urllib
import re
import os,time,sys

class jdspider(object):
	"""docstring for jdspider"""
	start_url=""
	lastPageNum=""
	def __init__(self, url):
		super(jdspider, self).__init__()
		self.start_url=url
		self.lastPageNum=self.getlastPageNum(url)
		reload(sys) 
		sys.setdefaultencoding('utf8')

	def getPageNum(self):
		return self.lastPageNum

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

	def getplist(partten,source):

		pass

	def getproductInfo(partten,plist):
		pass

	def saveImgAndpName(product):
		pass

	def getlastPageNum(self,start_url):
		partten_lastPageNumContent='<span class="p-num">(.*?)<a class="pn-next"'
		partten_lastPageNum='class="">(.*?)</a>'
		source_html=self.getSource(start_url)
		lastPageNumContent=re.compile(partten_lastPageNumContent,re.S).findall(source_html)
		lastPageNumContent=lastPageNumContent[0]
		lastPageNum=re.compile(partten_lastPageNum,re.S).findall(lastPageNumContent)
		lastPageNum=lastPageNum[0]
		return lastPageNum

	def saveHtml(self,i):
		url=self.start_url+'&page='+str(i)
		source=self.getSource(url)
		fileFolder="/data/html-source-code/"
		filePath=fileFolder+str(i)+".html"
		if os.path.isdir(fileFolder):
			file=open(filePath,"wb")
			file.write(source)
			file.close()
		else:
			os.mkdir(fileFolder)
			file=open(filePath,"wb")
			file.write(source)
			file.close()
		if len(source) > 3:
			print(str(i)+".html"+' is ok!')
		else:
			print(str(i)+".html"+' is error!')
		pass

	def getAndSaveHtml(self):
		lastPageNum=self.getlastPageNum(self.start_url)
		print(lastPageNum)
		#for i in range (1,2):
		for i in range (1,int(lastPageNum)+1):
			self.saveHtml(i)


#start_url="https://list.jd.com/list.html?cat=9987,653,655"
#jdspiderObj=jdspider(start_url)
#jdspiderObj.getAndSaveHtml()

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
