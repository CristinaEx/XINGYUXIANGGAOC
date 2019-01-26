from nflis_data import *
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

if __name__ == '__main__':
    eachStatePie('eachStatePie')