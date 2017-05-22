# my_spider
# version 0.0.1

FROM ubuntu

MAINTAINER "yuancheng" <yc929158066@163.com>

#添加更新源
ADD sources.list /etc/apt/

# update
RUN apt-get update

# install Chinese support
RUN apt-get install -y language-pack-zh-hant language-pack-zh-hans
ENV LANG "zh_CN.UTF-8"

#install aptitude
RUN apt-get install -y aptitude

#install python-pip
#RUN aptitude install -y python-setuptools python-dev build-essential

#install basic tools
RUN apt-get install -y -f wget vim python

# install pip
RUN wget https://bootstrap.pypa.io/get-pip.py;python get-pip.py;rm -f get-#pip.py

#RUN easy_install pip3
RUN pip install --upgrade lxml requests



# install my_spider requirements
#RUN pip install wheel Scrapy pymongo requests celery -i http://#pypi.douban.com/simple --trusted-host pypi.douban.com

EXPOSE 27017 15672

ENV container docker

# for celery worker run as root user
ENV C_FORCE_ROOT true

#Set user
USER root

#Add start-spider.sh to /
ADD start-spider.sh /
RUN chmod +x start-spider.sh

VOLUME [ "/sys/fs/cgroup" ]

CMD ["sh", "start-spider.sh"]

