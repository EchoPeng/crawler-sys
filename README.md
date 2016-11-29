# crawler-sys
Web crawler and big data analysis system

#体系框架：
* python -> crawler 用python实现爬虫（非应用爬虫）
* crawler + docker -> crawler-node 将爬虫装入docker形成节点，并暴露一些端口口用于外部读写文件和与其他节点进行通讯
* crawler-node + hdfs/hive(hadoop/spark/yarn) -> resSet 将爬虫得到的结果集合大数据平台的一些技术手段形成分析前的数据库
* resSet + analysis -> action performance 数据分析后可以得到相类似的行为或者是类似的关键字结果集合，并依此形成推荐

