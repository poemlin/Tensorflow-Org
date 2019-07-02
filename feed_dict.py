# -*- coding: utf-8 -*-
'''
feed_dict的作用是给使用placeholder创建出来的tensor赋值
占位符并没有初始值，它只会分配必要的内存。
在会话中，占位符可以使用 feed_dict 馈送数据。
'''
import tensorflow as tf
 
# 定义placeholder
input1 = tf.placeholder(tf.float32)
input2 = tf.placeholder(tf.float32)
 
# 定义乘法运算
#因为是一个数值相乘，只要简单的乘法即可：tf.multiply()
output = tf.multiply(input1, input2) 
 
# 通过session执行乘法运行
with tf.Session() as sess:
    # 执行时要传入placeholder的值
    print(sess.run(output, feed_dict = {input1:[2.], input2: [3.]}))
