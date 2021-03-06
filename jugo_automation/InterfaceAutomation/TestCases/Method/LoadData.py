# -*- coding:utf-8 -*-
import os
import re

class LoadData():

    def __init__(self):
        self._configpath = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir))
        # print self._configpath
        pass

    def read_domain(self):
        abspath = os.path.join(self._configpath, 'Config/domain.txt')
        try:
            f = open(abspath, 'r')
            content = f.read()
            result = str()
            patt = r'domain=(.+)'
            patt = re.compile(patt)
            result = re.findall(patt, content)[0]
            f.close()
        except:
            raise IOError
        return result

    def read_interface_by_name(self, name):
        #dict_key:interface name dict_value:uil
        abspath = os.path.join(self._configpath,'Data/interface.txt')
        f = open(abspath, 'r')
        result = dict()
        for line in f:
            line = line.split('$')
            result[line[0]] = line[1]
        f.close()
        for key, value in result.items():
            if key == name:
                return value


if __name__ == '__main__':
    LoadData()