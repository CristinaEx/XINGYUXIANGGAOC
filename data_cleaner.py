from data_reader import *
import numpy

def cleanData():
    """
    数据清洗
    """
    data = readData()
    for data_dict in data.values():
        if not type(data_dict) == dict:
            continue
        for key in data_dict.keys():
            data_dict[key] = data_dict[key].dropna()
    return data


if __name__ == '__main__':
    data = cleanData()
    print(data['2010-2014'])