from nflis_data_exploder import *
import numpy

def getTrainBatch():
    """
    获取训练用的data和label
    """
    data = ExplodedData()
    x_batch = data.data[:7]
    y_batch = []
    for i in range(1,8):
        y_batch.append([])
        for d in data.data[i]:
            y_batch[i-1].append(d[0])
    return x_batch,y_batch

def train(save_path):
    """
    训练
    """
    if not os.path.exists(save_path):
        os.makedirs(save_path)

if __name__ == '__main__':
    train('problem1')