# -*- coding: utf-8 -*-
#%%
# 计算预测的结果和实际结果的是否相等，返回一个bool类型的张量
'''
predictions: 你的预测结果（一般也就是你的网络输出值）大小是预测样本的数量乘以输出的维度
target:      实际样本类别的标签，大小是样本数量的个数
k:           每个样本中前K个最大的数里面（序号）是否包含对应target中的值
'''
tf.nn.in_top_k(predictions, targets, k, name=None)

#%% TEST

import tensorflow as tf;
 
A = [[0.8,0.6,0.3], [0.1,0.6,0.4]]
B = [1, 1]
out = tf.nn.in_top_k(A, B, 1)
with tf.Session() as sess:
	sess.run(tf.initialize_all_variables())
	print(sess.run(out)) # [False  True]


# 使用这个函数时，注意label（target）不是onehot