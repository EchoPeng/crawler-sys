#coding=gbk
import re
class product(object):
	"""docstring for product"""
	productId = ""#phone id not contains 'J_'
	pName=""#phone name
	pImg=""#phone img url
	pPrice=""#phone open current price
	commentCount=""#perhaps commentCount
	commentCountStr=""#perhaps commentCount str add+
	pShop=""#saler
	averageScore=""#
	generalCount=""#perhaps generalCount
	generalRate=""#
	goodCount=""#perhaps goodCount
	goodRate=""#
	poorCount=""#perhaps poorCount
	poorRate=""#

	result=None #goodRate*averageScore*commentCount/price

	# 'ShowCount', 'ShowCountStr' ,
	# 'GoodRateShow', 'GoodRateStyle', 'GoodRate', 'GoodCount', 'GoodCountStr' ,
	# 'AfterCountStr', 'AfterCount',
	# 'GeneralRateShow', 'GeneralRate', 'GeneralCount', 'GeneralRateStyle' ,'GeneralCountStr'
	# 'AverageScore',
	# 'PoorRateStyle', 'PoorRate', 'PoorCountStr', 'PoorRateShow','PoorCount',
	# 'ProductId', 'SkuId',
	# 'CommentCount', 'CommentCountStr',
	def __init__(self):
		super(product, self).__init__()

	def __repr__(self):
		return repr((self.productId,self.pName.decode("string_escape"),self.pImg,self.pPrice,self.commentCount,self.commentCountStr,self.pShop.decode("string_escape"),self.averageScore,self.generalCount, self.generalRate, self.goodCount, self.goodRate, self.poorCount,self.poorRate , self.result))