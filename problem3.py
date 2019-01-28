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
        if not county == 'CUYAHOGA':
            continue             
        if useful :
            x_batch.append(x)
    x_batch = numpy.array(x_batch)
    x_batch = x_batch.transpose((1,0,2,3))
    return x_batch[-1]

def train(save_path = 'problem2_model\\',learning_rate = 0.00001):
    """
    训练
    """  
    model_path = save_path + 'problem2'
    # 初始化权值
    weights = dict()
    biases = dict()
    reader = tf.train.NewCheckpointReader(save_path + 'problem2')
    variables = reader.get_variable_to_shape_map()
    for ele in variables:
        if ele[0] == 'w':
            weights[ele] = tf.Variable(reader.get_tensor(ele),dtype = tf.float32)
        else:
            biases[ele] = tf.Variable(reader.get_tensor(ele),dtype = tf.float32)
    data_batch = getTrainBatch()
    data_batch = tf.Variable(data_batch,dtype = tf.float32)
    data_batch = tf.reshape(data_batch,shape = (1,155))
    data_in = tf.add(tf.matmul(data_batch,weights['wi']),biases['bi'])
    data_in = tf.nn.relu(data_in)
    data_a = tf.add(tf.matmul(data_in,weights['wa']),biases['ba'])
    data_a = tf.nn.leaky_relu(data_a)
    data_b = tf.add(tf.matmul(data_a,weights['wb']),biases['bb'])
    data_b = tf.nn.leaky_relu(data_b)
    output = tf.add(tf.matmul(data_b,weights['wo']),biases['bo'])
    output = tf.nn.leaky_relu(output)
    predict = tf.reshape(output,shape = (1,))
    # 建立优化器 随机梯度下降
    optimizer = tf.train.GradientDescentOptimizer(learning_rate = learning_rate)
    train = optimizer.minimize(predict,var_list = [data_batch])
    with tf.Session(config=tf.ConfigProto(gpu_options=tf.GPUOptions(allow_growth=True))) as sess:
        # 输入变量
        init = tf.group(tf.global_variables_initializer())
        sess.run(init)
        for i in range(10):
            sess.run(train)
            x = sess.run([data_batch]) 
            print(x)

def go(save_path = 'problem2_model\\'):
    model_path = save_path + 'problem2'
    # 初始化权值
    weights = dict()
    biases = dict()
    reader = tf.train.NewCheckpointReader(save_path + 'problem2')
    variables = reader.get_variable_to_shape_map()
    for ele in variables:
        if ele[0] == 'w':
            weights[ele] = numpy.matrix(reader.get_tensor(ele))
        else:
            biases[ele] = numpy.matrix(reader.get_tensor(ele))
    w = weights['wi'] * weights['wa'] * weights['wb'] * weights['wo']
    for i in w:
        if i > 0:
            print('-')
        else:
            print('+')

if __name__ == '__main__':
    go()