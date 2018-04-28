#*- coding: UTF-8 -*-
#encoding=utf-8
import sys,os
reload(sys)
sys.setdefaultencoding('utf-8')

__author__ = 'jasonchen'

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


    def merchant_register(self, sessiondata, url, username, file_path='./images/test.jpg'):
        """商家注册，第一个参数既可以是session，也可以是sessiondata：{'session':'', 'header':'', 'type':'' ,'body':''}
        注意：post的参数和file比较复杂，暂时在此方法里写死
        Example:
        | Merchant register | session | http://www.qianwang365.com/uc/registerBusiness.html | 18020108465 |
        返回值:
        同self.visit_url
        """
        #初始化部分返回数据
        res_dict = {}
        #处理传入值
        url = str(url)
        try:
            session = sessiondata['session']
        except:
            session = sessiondata

        file_type = mimetypes.guess_type(file_path)[0]
        file_name = file_path.split('/')[-1]
        #不同平台会把jpeg认做pjpeg，png认做x-png，转换一下
        if 'image/pjpeg' == file_type:
            file_type = 'image/jpeg'
        elif 'image/x-png' == file_type:
            file_type = 'image/png'

        fa = open(file_path, 'rb')
        filestream = fa.read()

        resp = session.post(url, data={'from': 'qianwang',
                                       'status': '',
                                       'businessInfo.id': '',
                                       'businessInfo.username': username,
                                       'phoneCode': '',
                                       'businessInfo.shopName': username,
                                       'businessInfo.storeFrontName': username,
                                       'businessInfo.webSite': '',
                                       'businessInfo.shopIntroduction': '',
                                       'businessInfo.provinceId': '',
                                       'businessInfo.cityId': '',
                                       'businessInfo.areaId': '',
                                       'businessInfo.address': '',
                                       'cityIdByPoint': '',
                                       'businessInfo.bdPointX': '',
                                       'businessInfo.bdPointY': '',
                                       'businessInfo.phone': '',
                                       'accepted': 'on'
                                       }, files={'identityCardImage': (file_name, filestream, file_type),
                                                 'bsLicenseImage': (file_name, filestream, file_type),
                                                 'taxImage': (file_name, filestream, file_type),
                                                 'orgImage': (file_name, filestream, file_type)
                                                 }
                            )
        fa.close()
        res_dict = self._make_res(session, resp)
        return res_dict


    def upload_user_photo(self, sessiondata, url):
        """qb用户上传头像，第一个参数既可以是session，也可以是sessiondata：{'session':'', 'header':'', 'type':'' ,'body':''}
        Example:
        | Upload user photo | session | http://user.qianbao666.com/usercenter/uploadAvataNew.html |
        返回值:
        同self.visit_url
        """
        #初始化部分返回数据
        res_dict = {}
        #处理传入值
        url = str(url)
        session = sessiondata['session']
        filepath='./lib/images/test.jpg'
        abspath = os.path.join(self._configpath,filepath)
        fileparams = {"Filedata": (filepath.split("/")[-1], open(abspath, "rb"), "application/octet-stream")}
        resp = session.post(url, data={}, files=fileparams, verify=False)
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

    def get_logindata(self,url):
        carloginurl = self._configobj.read_interface( './lib/config/','car_interface', 'carLoginurl')
        pmloginurl = self._configobj.read_interface( './lib/config/','car_interface', 'paimaiLoginurl')

        session = self.start_session()
        tmplist = url.split('?')
        url_login_pre = url
        #安全中心登录处理
        resp = session.get(url_login_pre,allow_redirects=False)

        tmp = str(resp.headers['Set-Cookie'])
        jsessionid = self._otherobj.find_str(tmp, 'JSESSIONID=', '; Path=/')[0]

        if 302 == resp.status_code:
            url = resp.headers['Location']
            resp = self.visit_url(session, url, 'get', '')

        try:
            respstr = resp.content
        except:
            respstr = resp['body']

        try:
            try:
                lt_data = self._otherobj.find_str(respstr, 'name="lt" value="', '" />')[0]
                uuid_data = self._otherobj.find_str(respstr, 'name="s_uuid" value="', '" />')[0]
            except:
                lt_data = self._otherobj.find_str(respstr, 'name="lt" type="hidden" value="', '"/>')[0]
                uuid_data = self._otherobj.find_str(respstr, 'name="s_uuid" type="hidden" value="', '"/>')[0]
        except:
            lt_data = self._otherobj.find_str(respstr, 'name="lt" value="', '" />')[0]
            uuid_data = ''
        url_login = tmplist[0] + ';jsessionid=' + jsessionid + '?' + tmplist[1]
        return lt_data,uuid_data,url_login

    def user_login(self, url, username, password, ltype = 1):
        """登录
        Example:
        type: 1. 正常登录
              2. 使用绑定信息登录
        | User login | http://passport.qianbao666.com/cas/qianbaoLogin?service=http%3A%2F%2Fwww.qianbao666.com%2Fj_spring_cas_security_check | admin | 111111 | type |
        """

        carloginurl = self._configobj.read_interface( './lib/config/','car_interface', 'carLoginurl')
        pmloginurl = self._configobj.read_interface( './lib/config/','car_interface', 'paimaiLoginurl')

        session = self.start_session()
        tmplist = url.split('?')
        url_login_pre = url
        #安全中心登录处理
        resp = session.get(url_login_pre,allow_redirects=False)

        tmp = str(resp.headers['Set-Cookie'])
        jsessionid = self._otherobj.find_str(tmp, 'JSESSIONID=', '; Path=/')[0]

        if 302 == resp.status_code:
            url = resp.headers['Location']
            resp = self.visit_url(session, url, 'get', '')

        try:
            respstr = resp.content
        except:
            respstr = resp['body']

        try:
            try:
                lt_data = self._otherobj.find_str(respstr, 'name="lt" value="', '" />')[0]
                uuid_data = self._otherobj.find_str(respstr, 'name="s_uuid" value="', '" />')[0]
            except:
                lt_data = self._otherobj.find_str(respstr, 'name="lt" type="hidden" value="', '"/>')[0]
                uuid_data = self._otherobj.find_str(respstr, 'name="s_uuid" type="hidden" value="', '"/>')[0]
        except:
            lt_data = self._otherobj.find_str(respstr, 'name="lt" value="', '" />')[0]
            uuid_data = ''
        postdata = {'username': username,
                    'password': password,
                    'lt': lt_data,
                    '_eventId': 'submit',
                    's_uuid': uuid_data}
        url_login = tmplist[0] + ';jsessionid=' + jsessionid + '?' + tmplist[1]
        domainurl = tmplist[1].split('%3A%2F%2F')[1].split('%2F')[0]

        if type(resp) == requests.models.Response:
            resp = self.visit_url(session, url_login, 'post', postdata)
        else:
            resp = self.visit_url(resp, url_login, 'post', postdata)

        #安全中心特殊逻辑
        if 'user.qianbao666.com' == domainurl:
            tourl = '/usercenter/ucIndex.html'
        else:
            tourl = '/index.html'

        resp = self.visit_url(resp, 'http://' + domainurl + tourl, 'get', '')

        #只有钱宝后台、安全中心改造过了
        if 'backoffice.qianbao666.com' == domainurl:
            resusername = self._otherobj.find_str(str(resp['body']), '<img alt="" class="mr10" height="40" src="/images/userpicnone65.gif" width="40"/>', '\r\n')
        elif 'user.qianbao666.com' == domainurl:
            #resusername = self._otherobj.find_str(str(resp['body']), 'var pageUsername = \'', '\';')
            #resusername = self._otherobj.find_str(str(resp['body']), 'var username = ', '\');')
            if -1 != str(resp['body'].find(str(username))):
                resusername = username
            else:
                resusername = None

        else:
            #Log.info(str(resp['body']))
            if str(resp['body']).__contains__("用户您好，由于您长时间没有登录，为了保障您的账户资金安全，需要对您的账号进行重新校验，请完成签到拼图来完成校验"):
                Log.info('用户 ：' + username + ' 为沉默用户')
                return resp
            else:
                #resusername = self._otherobj.find_str(str(resp['body']), 'var username = \'', '\'')
                if -1 != str(resp['body'].find(str(username))):
                    resusername = username
                else:
                    resusername = None

        try:
            #resp = self.visit_url(resp, carloginurl, 'get', '')
            resp1 = session.get(carloginurl,allow_redirects=False)
            #print 'hehehe'
            #print resp1
            if 302 == resp1.status_code:
                url = resp1.headers['Location']
                #print 'url ' + url
                resp1 = self.visit_url(session, url, 'get', '')
        except Exception as e:
            Log.info('cas 同步 car 失败'+str(e))

        try:
            #resp = self.visit_url(resp, pmloginurl, 'get', '')
            resp1 = session.get(pmloginurl,allow_redirects=False)
            #print 'xixixi'
            #print resp1
            if 302 == resp1.status_code:
                url = resp1.headers['Location']
                #print 'url ' + url
                resp1 = self.visit_url(session, url, 'get', '')
        except Exception as e:
            Log.info('cas 同步 paimai 失败'+str(e))

        if(ltype == 1):
            #if resusername is not None and len(resusername) > 0 and HTMLParser().unescape(resusername[0]) == username:
            if resusername is not None and len(resusername) > 0:
                return resp
            else:
                return None
        else:
            if resusername is not None and len(resusername) > 0:
                return resp
            else:
                return None


    def register(self, usertype):
        '''
        用户注册
        input:url：注册url
        type:
        1:手机号码
        2:邮箱
        3:用户名
        Example:
        | Task Receive | url  |
        '''
        #判断账号类型
        usertype=int(usertype)

        if usertype==1:
            username = self._otherobj.generate_username()
        elif usertype==2:
            username= self._otherobj.generate_email()
        else:
            username= self._otherobj.generate_name()
        #处理传入值
        session = self.start_session()
        #toRegisturl = 'http://user.qianbao666.com/usercenter/regist/toRegist.html'
        #doRegisturl = 'http://user.qianbao666.com/usercenter/regist/doRegist.html'
        toRegisturl = self._configobj.read_interface( './lib/config/','qb_interface', 'toRegisturl')
        doRegisturl = self._configobj.read_interface( './lib/config/','qb_interface', 'doRegisturl')

        try:
            resp = self.visit_url(session, toRegisturl, 'get', '')
        except Exception as e:
           raise AssertionError('打开注册页面出错'+str(e))
        post_data={'username':username, 'password':'111111', 'rePassword':'111111','securityCode':'111111','presenterCode':'','from':''}
        try:
            resp = self.visit_url(resp, doRegisturl, 'post', post_data)
        except Exception as e:
           raise AssertionError('注册出错'+str(e))
        #关闭session
        self.close_session(resp)
        if str(resp['body']['success']).__eq__('True'):
            #设置为非ascii解析
            bodystr = json.dumps(resp['body'], ensure_ascii=False)
            sql = "SELECT id from hyip_user where username = '%s'"%username
            userid = self._sqlobj.select_data_into_list(sql)

            try:
                user_id = userid[0]['id']
                return username,user_id
            except Exception as e:
                raise AssertionError('获取用户id出错'+str(e))
        else:
            self.close_session(resp)
            return None

    def bind_trade_password(self,session):
        #交易密码验证码请求
        bind_url='http://user.qbao.com/usercenter/setBindedUserTradePwd.html'
        post_data="{'verifyCode':'111111'}"
        #交易密码设置请求
        bind_tradingpwd_url='http://user.qbao.com/usercenter/bindedUserSetPwd.html'
        tradingpwd_post_data="{'newPwd':'222222'," \
                             "'confirmNewPwd':'222222'}"

        try:
            verificationcode_response=self.visit_url(session,bind_url,'post',post_data)
        except Exception as e:
            raise AssertionError('设置交易密码验证码出错:'+str(e))

        try:
            bind_tradingpwd_response=self.visit_url(session,bind_tradingpwd_url,'post',tradingpwd_post_data)
        except Exception as e:
            raise AssertionError('设置交易密码出错:'+str(e))

        if str(bind_tradingpwd_response['header']['rescode']).__eq__("200"):
            print bind_tradingpwd_response['header']['rescode']
            return True
        else:
             raise AssertionError('请求返回code错误:%s'% bind_tradingpwd_response['header']['rescode'])

    def add_shop_photo(self, sessiondata, url,file):
        """qb用户上传头像，第一个参数既可以是session，也可以是sessiondata：{'session':'', 'header':'', 'type':'' ,'body':''}
        Example:
        | Upload user photo | session | http://user.qianbao666.com/usercenter/uploadAvataNew.html |
        返回值:
        同visit_url
        """
        #初始化部分返回数据
        res_dict = {}
        #处理传入值
        url = str(url)
        session = sessiondata['session']
        filepath=file
        fileparams = {"file": (filepath.split("/")[-1], open(filepath, "rb"), "application/octet-stream")}
        resp = session.post(url, data={}, files=fileparams, verify=False)
        res_dict = self._make_res(session, resp)
        return res_dict



    def login_app(self, url, username, password):
        '''
        登录app
        Example:
        | User login | http://passport.qianbao666.com/api/v10/cas/tickets | admin | 111111 |
         '''

        session = self.start_session()
        url_login_pre = url
        _serviceurl = self._configobj.read_interface( './lib/config/','api_interface', 'Serviceurl')
        _url_app = self._configobj.read_interface( './lib/config/','api_interface', 'AppLoginurl')

        #verifyCode无需验证
        verifyCode = self._md5obj.MD5encodePassword(username, '3edc4rfv')
        password = self._md5obj.MD5encodePassword(password, username)

        postdata = {'verifyCode': verifyCode,'password': password,'username': username,'account': username}
        #app登录处理
        resp = self.visit_url(session, url_login_pre, 'post', postdata)
        res_dict = resp['body']

        if(str(res_dict['responseCode']).__ne__(self._SUCCESS_CODE)):
            raise AssertionError('Http response responseCode Status: '+ str(res_dict['responseCode']))

        try:
            url_login_after = url + '/' + str(res_dict['data'])
            postdata = {'service':_serviceurl}
            resp = self.visit_url(resp, url_login_after, 'post', postdata)
        except Exception as e:
            raise AssertionError(url_login_after +  ' Http Request Failed,Code Status: '+str(e))

        if(str(resp['body']['responseCode']).__ne__(self._SUCCESS_CODE)):
            raise AssertionError('Http response responseCode Status: '+ str(res_dict['responseCode']))

        try:
            postdata = {'st':resp['body']['data']}
            resp = self.visit_url(resp, _url_app, 'post', postdata)
        except Exception as e:
            raise AssertionError(url_login_after +  ' Http Request Failed,Code Status: '+str(e))

        if(str(resp['body']['responseCode']).__ne__(self._SUCCESS_CODE) or str(resp['body']['errorMsg']).__ne__('')):
            Log.info('App login failed,Http response : ' + str(resp['body']))
        return resp

    def register_app(self, usertype):
        '''
        app用户注册,只有两种注册方式
        input:url：注册url
        type:
        2:手机号码
        3:用户名
        Example:
        | Task Receive | url  |
        '''
        #判断账号类型
        usertype=int(usertype)
        headers = {'version': '2.3.0','iOSversion': 'iPhone 5 (GSM+CDMA)','channel': 'App Store','devType': 'iPhone','devId': 'f28a47d48cf75ad1addbebd695906169b4a3fa4d',
                   'Content-Type': 'application/x-www-form-urlencoded','User-Agent': 'QianbaoIOS/2.3.0','sourceType': 'client'}
        if usertype==3:
            username= self._otherobj.generate_name()
        else:
            usertype = 2
            username= self._otherobj.generate_username()
        #处理传入值
        session = self.start_session()
        doRegisturl = self._configobj.read_interface( './lib/config/','api_interface', 'doRegisturl')
        #密码需md5加密，默认密码111111
        password = self._md5obj.MD5encodePassword('111111', username)
        #post_data={'username':username, 'password':'111111', 'rePassword':'111111','securityCode':'111111','presenterCode':''}

        post_data={'securityCode':111111,'password':password,'username':username,'verifyCode':'111111','recommendCode':28048,'nameType':usertype}
        try:
            resp = self.visit_url(session, doRegisturl, 'post', post_data,headers=headers)
        except Exception as e:
           raise AssertionError('注册出错'+str(e))

        #关闭session
        self.close_session(resp)

        if (str(resp['body']['responseCode']).__eq__(self._SUCCESS_CODE) and str(resp['body']['errorMsg']).__eq__('注册成功')):
            #设置为非ascii解析
            bodystr = json.dumps(resp['body'], ensure_ascii=False)
            sql = "SELECT id from hyip_user where username = '%s'"%username
            userid = self._sqlobj.select_data_into_list(sql)
            try:
                user_id = userid[0]['id']
                return username,user_id
            except Exception as e:
                raise AssertionError('获取用户id出错'+str(e))
        else:
            self.close_session(resp)
            return None


    def _encode_multipart_formdata(self,fields, files=[]):

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