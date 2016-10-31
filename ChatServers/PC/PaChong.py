import urllib.request
import urllib.parse
import pymysql
from html.parser import HTMLParser
from sqlalchemy import *
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from PC.PCModels import Pachongimage
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from django.core import serializers
import json
import pickle
from PC.SqlAlchemyToJson import AlchemyEncoder

class ConnectMysql(object):

    Base = declarative_base()

    def connectSql(self):

        engine = create_engine('mysql+pymysql://root@localhost:3306/roguedatabase',
                               connect_args = {'charset': 'utf8'},
                               echo = True)
        Session = sessionmaker(bind=engine)
        session = Session()
        return session


    def insertSql(self, imageList=None):

        print('------传参数后显示的数组:' + str(len(imageList)))
        if imageList is None:
            print('-------现在显示的是 imageList 为 None')
            imageList = ''

        print('--------- imageList (' + str(imageList[0]) + ')')
        session = self.connectSql()
        session.add_all(imageList)
        session.commit()
        session.close()


    def querySql(self):

        session = self.connectSql()
        query = session.query(Pachongimage).all()
        session.close()
        return query



class HtmlParser(HTMLParser):

    def error(self, message):
        pass

    def __init__(self):
        HTMLParser.__init__(self)
        self.links = []

    def handle_starttag(self, tag, attrs):
        if tag == 'img':
            s = []
            for (variable, value) in attrs:
                s.append(value)

            self.links.append(s)

    def handle_endtag(self, tag):
        pass

    def handle_data(self, data):
        pass


def geturl(url_parameter):

    req = urllib.request.urlopen(url_parameter)
    req = req.read()
    return req.decode('utf-8')


def continsrc(src):

    currentIndex = 0
    return_str = ''
    all_str = src
    start_parameter = "<li class=\"m-b-hot\">"
    end_parameter = "</li>"

    j = 0

    while all_str.find("<li class=\"m-b-hot\">"):

        inta = all_str.find(start_parameter)
        if inta == -1:
            break

        inta += currentIndex
        all_str = src[inta:]
        intb = all_str.find(end_parameter)
        finally_str = src[inta:inta + intb + len(end_parameter)]
        print(finally_str)
        return_str = return_str + finally_str
        currentIndex = inta + intb + len(end_parameter)
        all_str = src[currentIndex:]
        j += 1

    return return_str


def pageinurl(url_parameter):

    urllists = []
    src = geturl(url_parameter)
    content = continsrc(src)
    parser = HtmlParser()
    parser.feed(content)
    parser.close()
    for i in parser.links:
        image = Pachongimage()
        urlString = '/Users/rogueandy/Desktop/ceshi/' + i[1] + '.jpg'
        urllib.request.urlretrieve(i[0], urlString)
        image.imgaddress = urlString
        image.imgtitle = i[0]
        image.imgfromurl = url_parameter
        urllists.append(image)

    return urllists

def convert_to_builtin_type(obj):
    print('default(', repr(obj), ')')
    d = {}
    d.update(obj.__dict__)
    return d


@csrf_exempt
def showPaChongToIOS(request):

    connect = ConnectMysql()
    current = connect.querySql()

    return HttpResponse(json.dumps({'status': '1', 'imgurls': current}, cls=AlchemyEncoder),
                        content_type='application/json')