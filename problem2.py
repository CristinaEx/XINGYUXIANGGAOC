from our_data import *
from nflis_data_exploder import *
import numpy
import tensorflow as tf

def getTrainBatch():
    """
    获取训练集
    """
    nflis_data = ExplodedData()
    # print(nflis_data.state_index)
    our_data = OurData()
    counties = list(nflis_data.combine_index_book.keys())
    x_batch = []
    for i in range(len(counties)):
        x = []
        useful = True
        for j in range(7):
            x.append([])
            try:
                county = counties[i].split(' ')[1]
                x[j].append(list(nflis_data.data[j][i][1:]) + our_data.data[our_data.county_index_book[county]][j])
            except:
                useful = False
                break
        if useful :
            x_batch.append(x)
    y_batch = []
    for i in range(1,8):
        y_batch.append([])
        for j in range(380):
            y_batch[i-1].append(nflis_data.data[i][j][1] - nflis_data.data[i-1][j][1])
    y_batch = numpy.array(y_batch)
    x_batch = numpy.array(x_batch)
    x_batch = x_batch.transpose((1,0,2,3))
    return x_batch,y_batch

def train(save_path = 'problem2_model\\',learning_rate = 1,iterate_time = 1000):
    """
    训练
    """  
    model_path = save_path + 'problem2'
    # 初始化权值
    weights = {
        'in': tf.get_variable('wi',initializer=tf.random_normal([155,155])),
        'a': tf.get_variable('wa',initializer=tf.random_normal([155,310])),
        'b': tf.get_variable('wb',initializer=tf.random_normal([310,310])),
        'o': tf.get_variable('wo',initializer=tf.random_normal([310,1]))
    }
    biases = {
        'in': tf.get_variable('bi',initializer=tf.random_normal([155,])),
        'a': tf.get_variable('ba',initializer=tf.random_normal([310,])),
        'b': tf.get_variable('bb',initializer=tf.random_normal([310,])),
        'o': tf.get_variable('bo',initializer=tf.random_normal([1,]))
    }
    data_batch,label_batch = getTrainBatch()
    data_batch = tf.cast(data_batch,dtype = tf.float32)
    data_batch = tf.reshape(data_batch,shape = (7*380,155))
    label_batch = tf.cast(label_batch,dtype = tf.float32)
    label_batch = tf.reshape(label_batch,shape = (7*380,))
    data_in = tf.add(tf.matmul(data_batch,weights['in']),biases['in'])
    data_in = tf.nn.relu(data_in)
    data_a = tf.add(tf.matmul(data_in,weights['a']),biases['a'])
    data_a = tf.nn.sigmoid(data_a)
    data_b = tf.add(tf.matmul(data_a,weights['b']),biases['b'])
    data_b = tf.nn.sigmoid(data_b)
    output = tf.add(tf.matmul(data_b,weights['o']),biases['o'])
    output = tf.nn.leaky_relu(output)
    predict = tf.reshape(output,shape = (7*380,))
    loss = predict - label_batch
    loss = tf.reduce_mean(tf.multiply(loss,loss))
    # loss = tf.reduce_mean(tf.abs(loss))

    # 建立优化器 随机梯度下降
    optimizer = tf.train.GradientDescentOptimizer(learning_rate = learning_rate)

    # 减少误差，提升准确度
    train = optimizer.minimize(loss)

    saver = tf.train.Saver(tf.get_collection(tf.GraphKeys.TRAINABLE_VARIABLES))
    with tf.Session(config=tf.ConfigProto(gpu_options=tf.GPUOptions(allow_growth=True))) as sess:
        # 输入变量
        init = tf.group(tf.global_variables_initializer())
        sess.run(init)
        if os.path.exists(save_path):
            # 变量替换
            saver.restore(sess, model_path)            
        for m in range(iterate_time):
            sess.run(train)
            lo = sess.run([loss]) 
            if m % 100000 == 0:
                if not os.path.exists(save_path):
                    os.makedirs(save_path)
                save_path = saver.save(sess, model_path)
                print("Model saved in file: %s" % save_path)   
            if not iterate_time % (m+1) == 0:
                continue
            print('loss:',end = '')
            print(lo)
        if not os.path.exists(save_path):
            os.makedirs(save_path)
        save_path = saver.save(sess, model_path)
        print("Model saved in file: %s" % save_path)

if __name__ == '__main__':
    train(save_path = 'problem2_model\\',learning_rate = 0.0001,iterate_time = 1000000)