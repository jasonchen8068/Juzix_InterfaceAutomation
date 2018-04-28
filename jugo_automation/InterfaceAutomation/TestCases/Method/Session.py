# -*- coding: UTF-8 -*-
# encoding=utf-8
import sys,os
reload(sys)
sys.setdefaultencoding('utf-8')

import requests, json
import mimetypes,mimetools
from bs4 import BeautifulSoup
from HTMLParser import HTMLParser
from Produce import Produce
from SelectFromMysql import SelectFromMysql
from LoadConfig import LoadConfig
from MD5 import MD5
from LogPrint import Log
import datetime
import HTMLParser
import cgi

class Session():
    def __init__(self):
        self._sqlobj  = SelectFromMysql()
        self._otherobj = Produce()
        self._configobj = LoadConfig()
        self._md5obj = MD5()
        self._HTTP_CODE =['200','201','301','302','400', '401','500','504','403','405','404', '502']
        self._SUCCESS_CODE = '1000'
        self._configpath = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir, os.pardir))
        pass
    def start_session(self):
        """声明一个session返回
        Example:
        | Start session |
        """
        session = requests.Session()
        return session

    def close_session(self, sessiondata):
        """关闭session一个session
        Example:
        | Start session |
        """
        if(None == sessiondata or ' ' == sessiondata or not isinstance(sessiondata, dict)):
            return
        try:
            session = sessiondata['session']
        except:
            session = sessiondata
        session.close()



    def visit_url(self, sessiondata, url, method, params, headers={},cookies={},ntimeout = 30,bodytype='dict'):
        """访问一个链接，第一个参数既可以是session，也可以是sessiondata：{'session':'', 'header':'', 'type':'' ,'body':''}
        Example:
        | Visit url | session | http://www.baidu.com/ | get | '' |
        | Visit url | session | http://passport.qianbao666.com/cas/qianbaoLogin | post | {'username': username,'password': password,'lt': '123','_eventId': 'submit','s_uuid': '345'} |
        返回值:
        """
        #初始化部分返回数据
        #headers类型判断转换
        if type(headers) == str:
                #传入str类型，转换成json串
            headers = headers.replace('\'', '"')
            headers = json.loads(headers)
        elif type(headers) == unicode:
                #传入unicode类型，转换str后，同str处理
            headers = str(headers)
            headers = headers.replace('\'', '"')
            headers = json.loads(headers)

        elif type(headers) == dict:
                #传入dict类型，不用转换，直接可用
            None
        else:
                #非以上两种类型，抛错
            raise TypeError('%s is not a DICT or STR, its a %s' % (headers, type(headers)))
        res_dict = {}
        #处理传入值
        url = str(url)
        method = str(method)
        #设定重试次数=1
        #requests.adapters.DEFAULT_RETRIES = 1
        if sessiondata is None:
            session = self.start_session()
        else:
            try:
                session = sessiondata['session']
            except:
                session = sessiondata

        #判定传入调用方式，获取结果
        if 'get'.lower().__eq__(method.lower()):
            resp = session.get(url, verify=False, headers=headers,timeout = int(ntimeout))
        elif 'post'.lower().__eq__(method.lower()):
            if type(params) == str:
                #传入str类型，转换成json串
                Log.info("d1")
                params = params.replace('\'', '"')
                params = json.loads(params)
            elif type(params) == unicode:
                Log.info("d2")
                #传入unicode类型，转换str后，同str处理
                params = str(params)
                params = params.replace('\'', '"')
                params = json.loads(params)
                #params =unicode(params,"utf-8")
            elif type(params) == dict and 'json'.__eq__(bodytype):
                Log.info("d4")
                params = json.dumps(params)
            elif type(params) == dict:
                Log.info("d3")
                None
            elif type(params) == list:
                Log.info("d5")
                params = json.dumps(params)
            else:
                #非以上两种类型，抛错
                raise TypeError('%s is not a DICT or STR, its a %s' % (params, type(params)))
            #params =unicode(params,"utf-8")
            resp = session.post(url, data=params, verify=False, headers=headers,timeout = int(ntimeout))
        res_dict = self._make_res(session, resp)
        return res_dict

    def _make_res(self, session, resp):
        #初始化部分返回数据
        res_dict = {}
        resheadstr = resp.headers
        resheadstr['rescode'] = resp.status_code
        
        
        if str(resheadstr['rescode']) not in self._HTTP_CODE:
            raise AssertionError('Http Request Failed,Code Status: '+str(resheadstr['rescode']))

        try:
            encodetype = str(resheadstr['content-type'].split('=')[1]).lower()

            if 'utf-8'.__eq__(encodetype):
                resbodystr = resp.content.decode('utf-8')
            elif 'gbk'.__eq__(encodetype):
                resbodystr = resp.content.decode('gbk')
            else:
                resbodystr = resp.content
        except Exception as e:
            resbodystr = resp.content
        try:
            if 'application/json'.__eq__(resheadstr['Content-Type'].split(';')[0]):
                restype = 'json'
            elif 'text/xml'.__eq__(resheadstr['Content-Type'].split(';')[0]):
                restype = 'xml'
            elif 'text/html'.__eq__(resheadstr['Content-Type'].split(';')[0]):
                restype = 'html'
            elif 'image/jpeg'.__eq__(resheadstr['Content-Type'].split(';')[0]) or 'image/png'.__eq__(resheadstr['Content-Type'].split(';')[0]):
                restype = 'image'
            elif 'application/x-shockwave-flash'.__eq__(resheadstr['Content-Type'].split(';')[0]):
                restype = 'flash'
            else:
                restype = 'text'
        except Exception as e:
            restype = None
        #按照返回结果格式，分别转成json/beautifulsoap格式
        print resbodystr
        print restype
        if not '' == resbodystr:
            if restype in ('html', 'xml'):
                resbodystr = BeautifulSoup(''.join(resbodystr))
            elif 'json' == restype:
                try:
                    resbodystr = json.loads(resbodystr)
                except Exception,e:
                    print '[Error]%s' %(e)
                #resbodystr = json.dumps(resbodystr, ensure_ascii=False)

        #构造返回字典，包含session, resphead, resptype, respvalue
        res_dict['cookie'] = tuple(resp.cookies)
        res_dict['session'] = session
        res_dict['header'] = resheadstr
        res_dict['type'] = restype
        res_dict['body'] = resbodystr
        return res_dict

    def _get_lable_value(self, sessiondata, lbtype, lbname, resclass):
        tmpstr = sessiondata['body']
        reslist = tmpstr.find_all(lbtype, attrs={'name': lbname})
        if 1 != len(reslist):
            return reslist
        return reslist[0][resclass]

    def _encode_multipart_formdata(self, fields, files=[]):

        BOUNDARY = mimetools.choose_boundary()
        print BOUNDARY
        CRLF = '\r\n'
        L = []
        for (key, value) in fields.items():

            L.append('--' + BOUNDARY)
            L.append('Content-Disposition: form-data; name="%s"' % key)
            L.append('')
            L.append(value)
        for (key, filepath) in files:
            L.append('--' + BOUNDARY)
            L.append('Content-Disposition: form-data; name="%s"; filename="%s"' % (key, os.path.basename(filepath)))
            L.append('Content-Type: application/octet-stream')
            L.append('')
            L.append(open(filepath, 'rb').read())
        L.append('--' + BOUNDARY + '--')
        L.append('')
        body = CRLF.join(L)
        content_type = 'multipart/form-data; boundary=%s' % BOUNDARY
        return BOUNDARY, body

    def get_yesterday(self,i=0):
        '''
        i为减少的天数
        '''
        now_time = datetime.datetime.now()
        if i==0:
            now_time_nyr = now_time.strftime('%Y-%m-%d')
            return now_time_nyr
        else:
            i=int(i)
            yes_time = now_time + datetime.timedelta(days=-i)
            yes_time_nyr = yes_time.strftime('%Y-%m-%d')
            return yes_time_nyr

    def str_convert(self,str_txt,var1,var2=None,var3=None):
        if ''.__eq__(var2):
            str_txt=str(str_txt)
            var1=str(var1)
            str_finished=str_txt%(var1)
        elif ''.__eq__(var3):
            str_txt=str(str_txt)
            var1=str(var1)
            var2=str(var2)
            str_finished=str_txt%(var1,var2)
        else:
            str_txt=str(str_txt)
            var1=str(var1)
            var2=str(var2)
            var3=str(var3)
            str_finished=str_txt%(var1,var2,var3)
        return str_finished

    def upload_imgs_request(self, sessiondata, url,params,name, file_path='./lib/images/test.jpg'):
        """
        """
        res_dict = {}
        #处理传入值
        url = str(url)
        try:
            session = sessiondata['session']
        except:
            session = sessiondata

        file_type = mimetypes.guess_type(file_path)[0]

        if 'image/pjpeg' == file_type:
            file_type = 'image/jpeg'
        elif 'image/x-png' == file_type:
            file_type = 'image/png'

        fa = open(file_path, 'rb')
        filestream = fa.read()

        params = params.replace('\'', '"')
        params = json.loads(params)

        resp = session.post(url, data=params,
                            files={name:(file_path, filestream)}
                           )

        fa.close()
        Log.info(resp)
        res_dict = self._sessobj._make_res(session, resp)
        return res_dict


    def html_unescape(self,params):
        if type(params) != str:
            params = str(params)
        hp = HTMLParser.HTMLParser()
        html_unescape = hp.unescape(params)
        return html_unescape

    def add_message (self, sessiondata, url,params, file_path='../../lib/images/test.jpg'):
        print os.getcwd()
        res_dict = {}
        #处理传入值
        url = str(url)
        try:
            session = sessiondata['session']
        except:
            session = sessiondata

        file_type = mimetypes.guess_type(file_path)[0]

        if 'image/pjpeg' == file_type:
            file_type = 'image/jpeg'
        elif 'image/x-png' == file_type:
            file_type = 'image/png'

        fa = open(file_path, 'rb')
        filestream = fa.read()

        params = params.replace('\'', '"')
        params = json.loads(params)

        resp = session.get('http://message.ba.qbao.com/message/toListMessage.html')
        resp = session.post(url, data=params,
                            files={'portionMembers-file':(file_path, filestream)}
                           )

        fa.close()
        Log.info(resp)
        res_dict = self._make_res(session, resp)
        return res_dict


    def visit_url_xml(self,sessiondata, url, params,headers={'Content-Type': 'application/xml'}):
        """
        发送xml请求
        """
        if sessiondata is None:
            session = self.start_session()
        else:
            try:
                session = sessiondata['session']
            except:
                session = sessiondata

        print type(params)
        url = str(url)
        params = str(params)
        print type(params)

        #params =unicode(params,"utf-8")
        resp = session.post(url, data=params, headers=headers)

        res_dict = {}
        res_dict = self._make_res(session, resp)
        print res_dict['body']
        return res_dict