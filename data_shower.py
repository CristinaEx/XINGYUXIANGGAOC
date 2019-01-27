from our_data import *
import matplotlib.pyplot as plt
import numpy
import os

colors = ['c','g','r','gray','y','darkred','lime','lightgray','b','m','k']

def eachStateEachYearAverageBar(save_path,years = [0,1,2,3,4,5,6]):
    """
    每个state各年各项指标与家庭总数的比值的平均值对比条形图
    按每年的各个指标分开来排
    """
    if not os.path.exists(save_path):
        os.makedirs(save_path)
    data = OurData()
    attrs = list(data.data_index_book.keys())
    states = dict()
    states[' Kentucky'] = 0
    states[' Ohio'] = 1
    states[' Pennsylvania'] = 2
    states[' Virginia'] = 3
    states[' West Virginia'] = 4
    messages = list(data.data_message_book.values())
    family_num = [[0]*5]*7
    for i in range(len(attrs)):
        for j in range(YEAR_NUM):
            if not j in years :
                continue
            y = [0]*5
            x = list(states.keys())
            plt.title(str(j+2010) + ' ' + data.data_index_book[attrs[i]][1])
            for m in range(ITEM_NUM):
                try:
                    y[states[messages[m]['GEO.display-label'].split(',')[1]]] = y[states[messages[m]['GEO.display-label'].split(',')[1]]] + data.data[m][j][i]
                except:
                    continue
            if i == 0:
                family_num[j] = y
            else:
                for n in range(5):
                    y[n] = y[n] / family_num[j][n]
            plt.bar(x, y,color=colors)
            plt.savefig(save_path + '\\' + str(j+2010) + ' ' + data.data_index_book[attrs[i]][1].replace('\"','') + '.png')
            plt.close()

def eachCountyAverageBar(save_path):
    """
    每个county逐年各项指标与家庭总数的比值的平均值对比条形图
    按每年的各个指标分开来排
    """
    if not os.path.exists(save_path):
        os.makedirs(save_path)
    data = OurData()
    attrs = list(data.data_index_book.keys())
    for i in range(len(attrs)):
        for j in range(YEAR_NUM):
            pass
        
if __name__ == '__main__':
    eachStateEachYearAverageBar('eachStateEachYearAverageBar',[0,6])