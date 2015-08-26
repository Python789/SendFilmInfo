# -*- coding: utf-8 -*-
__author__ = 'jeffrey_cui'
import smtplib
import time
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage
class myMailOperation:
    def __init__(self,h,u,p,postfix):
        self.mailHost=h
        self.user=u
        self.password=p
        self.postfix=postfix
        try:
            self.smtpServer = smtplib.SMTP()
            self.smtpServer.connect(h)
            self.smtpServer.login(self.user,self.password)
        except:
            print "smtp server init error"
    def close(self):
        self.smtpServer.quit()
        self.smtpServer.close()
    def sendFilm(self,sendFilmList,receiveUserMailList):
        self.sender="jeffrey"+"<"+self.user+"@"+self.postfix+">"
        self.msg = MIMEMultipart()
        self.msg['Subject'] = u"今日热门电影"
        self.msg['From'] = self.sender
        self.msg['To'] = ";".join(receiveUserMailList)
        self.filmInfoHtml=u''
        id=0
        for f in sendFilmList:
            id+=1
            self.filmInfoHtml+=self.generateFilmHtml(f,id).decode('utf-8')
            self.imgfile = "D:/MovieImage/"+f['filmName']+".jpg"
            try:
                self.image = MIMEImage(open(self.imgfile.decode('utf-8'),'rb').read())
                #ss='<image%d>'%id
                ss='<image'+chr(id+64)+'>'
                self.image.add_header('Content-ID',ss)
                self.msg.attach(self.image)
            except:
                print "mail image get failed"
        print self.filmInfoHtml
        self.txt = MIMEText(self.filmInfoHtml,'html','utf-8')
        self.msg.attach(self.txt)
        try:
            self.smtpServer.sendmail(self.msg['From'], self.msg['To'], self.msg.as_string())
            print "send success"
        except:
            print "send error"
    def generateFilmHtml(self,film,n):
        filmHtml='<div><h2>%d.</h2>'%(n)
        filmHtml+='<div id="filmImage%d">'%n
        #filmHtml+='<img src="cid:image%d">' %(n)
        filmHtml+='<img src="cid:image'+chr(64+n)+'">'
        filmHtml+='</div>'
        filmHtml+='<div id="filmInfo%d">'%n
        filmHtml+='<h3>电影名称:'+film['filmName']+'</h3>'
        filmHtml+='<p>电影类型:'+film['filmStyle']+'</p>'
        filmHtml+='<p>语言:'+film['filmLanguage']+'</p>'
        filmHtml+='<p>时长:'+film['filmTime']+'</p>'
        filmHtml+='<p>导演:'+film['filmDirector']+'</p>'
        filmHtml+='<p>演员:'+film['filmActor']+'</p>'
        filmHtml+='<p>关注度:'+film['filmFocus']+'</p>'
        filmHtml+='<p>购买量:'+film['filmBuy']+'</p>'
        filmHtml+='<p>评分:'+film['filmScore']+'</p></div></div>'
        return filmHtml

