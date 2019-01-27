from data_reader import *
import numpy

YEAR_NUM = 7 # 年份数量
ATTR_NUM = 596 # 属性数量 596 / 4 -> 有用的属性数量
ITEM_NUM = 464 # 项目数量

class OurData:
    """
    除Nflis数据矩阵化
    """
    def __init__(self):
        # ITEM_INDEX | YEAR_INDEX | DATA
        self.data = [[[0]*ATTR_NUM]*YEAR_NUM]*ITEM_NUM
        # ID对应的ITEM_INDEX的message，即前三项数据
        self.data_message_book = dict()
        # [DATA中各个数据所对应的的index,含义]
        self.data_index_book = dict()
        self.county_index_book = dict()
        data = readData()    
        data_keys = list(data.keys())[1:8]   
        item_keys = list(data[data_keys[0]].columns)  
        # 首先读取data_index_book
        for i in range(3,len(item_keys)):
            if not i % 4 == 3:
                continue
            self.data_index_book[item_keys[i]] = [int(i/4),data['2006-2010'][item_keys[i]][0]]
        # 获取data
        # 规则缺失值或非法值填0，+ = 1,- = -1
        for year_index in range(YEAR_NUM):
            for i in range(1,len(data[data_keys[year_index]])):
                values = data[data_keys[year_index]].loc[i].values
                item_index = values[0]
                if not item_index in self.data_message_book.keys():
                    self.data_message_book[item_index] = {'index':len(self.data_message_book.keys()),'GEO.id2':values[1],'GEO.display-label':values[2]}
                    self.county_index_book[values[2].split(' ')[0].upper()] = len(self.county_index_book.keys())
                values = values[3:ATTR_NUM+3]
                useful_values = []
                for j in range(ATTR_NUM):
                    if not j % 4 == 0:
                        continue
                    try:
                        values[j] = float(values[j])
                    except:
                        if values[j] == '(X)':
                            values[j] = 0
                        elif values[j] == '*****':
                            values[j] = 0
                        elif values[j] == '**':
                            values[j] = 0
                        elif values[j] == '-':
                            values[j] = -1
                        elif values[j] == '+':
                            values[j] = 1
                        else:
                            print(values[j])
                            exit(0)
                    else:
                        values[j] = float(values[j])
                    useful_values.append(values[j])
                self.data[self.data_message_book[item_index]['index']][year_index] = useful_values
                

if __name__ == '__main__':
    our_data = OurData()
    # print(numpy.array(our_data.data).shape)
    # print(our_data.data[0][6])
    # print(our_data.data_message_book)
    print(our_data.county_index_book)
    print(our_data.county_index_book['WOLFE'])