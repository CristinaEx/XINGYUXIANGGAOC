from nflis_data_exploder import *
import numpy
import tensorflow as tf
import os
import json

def getTrainBatch():
    """
    获取训练用的data和label
    """
    data = ExplodedData()
    print(data.state_index)
    x_batch = data.data[:7]
    y_batch = []
    for i in range(1,8):
        y_batch.append([])
        for j in range(380):
            y_batch[i-1].append(data.data[i][j][0] - data.data[i-1][j][0])
    return x_batch,y_batch

def saveData(save_path,w,b,s):
    data = dict()
    data['w'] = w.tolist()
    data['b'] = b.tolist()
    data['s'] = s.tolist()
    with open(save_path, 'w') as f:
        json.dump(data,f,ensure_ascii=False)

def loadData(model_path):
    with open(model_path, 'r') as f:
        load_dict = json.load(f)
    w = load_dict['w']
    b = load_dict['b']
    s = load_dict['s']
    return w,b,s

def firstTrain(model_path,learning_rate = 0.0001,iterate_time = 1000):
    """
    首次训练
    """
    train_batch,label_batch = getTrainBatch()
    train_batch = tf.cast(train_batch,dtype = tf.float32)
    train_batch = tf.reshape(train_batch,shape = (7*380,7))
    label_batch = tf.cast(label_batch,dtype = tf.float32)
    label_batch = tf.reshape(label_batch,shape = (7*380,))
    # 生成随机权值
    w = tf.get_variable('w',initializer=tf.random_normal([7,1]),trainable = True)
    b = tf.get_variable('b',initializer=tf.random_normal([1,]),trainable = True)
    s = tf.get_variable('s',initializer=tf.random_normal([1,1]),trainable = True)

    train_batch = tf.matmul(train_batch,w)
    train_batch = tf.nn.bias_add(train_batch, b)
    train_batch = tf.sigmoid(train_batch)
    train_batch = tf.matmul(train_batch,s)

    pred = tf.reduce_mean(train_batch,reduction_indices = 1)

    loss = pred - label_batch
    loss = tf.reduce_mean(tf.abs(loss))
    # 建立优化器 随机梯度下降
    optimizer = tf.train.GradientDescentOptimizer(learning_rate = learning_rate)
    # 减少误差，提升准确度
    train = optimizer.minimize(loss)
    # 输入所有的变量
    init = tf.group(tf.global_variables_initializer(),tf.local_variables_initializer())
    with tf.Session(config=tf.ConfigProto(gpu_options=tf.GPUOptions(allow_growth=True))) as sess:
        sess.run(init)
        for m in range(iterate_time):
            sess.run(train)
            lo = sess.run([loss])     
            if iterate_time % (m+1) == 0:
                print('loss:',end = '')
                print(lo)
        if not os.path.exists(model_path):
            os.makedirs(model_path) 
        model_path = model_path + 'data.json'
        wi,bi,si = sess.run([w,b,s])
        saveData(model_path,wi,bi,si)

def nextTrain(model_path,learning_rate = 1,iterate_time = 1000):
    model_path = model_path + 'data.json'

    train_batch,label_batch = getTrainBatch()
    train_batch = tf.cast(train_batch,dtype = tf.float32)
    train_batch = tf.reshape(train_batch,shape = (7*380,7))
    label_batch = tf.cast(label_batch,dtype = tf.float32)
    label_batch = tf.reshape(label_batch,shape = (7*380,))
    # 生成随机权值
    wi,bi,si = loadData(model_path)
    w = tf.get_variable('w',initializer=wi)
    b = tf.get_variable('b',initializer=bi)
    s = tf.get_variable('s',initializer=si)

    train_batch = tf.matmul(train_batch,w)
    train_batch = tf.nn.bias_add(train_batch, b)
    train_batch = tf.sigmoid(train_batch)
    train_batch = train_batch * s

    pred = tf.reduce_mean(train_batch,reduction_indices = 1)

    loss = pred - label_batch
    loss = tf.reduce_mean(tf.abs(loss))
    # 建立优化器 随机梯度下降
    optimizer = tf.train.GradientDescentOptimizer(learning_rate = learning_rate)
    # 减少误差，提升准确度
    train = optimizer.minimize(loss)
    # 输入所有的变量
    init = tf.group(tf.global_variables_initializer(),tf.local_variables_initializer())
    with tf.Session(config=tf.ConfigProto(gpu_options=tf.GPUOptions(allow_growth=True))) as sess:
        sess.run(init)
        for m in range(iterate_time):
            sess.run(train)
            lo = sess.run([loss])     
            if iterate_time % (m+1) == 0:
                print('loss:',end = '')
                print(lo)
        wi,bi,si = sess.run([w,b,s])
        saveData(model_path,wi,bi,si)

def train(model_path = 'model\\',learning_rate = 1,iterate_time = 10000):
    """
    训练
    """
    if not os.path.exists(model_path + 'data.json'):
        firstTrain(model_path,learning_rate,iterate_time)
    else:
        nextTrain(model_path,learning_rate,iterate_time) 

if __name__ == '__main__':
    train(learning_rate = 1,iterate_time = 10000)