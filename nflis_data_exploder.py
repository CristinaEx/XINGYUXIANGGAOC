from nflis_data import *
import numpy
# 进行数据扩展

class ExplodedData:

    def __init__(self):
        # YEAR | COMBINE -> DATA
        self.data = []
        exp_data = []
        for i in range(8):
            self.data.append([])
            exp_data.append([])
            for j in range(5):
                exp_data[i].append(0)
        self.combine_index_book = dict()
        nflis_data = NflisData()
        # DATA 中 STATE TOTAL的排列
        self.state_index = list(nflis_data.state_index_book[2010].keys())
        for year in range(2010,2018):
            for state in nflis_data.state_index_book[year].keys():
                exp_data[year-2010][nflis_data.state_index_book[2010][state]] = nflis_data.data[nflis_data.year_index_book[year]][nflis_data.state_index_book[year][state]][0][2]
        for state in nflis_data.state_index_book[2010].keys():
            for county in nflis_data.county_index_book[2010][state].keys():
                useful = True
                for year in range(2011,2018):
                    if county not in nflis_data.county_index_book[year][state].keys():
                        useful = False
                        break
                if useful:
                    self.combine_index_book[state + ' ' + county] = len(self.combine_index_book.keys())
                    for year in range(2010,2018):
                        add_data = [0] * 5
                        add_data[nflis_data.state_index_book[2010][state]] = exp_data[year-2010][nflis_data.state_index_book[2010][state]]
                        self.data[nflis_data.year_index_book[year]].append(nflis_data.data[nflis_data.year_index_book[year]][nflis_data.state_index_book[year][state]][nflis_data.county_index_book[year][state][county]][:2] + add_data)
        self.data = numpy.array(self.data)         

if __name__ == '__main__':
    data = ExplodedData()
    print(data.combine_index_book)