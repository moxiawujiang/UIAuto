#coding:utf-8
import json

class OperaJson:
    def __init__(self,name):
        try:
            self.file_path="../data_config/"+name+'.json'
            with open(self.file_path,'rb')  as f:
                self.data=json.load(f)
        except FileNotFoundError:
            raise

    #获取json数据
    def get_json_data(self,key):
        try:
            # print(self.data[key])
            # print(type(self.data[key]))
            return self.data[key]
        except KeyError:
            print("获取json数据出错")
            raise

    #更新json数据
    def create_json_data(self,key,value):
        try:
            self.data[key]=value
            with open(self.file_path,'w') as f:
                json.dump(self.data,f)
        except KeyError:
            print("保存json数据出错")
            raise


if __name__ == '__main__':
    OperaJson("dbname").get_json_data('test')
