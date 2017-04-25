import threading,time
import multiprocessing
import random,time
import jdspider
import myparser,random
from multiprocessing import Pool
"""
class MyThread(threading.Thread):
	def __init__(self,threadname):
		threading.Thread.__init__(self,name=threadname)

	def run(self):
		for i in range(1,10):
			print("I am working!!"+str(i))
			start_url="https://list.jd.com/list.html?cat=9987,653,655"
			jdspider.getAmdSaveHtml(start_url)
			time.sleep(1)

mythread = MyThread('test')
print(mythread.getName())
#mythread.setDaemon(True)
mythread.start()
"""
"""
def run(jdDemo,i):
    jdDemo.saveHtml(int(i))
    print(i)
    time.sleep(0.5)
"""

def run(q):
    while True:
        try:
            #value = q.get()
            obj=q.get()
            jdDemo=obj[0]
            i=obj[1]
            myparserDemo=obj[2]
            #print(str(i))
            jdDemo.saveHtml(int(i))
            #print('Get %s from queue.' % value)
            folderPath="/data/html-source-code/"
            file_name=str(i)+'.html'
            myparserDemo.setFilePath(folderPath,file_name)
            myparserDemo.runDemo()
            time.sleep(random.random()*5)
            #time.sleep(random.random())
        finally:
            q.task_done()

def saveHtml():
    while True:
        try:
            pass
        finally:
            q.task_done()
    pass

def mulThreadRun(jdDemo):
    q = multiprocessing.JoinableQueue()
    pw1 = multiprocessing.Process(target=run, args=(q,))
    pw2 = multiprocessing.Process(target=run, args=(q,))
    # pw3 = multiprocessing.Process(target=run, args=(q,))
    # pw4 = multiprocessing.Process(target=run, args=(q,))
    # pw5 = multiprocessing.Process(target=run, args=(q,))
    # pw6 = multiprocessing.Process(target=run, args=(q,))
    # pw7 = multiprocessing.Process(target=run, args=(q,))
    # pw8 = multiprocessing.Process(target=run, args=(q,))
    # pw9 = multiprocessing.Process(target=run, args=(q,))
    # pw10 = multiprocessing.Process(target=run, args=(q,))
    # pw11 = multiprocessing.Process(target=run, args=(q,))
    # pw12 = multiprocessing.Process(target=run, args=(q,))
    # pw13 = multiprocessing.Process(target=run, args=(q,))
    # pw14 = multiprocessing.Process(target=run, args=(q,))
    # pw15 = multiprocessing.Process(target=run, args=(q,))
    # pw16 = multiprocessing.Process(target=run, args=(q,))
    pw1.daemon = True
    pw2.daemon = True
    # pw3.daemon = True
    # pw4.daemon = True
    # pw5.daemon = True
    # pw6.daemon = True
    # pw7.daemon = True
    # pw8.daemon = True
    # pw9.daemon = True
    # pw10.daemon = True
    # pw11.daemon = True
    # pw12.daemon = True
    # pw13.daemon = True
    # pw14.daemon = True
    # pw15.daemon = True
    # pw16.daemon = True
    pw1.start()
    pw2.start()
    # pw3.start()
    # pw4.start()
    # pw5.start()
    # pw6.start()
    # pw7.start()
    # pw8.start()
    # pw9.start()
    # pw10.start()
    # pw11.start()
    # pw12.start()
    # pw13.start()
    # pw14.start()
    # pw15.start()
    # pw16.start()
    PageNum=int(jdDemo.getPageNum())
    myparserDemo=myparser.myparser()
    for i in range(1,PageNum+1):
        q.put([jdDemo,i,myparserDemo])
    try:
        q.join()
    except KeyboardInterrupt:
        print("stopped by hand")
    pass

def downloadSource():
    start_url="https://list.jd.com/list.html?cat=9987,653,655"
    jdspiderDemo=jdspider.jdspider(start_url)
    print(jdspiderDemo.getPageNum())
    mulThreadRun(jdspiderDemo)
    print("collecting source is over!")
"""
    p=Pool()
    PageNum=int(jdspiderDemo.getPageNum())
    for i in range(PageNum+1):
        p.apply_async(run,args=(jdspiderDemo,i,))

    p.close()
    p.join()
"""
if __name__ == '__main__':
    downloadSource()
