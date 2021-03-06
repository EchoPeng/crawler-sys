import redis
import json
class Database:
    def __init__(self):
        # self.host = 'localhost'
        # self.host = '172.18.102.209'
        self.host = '192.168.42.1'
        self.port = 6379

    def write(self,website,city,year,month,day,deal_number):
        try:
            key = '_'.join([website,city,str(year),str(month),str(day)])
            val = deal_number
            r = redis.StrictRedis(host=self.host,port=self.port)
            r.set(key,val)
        except Exception, exception:
            print exception

    def read(self,website,city,year,month,day):
        try:
            key = '_'.join([website,city,str(year),str(month),str(day)])
            r = redis.StrictRedis(host=self.host,port=self.port)
            value = r.get(key)
            print value
            return value
        except Exception, exception:
            print exception

    def add_productInfo(self,pInfo):
        try:
            name = "pInfo"
            resultname = "result:"+str(pInfo.result)+":productId:"+pInfo.productId
            resultpopname="resultpop:"+str(pInfo.resultpop)+":productId:"+pInfo.productId
            productId=pInfo.productId
            key = productId
            val = json.dumps(pInfo, default=lambda o: o.__dict__, sort_keys=True, indent=4,ensure_ascii=False)
            val = json.loads(val)
            r = redis.StrictRedis(host=self.host,port=self.port)
            r.zadd("result-range",pInfo.result,resultname)
            r.zadd("resultpop-range",pInfo.resultpop,resultpopname)
            r.hmset(key,val)
        except Exception, exception:
            print exception

    def add_brandlist(self,brandlist,brandnamelist):
        try:
            key = "brandlist"
            r = redis.StrictRedis(host=self.host,port=self.port)
            brandlist = json.dumps(brandlist, sort_keys=True, indent=0, ensure_ascii=False)
            r.set(key,brandlist)
            brandnamelist = json.dumps(brandnamelist, sort_keys=True, indent=0, ensure_ascii=False)
            r.set("brandnamelist",brandnamelist)
        except Exception, exception:
            print exception

    def get_brandlist(self):
        try:
            key = "brandlist"
            r = redis.StrictRedis(host=self.host,port=self.port)
            brandlist = r.get(key)
            brandnamelist = r.get("brandnamelist")
            print(brandlist)
            print(brandnamelist)
        except Exception, exception:
            print exception

    def get_productInfo(self,pInfo):
        try:
            key = pInfo.productId
            r = redis.StrictRedis(host=self.host,port=self.port)
            value = r.get(key)
            print value
            return value
        except Exception, exception:
            print exception

    def add_productResult(self,pInfo):
        try:
            key = 'J_'+pInfo.productId
            val = pInfo.result
            # val = json.dumps(pInfo.__dict__)
            # print "val : "+val
            r = redis.StrictRedis(host=self.host,port=self.port)
            r.set(key,val)
        except Exception, exception:
            print exception

    def get_productResult(self,pInfo):
        try:
            key = key = 'J_'+pInfo.productId
            r = redis.StrictRedis(host=self.host,port=self.port)
            value = r.get(key)
            print value
            return value
        except Exception, exception:
            print exception
# if __name__ == '__main__':
#     db = Database()
#     db.write('meituan','beijing',2013,9,1,8000)
#     db.read('meituan','beijing',2013,9,1)
