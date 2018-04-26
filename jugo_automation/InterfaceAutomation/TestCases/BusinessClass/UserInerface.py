from Method.Session import Session
from Method.MyTools import MyTools
from Method import MD5
def Test_login(username, passwd, url):
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
    res = Session1.visit_url(sessiondata=sess, url=url, method='post', params=para, headers=headers, bodytype='json')
    # print res
    return res


# Test_login('chenjinsong','11111111')
