
#coding:utf-8
import pymysql
from common.operate_json import OperaJson


class OperateMysql:
    def __init__(self,dbname="test"):
        #读取数据库信息
        _dbinfo=OperaJson("dbinfo").get_json_data(dbname)
        _host=_dbinfo["host"]
        _username=_dbinfo["username"]
        _password=_dbinfo["password"]
        #打开数据库连接
        self._db = pymysql.connect(_host, _username, _password)
        # 使用 cursor() 方法创建一个游标对象 cursor
        self.cursor = self._db.cursor()

    def get_all_or_one_db_data(self,sql,type="all"):
        # 使用 execute()  方法执行 SQL 查询
        self.cursor.execute(sql)
        if type=="all":
            # 使用 fetchall方法获取全部数据.
            _data = self.cursor.fetchall()
        else:
            _data=self.cursor.fetchone()
        # 关闭数据库连接
        self._db.close()
        return _data

    def  updata_or_delete_db_data(self,sql):
        try:
            # 执行SQL语句
            self.cursor.execute(sql)
            # 提交修改
            self._db.commit()
        except:
            # 发生错误时回滚
            self._db.rollback()



