from excel_reader import *
import os

data_path = "2019_MCMProblemC_DATA\\2018_MCMProblemC_DATA\\"

def readData():
    """
    读取所有excel数据
    """
    data = dict()
    data['NFLIS_Data'] = readExceldFile('2019_MCMProblemC_DATA\\2018_MCMProblemC_DATA\\MCM_TEST.xlsx',header = 0)
    for year in range(2010,2017):
        filename = 'ACS_' + str(year-2000)+ '_5YR_DP02'
        data[str(year-4)+'-'+str(year)] = readCsvFile(data_path + filename + '\\' + filename  + '_with_ann.csv')
    return data

if __name__ == '__main__':
    data = readData()
    print(data['2010-2014'])