#*- coding: UTF-8 -*-
#encoding=utf-8
'''
Created on 2016年8月12日

__author__='jasonchen'
'''

import time,random,string,json

class MyTools():
    @classmethod
    def datetime_timestamp(self,date_format):
        #format='%Y/%m/%d %H:%M:%S'
        t2=time.strftime(date_format)#Convert a time tuple to a string according to a format specification.
        pt=time.strptime(t2, date_format)#Parse a string to a time tuple according to a format specification.
        st=time.mktime(pt)# Convert a time tuple in local time to seconds since the Epoch
        return int(st)

    @classmethod
    def random_name(self):
        s=random.sample('abcdejfghiklmnopqrstuvwxyz',4)
        i=random.randint(100,1000)
        result=string.join(s).replace(" ","")+str(i)
        #print(result)
        return result

    @classmethod
    def dict_to_json(self, dict1):
        if dict==type(dict1):
            dict2 = json.dumps(dict1)
            return dict2
        elif 'json'.__eq__(dict1):
            return dict1
        else:
            raise ValueError

