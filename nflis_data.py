from data_reader import *

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
            if not now_data[1] in self.state_index_book[now_data[0]].keys():
                self.state_index_book[now_data[0]][now_data[1]] = len(self.state_index_book[now_data[0]].keys())
                self.county_index_book[now_data[0]][now_data[1]] = dict()
                self.data[self.year_index_book[now_data[0]]].append([])
            if not now_data[2] in self.county_index_book[now_data[0]][now_data[1]].keys():
                self.county_index_book[now_data[0]][now_data[1]][now_data[2]] = len(self.county_index_book[now_data[0]][now_data[1]].keys())
                self.data[self.year_index_book[now_data[0]]][self.state_index_book[now_data[0]][now_data[1]]].append([])
            if len(self.data[self.year_index_book[now_data[0]]][self.state_index_book[now_data[0]][now_data[1]]][self.county_index_book[now_data[0]][now_data[1]][now_data[2]]]) == 0:
                self.data[self.year_index_book[now_data[0]]][self.state_index_book[now_data[0]][now_data[1]]][self.county_index_book[now_data[0]][now_data[1]][now_data[2]]] = list(now_data[7:])
            else:
                self.data[self.year_index_book[now_data[0]]][self.state_index_book[now_data[0]][now_data[1]]][self.county_index_book[now_data[0]][now_data[1]][now_data[2]]][0] = self.data[self.year_index_book[now_data[0]]][self.state_index_book[now_data[0]][now_data[1]]][self.county_index_book[now_data[0]][now_data[1]][now_data[2]]][0] + now_data[7]



if __name__ == '__main__':
    nflis_data = NflisData()
    for i in range(5):
        for j in range(8):
            print(nflis_data.data[j][i][0][2])