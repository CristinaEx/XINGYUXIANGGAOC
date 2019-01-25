import pandas
import xlrd

def readExceldFile(file_name,header = None):
    """
    读取excel文件
    """
    data = pandas.read_excel(io = file_name,header = header)
    return data

def readCsvFile(file_name):
    """
    读取csv文件
    """
    data = pandas.read_csv(file_name)
    return data

if __name__ == '__main__':
    data = readExceldFile('2019_MCMProblemC_DATA\\2018_MCMProblemC_DATA\\MCM_TEST.xlsx',header = 0)
    print(data)
    data = readCsvFile('2019_MCMProblemC_DATA\\2018_MCMProblemC_DATA\\ACS_10_5YR_DP02\\ACS_10_5YR_DP02_with_ann.csv')