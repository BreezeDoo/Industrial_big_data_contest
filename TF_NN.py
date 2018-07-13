from __future__ import print_function
import tensorflow as tf
import csv
import random


def add_layer(inputs, in_size, out_size, activation_function=None):
    # add one more layer and return the output of this layer
    Weights = tf.Variable(tf.random_normal([in_size, out_size]), dtype=tf.float32)
    biases = tf.Variable(tf.zeros([1, out_size]) + 0.1, dtype=tf.float32)
    Wx_plus_b = tf.matmul(inputs, Weights) + biases
    if activation_function is None:
        outputs = Wx_plus_b
    else:
        outputs = activation_function(Wx_plus_b)
    return outputs


# Load train data
with open(r'C:\Users\Yuhang Du\Desktop\ACT\python\15\Ldata_number_train_15.csv', 'r') as Ldata_train:
    train_reader = csv.reader(Ldata_train)
    data_train = []
    for row in train_reader:
        del row[27]
        del row[0]
        row = [float(item) for item in row]
        data_train.append(row)
    random.shuffle(data_train)

# Load test data
with open(r'C:\Users\Yuhang Du\Desktop\ACT\python\15\Ldata_number_test_15.csv', 'r') as Ldata_test:
    # 时间按序号排序的带标签测试数据集
    test_reader = csv.reader(Ldata_test)
    x_test = []
    y_test = []
    for row in test_reader:
        del row[27]
        del row[0]
        row = [float(item) for item in row]
        x_test.append(row)
    random.shuffle(x_test)
    len_ = len(x_test)
    for i in range(len_):
        if float(x_test[i][26]) == 1:
            y_test.append([0, 1])
        else:
            y_test.append([1, 0])
        del x_test[i][26]


# define placeholder for inputs to network
x = tf.placeholder(tf.float32, [None, 26])
y_ = tf.placeholder(tf.float32, [None, 2])
# add hidden layer
l1 = add_layer(x, 26, 100, activation_function=tf.nn.relu)
l2 = add_layer(l1, 100, 100, activation_function=tf.nn.relu)
l3 = add_layer(l2, 100, 40, activation_function=tf.nn.relu)
# add output layer
logits = add_layer(l3, 40, 2, activation_function=None)

y = tf.nn.softmax(logits)
# the error between prediction and real data
cross_entropy = tf.nn.softmax_cross_entropy_with_logits(labels=y_, logits=logits)
loss = tf.reduce_mean(cross_entropy)
train_step = tf.train.GradientDescentOptimizer(0.01).minimize(loss)

correct_prediction = tf.equal(tf.argmax(y, 1), tf.argmax(y_, 1))
accuracy = tf.reduce_mean(tf.cast(correct_prediction, tf.float32))

init = tf.global_variables_initializer()
sess = tf.Session()
sess.run(init)

times = len_ // 256
counter = 0
for count in range(10000):
    # 训练集生成
    x_batch_train = []
    y_batch_train = []
    for i in range(256):
        row = [data_train[i][j] for j in range(26)]
        x_batch_train.append(row)
        if data_train[i][26] == 1:
            y_batch_train.append([0, 1])  # 异常是[0,1]
        else:
            y_batch_train.append([1, 0])  # 正常是[1,0]
    train_feed_dict = {x: x_batch_train, y_: y_batch_train}
    sess.run(train_step, feed_dict=train_feed_dict)
    counter += 1
    # if counter == times:
    random.shuffle(data_train)
    #    counter = 0
    if count % 10 == 0:
        print(count/10)
        print(sess.run(loss, feed_dict=train_feed_dict))
        print(sess.run(accuracy, feed_dict=train_feed_dict))

print("Train step finished.\nThe loss and accuracy of test set are as followed:")
# 输出预测信息
test_feed_dict = {x: x_test, y_: y_test}
prediction = sess.run(y, feed_dict=test_feed_dict)
with open(r'C:\Users\Yuhang Du\Desktop\ACT\python\15\Ldata_number_test_15.csv', 'r') \
    as Ldata_test:
    with open(r'C:\Users\Yuhang Du\Desktop\ACT\python\15\Ldata_number_test_predict_15.csv', 'w', newline='') \
            as Ldata_test_predict:
        # 带神经网络预测标签的测试数据集
        reader = csv.reader(Ldata_test)
        writer = csv.writer(Ldata_test_predict)
        counter = 0
        for row in reader:
            flag = 0
            if prediction[counter][0] > prediction[counter][1]:
                pass
            else:
                flag = 1
            row.append(flag)
            writer.writerow(row)
            counter = counter + 1

print(sess.run(loss, feed_dict=test_feed_dict))
print(sess.run(accuracy, feed_dict=test_feed_dict))

# abs
# matplot
# 错误信息