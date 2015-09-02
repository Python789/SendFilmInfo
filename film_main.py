# -*- coding: utf-8 -*-
# __author__ = 'jeffrey_cui'
import urllib
import urllib2
import cookielib
import re
import json
import mySQLConnect
import time
import myMail
def findGeWaLaHotFilmInfo():#找出格瓦拉热门电影信息
    path='http://www.gewara.com/ajax/loadIndexKeyNumber.xhtml'
    values = {'keys':'ticketMovieCount,hotMovieCount,futureMovieCount,ticketCinemaCount,movieActivityCount,movieDetail_238815707@198430333@256218653@231341601@240180404@258874317@238959708@228158257@197928777@240254551'}
    data = urllib.urlencode(values)
    req = urllib2.Request(path, data)
    response = urllib2.urlopen(req)
    infoList = response.read()
    infoListJson=json.loads(infoList[11:])
    #print infoListJson['hotMovieCount']
    response.close()
    return infoListJson
def findHotFilmContent(n):#找出格瓦拉热门电影目录，包括电影名称，类型，语言，时长，导演，主演
    filmContents=[]
    path='http://www.gewara.com/movie/searchMovie.xhtml'
    checkNum=0
    filmNum=0
    filmContentHtmlObj=urllib.urlopen(path)
    filmContentHtml=filmContentHtmlObj.read()
    filmContentReg='<div class="ui_pic">[\s\S]*?</div>[\s]*?<div class="ui_text">[\s]*?<div class="title">[\s\S]*?</div>[\s\S]*?</div>'
    filmContentsHtml=re.findall(filmContentReg,filmContentHtml)
    checkNum=checkNum+len(filmContentsHtml)
    filmContentHtmlObj.close()
    if checkNum<n:
        for i in range(10):
            pageNum=i+1
            url=path+'?pageNo='
            url="%s%d"%(url,pageNum)
            filmContentHtmlObj=urllib.urlopen(url)
            filmContentHtml=filmContentHtmlObj.read()
            pageFilmContentsHtml=re.findall(filmContentReg,filmContentHtml)
            checkNum=checkNum+len(pageFilmContentsHtml)
            filmContentHtmlObj.close()
            for p in pageFilmContentsHtml:
                filmContentsHtml.append(p)
            if checkNum>(n-2):
                break
    for c in filmContentsHtml:
        filmNum=filmNum+1
        filmContent={}
        #checkNum=checkNum+1
        filmNameReg='<a href="/movie/\d*?" title="(.*?)" target="_blank" class="color3">.*?</a>'
        filmStyleReg='<p>类型：\s*?(.*?)</p>'
        filmLanguageReg='<p>语言：\s*?(.*?)</p>'
        filmTimeReg='<p>片长：\s*?(.*?)</p>'
        filmDirectorReg='<p>导演：\s*?(.*?)</p>'
        filmActorReg='<p>主演：\s*?(.*?)</p>'
        filmFocusReg='<span class="ml5">\(<span data-keynum=".*?">(\d*?)</span>人关注'
        filmBuyReg='<span data-keynum=".*?">(\d*?)</span>人购票\)</span>'
        filmScore1Reg='<sub style="margin:0;" data-keynum=".*?">(\d)</sub>'
        filmScore2Reg='<sup data-keynum=".*?">(.{2})</sup>'
        filmImageUrlReg='<img src="(.*?)"\s*?alt=".*?"\s*?height="\d*?"\s*?width="\d*?"/>'
        filmCinemaInfoReg='<p>(\d*?家影院上映\d*?场)</p>'

        filmName=re.findall(filmNameReg,c)
        filmStyle=re.findall(filmStyleReg,c)
        filmLanguage=re.findall(filmLanguageReg,c)
        filmTime=re.findall(filmTimeReg,c)
        filmDirector=re.findall(filmDirectorReg,c)
        filmActor=re.findall(filmActorReg,c)
        filmFocus=re.findall(filmFocusReg,c)
        filmBuy=re.findall(filmBuyReg,c)
        filmScore1=re.findall(filmScore1Reg,c)
        filmScore2=re.findall(filmScore2Reg,c)
        filmImageUrl=re.findall(filmImageUrlReg,c)
        filmCinemaInfo=re.findall(filmCinemaInfoReg,c)
        ################2015-9-2添加，获取其他的一些电影信息信息 filmMoreInfoUrl，filmCinemaInfo，filmReleaseDate
        filmMoreInfoUrlRe='<a href="(/movie/\d*?)" title=".*?" target="_blank" class="color3">.*?</a>'
        filmMoreInfoUrl='http://www.gewara.com'+re.findall(filmMoreInfoUrlRe,c)[0]
        filmReleaseDate=''
        try:#获取上映日期
            filmMoreInfoObj=urllib.urlopen(filmMoreInfoUrl)
            filmMoreInfo=filmMoreInfoObj.read()
            filmReleaseDateReg='<li class="first">上映时间：(.*?)</li>'
            filmReleaseDate=re.findall(filmReleaseDateReg,filmMoreInfo)
            filmMoreInfoObj.close()
        except:
            print 'get more film info error'
        filmContent['filmMoreInfoUrl']=filmMoreInfoUrl
        if len(filmCinemaInfo)==1:
            filmContent['filmCinemaInfo']=filmCinemaInfo[0]
        else:
            filmContent['filmCinemaInfo']=''
        if len(filmReleaseDate)==1:
            filmContent['filmReleaseDate']=filmReleaseDate[0]
        else:
            filmContent['filmReleaseDate']=''

        #########################################
        if len(filmName)==1:
            filmContent['filmName']=filmName[0]
            if len(filmStyle)==1:
                filmContent['filmStyle']=filmStyle[0]
            else:
                filmContent['filmStyle']=''
            if len(filmLanguage)==1:
                filmContent['filmLanguage']=filmLanguage[0]
            else:
                filmContent['filmLanguage']=''
            if len(filmTime)==1:
                filmContent['filmTime']=filmTime[0]
            else:
                filmContent['filmTime']=''
            if len(filmDirector)==1:
                filmContent['filmDirector']=filmDirector[0]
            else:
                filmContent['filmDirector']=''
            if len(filmActor)==1:
                filmContent['filmActor']=filmActor[0]
            else:
                filmContent['filmActor']=''
            if len(filmFocus)==1:
                filmContent['filmFocus']=filmFocus[0]
            else:
                filmContent['filmFocus']=''
            if len(filmBuy)==1:
                filmContent['filmBuy']=filmBuy[0]
            else:
                filmContent['filmBuy']=''
            if len(filmScore1)==1 and len(filmScore2)==1:
                filmScore=filmScore1[0]+filmScore2[0]
                filmContent['filmScore']=filmScore
            else:
                filmContent['filmScore']=''
            if len(filmImageUrl)==1:
                filmContent['filmImageUrl']=filmImageUrl[0]
            else:
                filmContent['filmImageUrl']=''
            filmContents.append(filmContent)
            print filmNum
            print filmContent['filmName']
            print filmContent['filmStyle']
            print filmContent['filmLanguage']
            print filmContent['filmTime']
            print filmContent['filmDirector']
            print filmContent['filmActor']
            print filmContent['filmFocus']
            print filmContent['filmBuy']
            print filmContent['filmScore']
            print filmContent['filmImageUrl']
            print filmContent['filmMoreInfoUrl']
            print filmContent['filmCinemaInfo']
            print filmContent['filmReleaseDate']
            print '---'
        else:
            print filmName[0],filmNum,'find film info error'
    return filmContents
