# -*- coding: UTF-8 -*-
# encoding=utf-8
__author__ = 'jasonchen'
from ConfigParser import ConfigParser
import os

class LoadConfig():

    def __init__(self):
        self._configpath = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir))
        pass

    def read_to_list(self):
        #./config/userlist.txt
        #os.chdir(os.path.dirname(os.getcwd()))

        abspath = os.path.join(self._configpath,'Config/userlist.txt')
        f = open(abspath, 'r')
        #f = open('./config/userlist.txt', 'r')
        result = list()
        for line in f:
            line = f.next().strip('\n')
            u = line.split(',')
            result.append(u)
        f.close()
        #print result[1][1][0:11]
        return result

    def read_config_to_mysql(self, name='jugotest'):
        mysql = {}
        config = ConfigParser()
        abspath = os.path.join(self._configpath, 'Config/mysql.conf')
        try:
            with open(abspath,'r') as cfgfile:
                config.readfp(cfgfile)
        except Exception as e:
            raise AssertionError('读取mysql配置文件失败'+str(e))
        #open and read
        mysql['host'] = config.get(name, 'host')
        mysql['user'] = config.get(name, 'user')
        mysql['passwd'] = config.get(name, 'passwd')
        mysql['db'] = config.get(name, 'db')
        return mysql


    def read_interface(self, name):

        config = ConfigParser()
        abspath = os.path.join(self._configpath,'Config/interface_para.conf')
        # open conf file
        try:
            with open(abspath,'r') as cfgfile:
                config.readfp(cfgfile)
        except Exception as e:
            raise AssertionError('读取interface_para配置文件失败'+str(e))
        # read data
        interfaceuil = config.get(name, 'uil')
        interfacepara = config.get(name, 'para')

        return interfaceuil, eval(interfacepara)

    def read_domain(self):
        config = ConfigParser()
        abspath = os.path.join(self._configpath, 'Config/domain.conf')
        # open conf file
        try:
            with open(abspath, 'r') as cfgfile:
                config.readfp(cfgfile)
        except Exception as e:
            raise AssertionError('读取domain配置文件失败' + str(e))

        return config.get('domain','domain')

# L = LoadConfig()
# a = L.read_interface('login')
# print a, a[0], a[1]
