from nflis_data import *
from nflis_data_exploder import *
import matplotlib.pyplot as plt
import numpy
import os

colors = ['c','g','r','gray','y','darkred','lime','lightgray','b','m','k']
ver = 'v0.9'

def eachStatePie(save_path):
    """
    历年各个州占比圆饼图
    """
    if not os.path.exists(save_path):
        os.makedirs(save_path)
    nflis_data = NflisData()
    for y in range(8):
        year = list(nflis_data.year_index_book.keys())[y]
        label = list(nflis_data.state_index_book[year].keys())
        plt.title(str(year) + ' TotalDrugReportsState')
        data = []
        color = []
        for i in range(5):
            data.append(nflis_data.data[y][i][0][2])
            if label[i] == 'OH':
                color.append('c')
            elif label[i] == 'VA':
                color.append('g')
            elif label[i] == 'WV':
                color.append('r')
            elif label[i] == 'KY':
                color.append('gray')
            else:
                color.append('y')
        plt.axis('equal')
        plt.pie(data, labels=label, autopct='%1.1f%%',colors=color)
        plt.savefig(save_path + '\\' + str(year) + ' TotalDrugReportsState.png')
        plt.close()

def eachStateLine(save_path):
    """
    历年各个州占比圆饼图
    """
    if not os.path.exists(save_path):
        os.makedirs(save_path)
    nflis_data = NflisData()
    plt.title('TotalDrugReportsState')
    data = []
    for i in range(5):
        data.append([])
    for y in range(8):
        year = list(nflis_data.year_index_book.keys())[y]
        label = list(nflis_data.state_index_book[year].keys())
        color = []
        for i in range(5):
            if label[i] == 'OH':
                data[0].append(nflis_data.data[y][i][0][2])
            elif label[i] == 'VA':
                data[1].append(nflis_data.data[y][i][0][2])
            elif label[i] == 'WV':
                data[2].append(nflis_data.data[y][i][0][2])
            elif label[i] == 'KY':
                data[3].append(nflis_data.data[y][i][0][2])
            else:
                data[4].append(nflis_data.data[y][i][0][2])
    txt = ['OH','VA','WV','KY','PA']
    lines = [0]*5
    for i in range(5):
        lines[i], = plt.plot(data[i],color = colors[i])  
    plt.legend(lines, txt, loc = 'upper right')
    plt.xlabel('year')
    plt.ylabel('num')
    # plt.show()
    plt.savefig(save_path + '\\' + 'TotalDrugReportsState.png')
    plt.close()

def eachStateCountyLine(save_path):
    """
    各county在各州之间的折线图
    只选用5年都有数据的county
    """
    if not os.path.exists(save_path):
        os.makedirs(save_path)
    data = ExplodedData()
    combines = list(data.combine_index_book.keys())
    for state in data.state_index:
        plt.title(state)
        txt = []
        lines = []
        for combine_index in range(len(combines)):
            if combines[combine_index].split(' ')[0] == state:
                txt.append(combines[combine_index].split(' ')[1])
                data_list = []
                for j in range(8):
                    data_list.append(data.data[j][combine_index][1])
                line, = plt.plot(data_list,color = colors[combine_index%11])  
                lines.append(line)
        plt.legend(lines, txt, loc = 'upper right')
        plt.xlabel('year')
        plt.ylabel('num')
        # plt.show()
        plt.savefig(save_path + '\\' + state + '.png')
        plt.close()

if __name__ == '__main__':
    eachStateCountyLine('eachStateCountyLine')