from data import Record
import json
class FileReader:
    def __init__(self,path:str='') -> None:
        self.path=path
    def read_data(self)->list[Record]:
        pass
class TextFileReader(FileReader):
    def read_data(self)->list[Record]:
        record_list:list[Record]=[]
        with open(self.path,'r',encoding='UTF-8') as f:
            for line in f.readlines():
                line=line.strip()
                data_list=line.split(',')
                record=Record(data_list[0],data_list[1],int(data_list[2]),data_list[3])
                record_list.append(record)
        return record_list
class JsonFileReader(FileReader):
    def read_data(self)->list[Record]:
        record_list:list[Record]=[]
        with open(self.path,'r',encoding='UTF-8') as f:
            for line in f.readlines():
                data_dict=json.loads(line)
                data_list=[]
                for data_key in data_dict:
                    data_list.append(data_dict[data_key])
                record=Record(data_list[0],data_list[1],data_list[2],data_list[3])
                record_list.append(record)
        return record_list
if(__name__=="__main__"):
    textfilereader=TextFileReader("2011年1月销售数据.txt")
    jsonfilereader=JsonFileReader("2011年2月销售数据JSON.txt")
    list1=textfilereader.read_data()
    list2=jsonfilereader.read_data()
    for l in list1:
        print(l)
    for l in list2:
        print(l)
