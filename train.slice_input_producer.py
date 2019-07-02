# -*- coding: utf-8 -*-

#%%
'''
tf.train.slice_input_producer是一个tensor生成器，作用是按照设定，
每次从一个tensor列表中按顺序或者随机抽取出一个tensor放入文件名队列。

定义了样本放入文件名队列的方式，包括迭代次数，是否乱序等，要真正将文件放入文件名队列，
还需要调用tf.train.start_queue_runners 函数来启动执行文件名队列填充的线程，
之后计算单元才可以把数据读出来，否则文件名队列为空的，计算单元就会处于一直等待状态，
导致系统阻塞。

在N个epoch的文件名最后是一个结束标志，当tf读到这个结束标志的时候，
会抛出一个 OutofRange 的异常，外部捕获到这个异常之后就可以结束程序了。

tensor_list：包含一系列tensor的列表，表中tensor的第一维度的值必须相等，
即个数必须相等，有多少个图像，就应该有多少个对应的标签。

num_epochs: 可选参数，是一个整数值，代表迭代的次数，如果设置 num_epochs=None,
生成器可以无限次遍历tensor列表，如果设置为 num_epochs=N，生成器只能遍历tensor列表N次。

shuffle： bool类型，设置是否打乱样本的顺序。一般情况下，如果shuffle=True，
生成的样本顺序就被打乱了，在批处理的时候不需要再次打乱样本，
使用 tf.train.batch函数就可以了;如果shuffle=False,就需要在批处理时候使用 
tf.train.shuffle_batch函数打乱样本。

seed: 可选的整数，是生成随机数的种子，在第三个参数设置为shuffle=True的情况下才有用。

capacity：设置tensor列表的容量。

shared_name：可选参数，如果设置一个‘shared_name’，则在不同的上下文环境（Session）
中可以通过这个名字共享生成的tensor。

name：可选，设置操作的名称。
'''

slice_input_producer(tensor_list, num_epochs=None, shuffle=True, seed=None,  
                         capacity=32, shared_name=None, name=None)  

#%%TEST

import tensorflow as tf
 
images = ['img1', 'img2', 'img3', 'img4', 'img5']
labels= [1,2,3,4,5]
 
step_num=8
 
f = tf.train.slice_input_producer([images, labels],num_epochs=None,shuffle=False)
 
with tf.Session() as sess:
    sess.run(tf.global_variables_initializer())
    coord = tf.train.Coordinator()
    threads = tf.train.start_queue_runners(sess=sess, coord=coord)
    for i in range(step_num):
        k = sess.run(f)
        print ('************************')
        print (i,k)
 
    coord.request_stop()

'''
************************  
(0, ['img1', 1])  
************************  
(1, ['img2', 2])  
************************  
(2, ['img3', 3])  
************************  
(3, ['img4', 4])  
************************  
(4, ['img5', 5])  
************************  
(5, ['img1', 1])  
************************  
(6, ['img2', 2])  
************************  
(7, ['img3', 3]) 
'''