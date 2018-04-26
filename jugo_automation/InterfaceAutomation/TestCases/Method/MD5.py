# -*- coding: UTF-8 -*-
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

__author__ = 'jasonchen'

import hashlib
import base64

class MD5():

    def __init__(self):
        pass
    @classmethod
    def MD5encodePassword(self, encoderstr,salt=''):
        return (hashlib.md5(encoderstr).hexdigest() if salt=='' else hashlib.md5(encoderstr+'{'+salt+'}').hexdigest())
    #其他加密类型
    def SHA1encodePassword(self, encoderstr,salt=''):
        return (hashlib.sha1(encoderstr).hexdigest() if salt=='' else hashlib.sha1(encoderstr+'{'+salt+'}').hexdigest())
    def SHA224encodePassword(self, encoderstr,salt=''):
        return (hashlib.sha224(encoderstr).hexdigest() if salt=='' else hashlib.sha224(encoderstr+'{'+salt+'}').hexdigest())
    def SHA256encodePassword(self, encoderstr,salt=''):
        return (hashlib.sha256(encoderstr).hexdigest() if salt=='' else hashlib.sha256(encoderstr+'{'+salt+'}').hexdigest())
    def SHA384encodePassword(self, encoderstr,salt=''):
        return (hashlib.sha384(encoderstr).hexdigest() if salt=='' else hashlib.sha384(encoderstr+'{'+salt+'}').hexdigest())
    def SHA512encodePassword(self, encoderstr,salt=''):
        return (hashlib.sha512(encoderstr).hexdigest() if salt=='' else hashlib.sha512(encoderstr+'{'+salt+'}').hexdigest())
    #b64编码
    def Base64encodePassword(self, encoderstr,salt=''):
        return (base64.b64encode(encoderstr) if salt=='' else base64.b64encode(encoderstr+'@qianbao'+u'\u0000'+encoderstr+u'\u0000'+salt))
    #b64解码
    def Base64decodePassword(self, decoderstr):
        return base64.b64decode(decoderstr)

