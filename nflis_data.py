from data_reader import *
import re

class NflisData:
    """
    Nflis数据矩阵化
    """
    def __init__(self):
        # 这个保存了nflis中后三项数据(可以转化为矩阵)
        # YEAR | STATE | COUNTY -> DATA
        # DATA : DrugReports	TotalDrugReportsCounty	TotalDrugReportsState
        self.data = []
        # 对应表
        self.year_index_book = dict()
        self.state_index_book = dict()
        self.county_index_book = dict()
        self.combine_message_book = dict()
        data = readData()
        # 首先处理NFLIS_Data
        NFLIS_Data = data['NFLIS_Data']
        # YYYY	State	COUNTY	FIPS_State	FIPS_County	FIPS_Combined	SubstanceName	DrugReports	TotalDrugReportsCounty	TotalDrugReportsState
        for item_index in range(len(NFLIS_Data)):
            now_data = NFLIS_Data.loc[item_index]
            if not now_data[0] in self.year_index_book.keys():
                self.year_index_book[now_data[0]] = len(self.year_index_book.keys())
                self.state_index_book[now_data[0]] = dict()
                self.county_index_book[now_data[0]] = dict()
                self.data.append([])
            if not now_data[3] in self.state_index_book[now_data[0]].keys():
                self.state_index_book[now_data[0]][now_data[3]] = len(self.state_index_book[now_data[0]].keys())
                self.county_index_book[now_data[0]][now_data[3]] = dict()
                self.data[self.year_index_book[now_data[0]]].append([])
            if not now_data[4] in self.county_index_book[now_data[0]][now_data[3]].keys():
                self.county_index_book[now_data[0]][now_data[3]][now_data[4]] = len(self.county_index_book[now_data[0]][now_data[3]].keys())
                self.data[self.year_index_book[now_data[0]]][self.state_index_book[now_data[0]][now_data[3]]].append([])
            if len(self.data[self.year_index_book[now_data[0]]][self.state_index_book[now_data[0]][now_data[3]]][self.county_index_book[now_data[0]][now_data[3]][now_data[4]]]) == 0:
                self.data[self.year_index_book[now_data[0]]][self.state_index_book[now_data[0]][now_data[3]]][self.county_index_book[now_data[0]][now_data[3]][now_data[4]]] = list(now_data[7:])
            else:
                self.data[self.year_index_book[now_data[0]]][self.state_index_book[now_data[0]][now_data[3]]][self.county_index_book[now_data[0]][now_data[3]][now_data[4]]][0] = self.data[self.year_index_book[now_data[0]]][self.state_index_book[now_data[0]][now_data[3]]][self.county_index_book[now_data[0]][now_data[3]][now_data[4]]][0] + now_data[7]



if __name__ == '__main__':
    nflis_data = NflisData()
    print(nflis_data.data[1][3][3])