from Method.Session import Session
from Method.MyTools import MyTools
from Method import MD5
class Login(object):
    def __init__(self, url, username, passwd):
        self._url = url
        self._username = username
        self._passwd = passwd
        self._res = self.Test_login(self._username, self._passwd)

    def Test_login(self, username, passwd):
        # 1-cookies
        # 2-headers
        headers = {'Content-Type': 'application/json;charset=UTF-8', 'Connection': 'keep-alive',
                   'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.117 Safari/537.36'}
        # 3-session
        Session1 = Session()
        sess = Session1.start_session()
        # 4-send request
        # get captchacode
        # url1 = 'http://192.168.112.178/Kaptcha.jpg?1'
        # res = Session1.visit_url(sessiondata=sess, url=url1, method='get', params={})
        # print res
        passwd = MD5.MD5().MD5encodePassword(passwd)
        para = {
            "loginName": username,
            "password": passwd,
            "rememberMe": False,
            "captchaCode": "9xhc",
            "os": "win10"
        }
        res = Session1.visit_url(sessiondata=sess, url=self._url, method='post', params=para, headers=headers, bodytype='json')
        # print res
        return res

    # assert method
    def Test_login_success(self):
        res = self._res
        return True

    def Test_login_false(self):
        res = self._res
        return True


