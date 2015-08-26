# -*- coding: utf-8 -*- 
# __author__ = 'jeffrey_cui'
'''create table filmlist 
(
    id int(3) auto_increment not null primary key,
    filmname varchar(50) not null,
    filmstyle varchar(50),
    filmlanguage varchar(50),
    filmtime varchar(50),
    filmdirector varchar(50),
    filmactor varchar(100),
    filmyear date,
    filmfocus int(10),
    filmbuy int(10),
    filmscore float,
    filmimagepath varchar(200),
    filmimageurl varchar(200)
);'''
import MySQLdb
import time
class MySQLFilmOperation:
    def __init__(self,h,u,p,dbase):
        try:
            self.con=MySQLdb.connect(host=h,user=u,passwd=p,db=dbase,charset="utf8")
            self.cursor=self.con.cursor()
        except:
            print "mysql init failed"
    def insertMovie(self,movieInfo):
        ISOTIMEFORMAT='%Y-%m-%d %X'
        insertTime=time.strftime(ISOTIMEFORMAT,time.localtime(time.time()))
        insertSql='insert into filmlist values(null,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'
        try:
            n = self.cursor.execute(insertSql,[movieInfo['filmName'],movieInfo['filmStyle'],movieInfo['filmLanguage'],movieInfo['filmTime'],
                                    movieInfo['filmDirector'],movieInfo['filmActor'],insertTime,movieInfo['filmFocus'],movieInfo['filmBuy'],movieInfo['filmScore'],movieInfo['filmImage'],movieInfo['filmImageUrl']])
            self.con.commit()
            print "insert",movieInfo['filmName'],"successfully"
        except:
            print "insert error"
    def checkMovieExist(self,movieInfo):#return 0:表示电影不在数据库中，other:数据库中存在该电影
        checkSql="select * from filmlist where filmname=%s"
        try:
            n = self.cursor.execute(checkSql,movieInfo['filmName'])
            if len(self.cursor.fetchall())==0:#不存在
                return 0
            else:
                return 1
        except:
            print "check error"
    def close(self):
        self.cursor.close()
        self.con.close()