def getGeWaLaFilmContent():#获取格瓦拉上最近热门电影的数目和信息概要
    hotFilmInfo=findGeWaLaHotFilmInfo()
    filmNum=hotFilmInfo['hotMovieCount']#获取今日热门电影的数目
    print filmNum
    filmContents=findHotFilmContent(filmNum)#获取热门电影内容概要
    return filmContents
def getZhongYingFilmContent(contentUrl):#获得南京南站中影的影片信息，只有影片名称
    url_obj=urllib.urlopen(contentUrl)
    result=url_obj.read()
    contents=json.loads(result)
    return contents
#向数据库中写入电影的数据，如果电影名称存在，则不写入
#return:数据库中不存在的电影，即今天新出现的电影，用于发邮件提醒我
def writeFilmData(filmData,imagePath):
    i=0;
    newFilmList=[]
    myDB=mySQLConnect.MySQLFilmOperation("192.168.1.123","root","cuijie.,1234","myfilm")
    for movie in filmData:
        exist=myDB.checkMovieExist(movie)
        if exist==0:
            i+=1;
            print "try to insert",i,"records"
            filmImagePath=imagePath+movie['filmName']+'.jpg'
            try:#将url指向的图片保存到本地
                urllib.urlretrieve(movie['filmImageUrl'],filmImagePath.decode('utf-8'))
                movie['filmImage']=filmImagePath.decode('utf-8')
            except:
                print "get image error"
                movie['filmImage']='no image'
            myDB.insertMovie(movie)
            newFilmList.append(movie)
            print "-------"
        else:
            print movie['filmName'],"was existed"
            #newFilmList.append(movie)#test
    myDB.close()
    return newFilmList
def changeDataFormat(flimListInfo):
    flimList=[]
    for f in flimListInfo:
        film={}
        film['filmName']=f[1].encode("utf-8")
        film['filmStyle']=f[2].encode("utf-8")
        film['filmLanguage']=f[3].encode("utf-8")
        film['filmTime']=f[4].encode("utf-8")
        film['filmDirector']=f[5].encode("utf-8")
        film['filmActor']=f[6].encode("utf-8")
        film['filmFocus']='%d'%f[8]
        film['filmBuy']='%d'%f[9]
        film['filmScore']='%f'%f[10]
        film['filmReleaseDate']=f[13].strftime('%Y-%m-%d')
        film['filmMoreInfoUrl']=f[14].encode("utf-8")
        film['filmCinemaInfo']=f[15].encode("utf-8")
        flimList.append(film)
    return flimList
def SendDataBaseFilm():
    myDB=mySQLConnect.MySQLFilmOperation("192.168.1.123","root","cuijie.,1234","myfilm")
    flimListInfo=myDB.getFilm()
    flimList=changeDataFormat(flimListInfo)
    if len(flimListInfo)!=0:
        myMailObj=myMail.myMailOperation("smtp.163.com","cuijie52410856","19910824cj","163.com")
        myMailObj.sendFilm(flimList,['446306514@qq.com'])
        myMailObj.close()
    myDB.close()
if __name__ == "__main__":
    saveImagePath="D:/MovieImage/"
    film=getGeWaLaFilmContent()
    todayNewFilm=writeFilmData(film,saveImagePath)
    print "there is",len(todayNewFilm),"new moive in GeWaLa"
    for new in todayNewFilm:
        print "there is a new movie in GeWaLa:",new['filmName']
    if len(todayNewFilm)>0:
        myMailObj=myMail.myMailOperation("smtp.163.com","cuijie52410856","19910824cj","163.com")
        myMailObj.sendFilm(todayNewFilm,['446306514@qq.com'])
        myMailObj.close()
    #SendDataBaseFilm()