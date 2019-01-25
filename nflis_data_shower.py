from nflis_data import *
import matplotlib.pyplot as plt
import numpy
import os

def eachStatePie(save_path):
    """
    历年各个州占比圆饼图
    """
    if not os.path.exists(save_path):
        os.makedirs(save_path)
    nflis_data = NflisData()

if __name__ == '__main__':
    eachStatePie('eachStatePie')