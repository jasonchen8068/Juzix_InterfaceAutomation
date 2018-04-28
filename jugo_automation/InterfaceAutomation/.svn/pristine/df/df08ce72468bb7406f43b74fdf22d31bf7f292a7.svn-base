# -*- coding: UTF-8 -*-
#encoding=utf-8

import MySQLdb,datetime
from LoadConfig import LoadConfig


class SelectFromMysql():

    def __init__(self):
        self._config =  LoadConfig()
        pass
    def select_data_into_list(self, sql, value=None, dbname='4hyip'):
        '''
        取mysql数据list
        @sql，传入sql字符串
        @value，绑定变量值
        函数流程说明：1、读取数据库配置ReadConfigToMysql
                   2、连接数据库
                   3、执行sql+value语句
                   4、每一行生成一个dict{}
                   5、所有行拼接list[]
                   6、return list[]
        '''

        mysql = self._config.read_config_to_mysql('./lib/config/', dbname)

        conn = MySQLdb.connect(
            host = mysql.get('host'),
            port = 3306,
            user = mysql.get('user'),
            passwd = mysql.get('passwd'),
            db = mysql.get('db'),
            charset = mysql.get('charset')
        )
        cr = conn.cursor()
        if not value is None:
            sql = sql % value
        try:
            cr.execute(sql)
        except Exception as e:
            pass
        #cr.execute(sql, value)
        rows = cr.fetchall()
        if rows is None:
            return None
        desc = cr.description
        tmp = {}
        res = []
        for row in rows:
            j = 0
            for i in desc:
                tmp[i[0]] = str(row[j]) if isinstance(row[j], datetime.datetime) else str(row[j])
                j = j+1
            res.append(tmp.copy())
        cr.close()
        conn.close()
        return res


    def insert_update_mysql(self, sql, value=None, dbname='4hyip'):
        '''
        取mysql数据list
        @sql，传入sql字符串
        @value，绑定变量值
        函数流程说明：1、读取数据库配置ReadConfigToMysql
                   2、连接数据库
                   3、执行sql+value语句
                   4、每一行生成一个dict{}
                   5、所有行拼接list[]
                   6、return list[]
        '''
        mysql = self._config.read_config_to_mysql('./lib/config/', dbname)

        print mysql.get('host')
        conn = MySQLdb.connect(
            host = mysql.get('host'),
            port = 3306,
            user = mysql.get('user'),
            passwd = mysql.get('passwd'),
            db = mysql.get('db'),
            #charset = "utf8"
            charset = mysql.get('charset')
        )
        cr = conn.cursor()
        if not value is None:
            sql = sql % value
        try:
            cr.execute(sql)
            conn.commit()
            res = True
        except:
            conn.rollback()
            res = False
        cr.close()
        conn.close()
        return res