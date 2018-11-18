import threading
import Queue
import urllib2
import time
import re
import gevent

from gevent import monkey;

monkey.patch_all()
monkey.patch_all()
emailqueue = Queue.Queue()
queue = Queue.Queue()  # 队列


def getdata(url):
    try:
        data = urllib2.urlopen(url).read().decode('utf-8')
        return data

    except:
        return "异常"


def getHtmlList():
    url_list = []
    for i in range(1, 47):
        url = 'https://bbs.tianya.cn/m/post-140-393974-{}.shtml'.format(str(i))
        print(url)
        url_list.append(url)
    return url_list


def getemail(data):
    try:
        mailregex = re.compile(
            r"([0-9a-zA-Z.%+\-]+@[0-9a-zA-Z.\-]+\.[A-Za-z]{1,3})",
            re.IGNORECASE)
        mylist = mailregex.findall(data)
        return mylist

    except:
        return []


# data=getdata(url)
# time.sleep(5)
# test='lingdianbing@sina.com'
# data=getdata(url)
# kk=getemail(data)
# print(kk)

email_list = []


def BFS(urllist):
    for url in urllist:
        queue.put(url)
        while not queue.empty():
            url = queue.get()  # 取出url
            pagedata = getdata(url)
            emaillist = getemail(pagedata)  # 抓取邮箱
            if len(emaillist) != 0:
                for email in emaillist:
                    print(email)
                    email_list.append(email)
                    for i in email_list:
                        emailqueue.put(i)


def saveEmail():
    global emailqueue
    mailfile = open("mail.txt", "wb")
    while True:
        time.sleep(3)
        while not emailqueue.empty():
            data = emailqueue.get()
            mailfile.write(data + "\r\n")
            mailfile.flush()
    mailfile.close()


gevent.joinall(
    [
        gevent.spawn(BFS, getHtmlList()),
        gevent.spawn(saveEmail),
    ]
)
