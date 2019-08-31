#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/8/19 22:22
# @Author  : Aries
# @Site    : 
# @File    : mysqloper.py
# @Software: PyCharm
import MySQLdb


class MysqlConn():
    def __init__(self,mysqlconf):
        self.mysqlconf = mysqlconf


    def getConn(self):
        host = self.mysqlconf["host"]
        port = self.mysqlconf["port"]
        user = self.mysqlconf["user"]
        passwd = self.mysqlconf["passwd"]

        msg = "now test mysql for %s:%s\n" % (host, port)
        # self.textEdit_send.insertPlainText(info)
        try:
            conn = MySQLdb.connect(host=host, port=port, user=user, passwd=passwd,charset='utf8')

        except MySQLdb.Error as e:
            msg = e.args[1]+"\n"
            print(msg)
            # self.textEdit_msg.insertPlainText(e.args[1] + "\n")
        else:
            msg = "connect sucess mysql for %s:%s\n"%(host, port)
            print(msg)
            # self.textEdit_msg.insertPlainText(msg)
            return conn

class MysqlExec(MysqlConn):
    def __init__(self,mysqlconf):
        super(MysqlExec,self).__init__(mysqlconf)
        # self.ret = -1
        self.mysql_values = ""
        self.error_logs = []
        self._conn = self.getConn()

    # def getConn(self):
    #     self._conn = self.getConn()
    def sql_noresult(self,sqls):
        isexec = False  # 执行标志，执行成功则修改为Ture
        ##先判断self._conn，是否连接
        if not self._conn:
            return isexec
        cursor = self._conn.cursor()
        try:
            #self.conn()
            if type(sqls) == tuple:
                for sql in sqls:
                    try:
                        cursor.execute(sql)
                        isexec = True
                    except MySQLdb.Error as e:
                        try:
                            self.sqlError = "Error %d:%s" % (e.args[0], e.args[1])
                        except IndexError:
                            print("MySQL Error:%s" % str(e))
                        error = "%s Error:%s" % (sql,str(e))
                        self.error_logs.append(list(error))
            else:
                try:
                    cursor.execute(sqls)
                    isexec = True
                except MySQLdb.Error as e:
                    try:
                        self.sqlError = "Error %d:%s" % (e.args[0], e.args[1])
                    except IndexError as e:
                        print("MySQL Error:%s" % str(e))
                    error = "%s Error:%s" % (sqls, str(e))
                    self.error_logs.append(list(error))
            #self.connet.close()
        except  Exception:
            print("__sql_noresult,%s" % str(Exception))
        finally:
            cursor.close()
            return isexec


    def getTableValue(self,table):
        values = ""
        fields = ""
        cursor = self._conn.cursor()
        _sql = "SELECT /*!40001 SQL_NO_CACHE */ * FROM %s" % table
        if cursor:
            try:


                # 执行SQL语句
                cursor.execute(_sql)
                # 获取所有记录值
                values = cursor.fetchall()
                # 获取结果字段名描述
                fields = cursor.description
                #print self.fields_des

            except MySQLdb.Error as e:
                try:
                    self.sqlError = "Error %d:%s" % (e.args[0], e.args[1])
                except IndexError:
                    print("MySQL Error:%s" % str(e))
                print(self.sqlError)
            finally:
                cursor.close()
        return values,fields
