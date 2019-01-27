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

def OHCountyAverageLine(save_path):
    """
    OH州每个county逐年各项指标与家庭总数的比值的平均值折线图
    按各个指标分开来排
    """
    if not os.path.exists(save_path):
        os.makedirs(save_path)
    data = OurData()
    attrs = list(data.data_index_book.keys())
    messages = list(data.data_message_book.values())
    for i in range(len(attrs)):
        for j in range(ITEM_NUM):
            if not messages[j]['GEO.display-label'].split(',')[1] == ' Ohio':
                continue
            if not (messages[j]['GEO.display-label'].split(',')[0] == 'Cuyahoga County' or messages[j]['GEO.display-label'].split(',')[0] == 'Hamilton County'):
                continue
            plt.title(messages[j]['GEO.display-label'] + ' ' + list(data.data_index_book.values())[i][1])
            y_data = []
            for year in range(YEAR_NUM):
                y_data.append(data.data[j][year][i])
            line, = plt.plot(y_data,color = colors[0])   
            plt.legend([line], [messages[j]['GEO.display-label']], loc = 'upper right')
            plt.xlabel('year')
            plt.ylabel('number')
            plt.savefig(save_path +'\\' +  messages[j]['GEO.display-label'] + ' ' + list(data.data_index_book.values())[i][1].replace('\"',' ') + '.png')
            plt.close() 

def custom_1(save_path = 'custom_1',years = [0,6]):
    """
    2010和2016年各个州人群血统占比饼图
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
    y_data = [[],[],[],[],[]]
    for i in range(len(attrs)):
        if i < 122:
            continue
        index = 0
        for j in range(YEAR_NUM):
            if not j in years :
                continue
            if i == 122:
                for m in range(5):
                    y_data[m].append([])
            y = [0]*5
            for m in range(ITEM_NUM):
                try:
                    y[states[messages[m]['GEO.display-label'].split(',')[1]]] = y[states[messages[m]['GEO.display-label'].split(',')[1]]] + data.data[m][j][i]
                except:
                    pass
            for m in range(5):
                y_data[m][index].append(y[m])
            index = index + 1
    label = []
    for l in list(data.data_index_book.values()):
        if l[0] < 122:
            continue
        label.append(l[1].split('-')[1])
    print(data.data[0][0][130])
    print(label)
    print(y_data[0][0])
    for i in range(5):
        for j in range(len(years)):
            plt.title(str(years[j]+2010) + list(states.keys())[i] + ' RACE')
            plt.axis('equal')
            plt.pie(y_data[i][j], labels=label , autopct='%1.1f%%',colors=colors)
            plt.savefig(save_path + '\\' + str(years[j]+2010) + list(states.keys())[i] + ' RACE.png')
            plt.close()
            

        
if __name__ == '__main__':
    # eachStateEachYearAverageBar('eachStateEachYearAverageBar',[0,6])
    OHCountyAverageLine('OHCountyAverageLine')
    # custom_1()