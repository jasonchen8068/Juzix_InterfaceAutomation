# -*- coding: UTF-8 -*-
#encoding=utf-8

from ConfigParser import ConfigParser
import re,os
# from robot.api import logger

#import os
#os.chdir("..")
#path = os.getcwd()
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

    def read_config_to_mysql(self, path, name='qb'):
        mysql = {}
        config = ConfigParser()
        abspath = os.path.join(self._configpath,path+'SQLconfig.cfg')
        try:
            with open(abspath,'r') as cfgfile:
                config.readfp(cfgfile)
        except Exception as e:
            raise AssertionError('读取mysql配置文件失败'+str(e))
        #open and read
        if name =='root':
            mysql['host'] = config.get('root_MySql','host')
            mysql['user'] = config.get('root_MySql','user')
            mysql['passwd'] = config.get('root_MySql','passwd')
            mysql['db'] = config.get('root_MySql','db')
            mysql['charset'] = config.get('root_MySql','charset')
        elif name =='qb':
            mysql['host'] = config.get('qb_MySql','host')
            mysql['user'] = config.get('qb_MySql','user')
            mysql['passwd'] = config.get('qb_MySql','passwd')
            mysql['db'] = config.get('qb_MySql','db')
            mysql['charset'] = config.get('qb_MySql','charset')
        elif name =='qw':
            mysql['host'] = config.get('qw_MySql','host')
            mysql['user'] = config.get('qw_MySql','user')
            mysql['passwd'] = config.get('qw_MySql','passwd')
            mysql['db'] = config.get('qw_MySql','db')
            mysql['charset'] = config.get('qw_MySql','charset')

        return mysql


    def read_interface(self, path, name, value):
        interface = ''
        config = ConfigParser()
        abspath = os.path.join(self._configpath,path+'qbinterface.cfg')
        try:
            with open(abspath,'r') as cfgfile:
                config.readfp(cfgfile)
        except Exception as e:
            raise AssertionError('读取mysql配置文件失败'+str(e))
        #open and read
        if name =='qb_interface':
            interface = config.get('qb_interface',value)
        elif name =='api_interface':
            interface = config.get('api_interface',value)
        elif name =='car_interface':
            interface = config.get('car_interface',value)
        else:
            pass
        return interface

