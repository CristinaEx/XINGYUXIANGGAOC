from data_reader import *
import re

class NflisData:
    """
    Nflis数据矩阵化
    """
    def __init__(self):
        # 这个保存了nflis中后三项数据(可以转化为矩阵)
        self.nflis_data = []
        # 这个保存了nflis_data中对应编号的message，与nflis_data一一对应
        self.nflis_data_message_book = []
        data = readData()
        # 首先处理NFLIS_Data
        NFLIS_Data = data['NFLIS_Data']
        # YYYY	State	COUNTY	FIPS_State	FIPS_County	FIPS_Combined	SubstanceName	DrugReports	TotalDrugReportsCounty	TotalDrugReportsState
        NFLIS_Data_keys = list(NFLIS_Data.keys())
        for index in range(len(NFLIS_Data)):
            message = dict()
            for message_index in range(7):
                message[NFLIS_Data_keys[message_index]] = NFLIS_Data[NFLIS_Data_keys[message_index]][index]
            self.nflis_data_message_book.append(message)
            dataList = []
            for message_index in range(7,10):
                dataList.append(NFLIS_Data[NFLIS_Data_keys[message_index]][index])
            self.nflis_data.append(dataList)

if __name__ == '__main__':
    nflis_data = NflisData()
    print(nflis_data.nflis_data_message_book[1])