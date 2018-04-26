# -*- coding: UTF-8 -*-
#encoding=utf-8
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
import os,random, re, json,string
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))

from LoadConfig import LoadConfig
from SelectFromMysql import SelectFromMysql
# from lib.common.MD5 import MD5
from LogPrint import Log

#eval 函数不支持null、true、false的转换，使用global false，
true = 1
false = 0

class Produce():

    def __init__(self):
        self._sqlobj  = SelectFromMysql()
        self._configobj = LoadConfig()

        pass
    def get_data_from_mysql(self, sql, value=None, db='y_hyip'):
        if ''.__eq__(value):
            value = None
        res = self._sqlobj.select_data_into_list(sql, value, db)
        if len(res) > 0:
            return res
        else:
            return None


    def opr_data_into_mysql(self, sql, value=None, db='4hyip'):
        if ''.__eq__(value):
            value = None
        res = self._sqlobj.insert_update_mysql(sql, value, db)
        return res

    def random_user(self):
        """从config/userlist.txt随机生成一个
        Example:
        | Random user |
        """
        user_list = self._configobj.read_to_list()
        user = user_list[random.randint(0, user_list.__len__()-1)][1]
        return user

    def random_userid(self):
        """从config/userlist.txt随机生成一个
        Example:
        | Random useruserandid |
        """
        user_list = self._configobj.read_to_list()
        ran = random.randint(0, user_list.__len__()-1)
        userid = user_list[ran][0]
        user = user_list[ran][1]
        return userid,user


    def generate_username(self):
        #res = str(random.randint(100, 199))+str(random.randint(1000, 9999))+str(random.randint(1000, 9999))
        head = random.sample(['130','131','132','133','134','135','136','137','138','139','147','150','151','152','153','155','156','157','158','159','170','180','181','182','183','184','185','186','187','188','189'], 1)
        res = str(head[0])\
              +str(random.randint(1000, 9999))\
              +str(random.randint(1000, 9999))

        if not self.if_qb_username_exsit(res):
            self.generate_username()
        else:
            return res

    def generate_email(self):
        domain=random.sample(['@qq.com','@163.com','@gmail.com'],1)
        res=self.generate_username()+str(domain[0])
        if not self.if_qb_username_exsit(res):
            self.generate_email()
        else:
            return str(res)
    def generate_name(self):
        name=string.join(random.sample(['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'], 3)).replace(" ","")
        res=name+'_'+str(random.randint(1000, 9999))
        if not self.if_qb_username_exsit(res):
            self.generate_name()
        else:
            return str(res)
    def generate_random(self):
        return random.random()

    def _if_qb_username_is_phonenumber(self, username):
        strphone = str(random.randint(100, 199))
        m = re.findall(r"^13|^18|^147|^15[^4]\w*", strphone)
        if 0 < len(m):
            return m[0]
        else:
            return None


    def if_qb_username_exsit(self, username):
        sql = """
        select id from qw_cas_user where username = '%s'
        """
        tmp = self._sqlobj.select_data_into_list(sql, username,'qw')
        if len(tmp) > 0:
            print ('username %s exsit in mysql!' % (username))
            return False
        else:
            return True


    def find_str(self, input_str, left_bond, right_bond):
        """通过左右边界匹配结果返回list，原则上足够精确的话，list只有1个元素；无或多个说明左右边界有问题
        Example:
        | Find str | 1234567890 | 2 | 7 |
        """

        regex = re.compile(left_bond + '(.*?)' + right_bond)
        reslist = regex.findall(str(input_str))
        return reslist

    def find_str_html(self, input_str, left_bond, right_bond):

        """通过左右边界匹配结果返回list，原则上足够精确的话，list只有1个元素；无或多个说明左右边界有问题
        Example:
        | Find str html| 1234567890 | 2 | 7 |
        """
        try:
            input_str = re.sub(r'[\r\n|\n|\t|\s]+', '',str(input_str))
            regex = re.compile(left_bond + '(.*?)' + right_bond)
            reslist = regex.findall(str(input_str))
            return reslist[0].encode("utf-8")
        except Exception as e:
            return e


    def result_should_be(self, input, expected):
        """Verifies that the input result is `expected`.
        Example:
        | Result Should Be | 3       |4
        """
        if type(input)!=type(expected):
            input=str(input)
            expected=str(expected)
        if input != expected:
            #print input,type(input),expected,type(expected)
            raise AssertionError('%s != %s' % (input, expected))
        

    def result_should_be_in (self,input,expectedList):
        """Verifies that the input result is in `expectedList`.
        Example:
        | Result Should Be In | (3,4)
        """
        result = False
        for items in expectedList:
            if type(input) != type(items):
                input = str(input)
                items = str(items)
            if input == items:
                result = True
                break
            else:
                result = false
        if result == False:
            raise AssertionError('%s not in  %s' % (input, expectedList))  
           
        
        
        
    def result_should_not_be(self, input, notexpected):
        """Verifies that the input result is not`notexpected`.
        Example:
        | Result Should Be | 3       |4
        """
        if input == notexpected:
            #print input,type(input),expected,type(expected)
            raise AssertionError('%s == %s' % (input, notexpected))


    def data_should_in_mysql(self, sql, value, dbname='qb'):
        """验证数据是否在mysql中存在
        Example:
        | Data should in mysql | select * from hyip_user where username=%s | 18020108465 |
        | Data should in mysql | select * from qw_cas_user where username=%s | 18020108465 | qw |
        """
        res = self._sqlobj.select_data_into_list(sql, value, dbname)
        if 0 == len(res):
            #print input,type(input),expected,type(expected)
            raise AssertionError('%s %s is not in mysql' % (sql, value))


    def data_should_not_in_mysql(self, sql, value, dbname='qb'):
        """验证数据是否在mysql中存在
        Example:
        | Data should not in mysql | select * from hyip_user where username=%s | 18020108465
        | Data should not in mysql | select * from qw_cas_user where username=%s | 18020108465 | qw |
        """
        res = self._sqlobj.select_data_into_list(self, sql, value, dbname)

        if 0 < len(res):
            #print input,type(input),expected,type(expected)
            raise AssertionError('%s||%s is in mysql' % (sql, value))



    def result_cmp(self, sqllist, responselist):
        """结果比较,responselist包含或者等于sqllist返回1，sqllist与responselist都为string
        Example:
        | Json Cmp | sqllist | responselist |
        """
        #全部转化为小写，且去除key中的下划线，由于两个结果集中的value预期相同，所以转换value中的下划线无影响
        try:
            sqllist = ''.join(sqllist.lower().split('_')).replace('null', "' '").replace('none',"' '")
            responselist = ''.join(responselist.lower().split('_')).replace('null',  "' '").replace('none',"' '")
            global true
            global false
        except Exception as e:
            raise AssertionError("can't lower or split"+str(e))
        #sqllist = sqllist.replace("'", "\"")
        #responselist = responselist.replace("'", "\"")

        try:
            #Log.info('sqllist:' + sqllist.replace('true',"1"))
            #Log.info('responselist len:' + responselist.replace('none',"' '"))
            #转化为list
            sqltemp = eval(sqllist)
            restemp = eval(responselist)
        except Exception as e:
            raise AssertionError("can't convert to list "+str(e))
            #raise AssertionError('Case task_do Failed,'+'doUserTask.html接口返回出错:')
        #templist = json.loads(sqllist)
        #responselist = json.loads(responselist)
        if(type(sqltemp) == list and type(restemp) == list):
            lengths = len(sqltemp)
            lengthr = len(restemp)
            #比较长度
            if(lengths != lengthr):
                Log.info('sqllist len:' + str(lengths) + 'responselist len:' + str(lengthr))
                return -1
            #长度为0为空，返回成功
            elif 0 == lengths:
                return 1

            #两个list对比，response包含sql结果
            for i in range(lengthr):
                for k,v in  sqltemp[i].items():
                    if str(sqltemp[i][k]) == str(restemp[i][k]):
                        pass
                    else:
                        Log.info(k + ':'+ str(sqltemp[i][k]) + ' not equal' + k + ':'+ str(restemp[i][k]))
                        return -1
            Log.info('List Compare Complete, Success...')
            return 1
        elif(type(sqltemp) == dict and type(restemp) == dict):
            '''
            精确匹配
            realdict = sorted(sqltemp.items(), key=lambda d: d[0])
            expectdict = sorted(restemp.items(), key=lambda d: d[0])
            if cmp(realdict,expectdict)!=0:
                Log.info('Not Equal')
                return -1
            return 1
            '''
            for k,v in  sqltemp.items():
                if str(sqltemp[k]) in ['',' ',None,"' '"] and str(restemp[k]) in ['',' ',None,"' '"]:
                    pass
                elif str(sqltemp[k]) == str(restemp[k]):
                    pass
                else:
                    raise AssertionError(k + ': '+ str(sqltemp[k]) + ' Not Equal ' + k + ': '+ str(restemp[k]))
                    #Log.info(k + ': '+ str(sqltemp[k]) + ' not equal' + k + ': '+ str(restemp[k]))
                    #return -1
            Log.info('Dict Compare Complete, Success...')
            return 1
        else:
            Log.info('Unknow Type')
            return -1


    def convert_postdata(self, postdata):
        '''
        仅适应fiddler的postdata参数
        '''
        if type(postdata) == str:
            #传入str类型，转换成json串
            postdata = "{'" + postdata +"'}"
            postdata = postdata.replace("=","':'").replace("&","','")
            params = postdata
            #params = json.loads(postdata)
        elif type(postdata) == unicode:
            #传入unicode类型，转换str后，同str处理
            postdata = str(postdata)
            postdata = "{'" + postdata +"'}"
            postdata = postdata.replace("=","':'").replace("&","','")
            params = postdata
            #params = json.loads(postdata)
        else:
            params = postdata
        return params




    def get_value(self, data, key):
        try:
            s = data.split(',')
            for ss in s:
                print ss
                item = ss.split(':')
                if key in item[0]:
                    #print item[1]
                    value = item[1].replace("'","").replace('"',"").replace("}","")
                    return value
        except:
            print None





