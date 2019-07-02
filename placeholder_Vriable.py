# -*- coding: utf-8 -*-


x = tf.placeholder(tf. float32, [None, 784]),
y_＝ tf.placeholder(tf.float32,[None, 10])
W = tf.Variable(tf.zeros([784, 10]))
b = tf.Variable(tf.zeros([l0]))
'''

在 TensorFlow 中 无论是
占位符还是变量， 他们实际上都是“ Tensor”。从 TensorFlow 的名字中，就
可以看出 Tensor 在整个系统中处于核心地位。 TensorFlow 中的 Tensor 并不
是具体的数值， 只是一些我们“希望” TensorFlow 系统计算的“节点’。
这里的占位符和变量是不同类型的 Tensor。

先来讲解占位符。占位符不
依赖于真他的 Tensor ，他的值由用户自行传递给 TensorFlow ，通常用来存储
样本数据和标签。如在这里定义了 x = tf.placeholder(tf. float32, [None, 784]),
它是用来存储训练图片数据的占位符。宫的形状为［None, 784], None 表示
这一维的大小可以是任意的，也就是说可以传递任意张训练图片给这个占位
符，每张图片用一个 784 维的向量表示 。 同样的， y_＝ tf.placeholder(tf.float32,
[None, 10］）也是个占位符，它存储训练图片的实际标签 。

再来看什么是变量 。 变量是指在计算过程中可以改变的值，每次计算后
变量的值会被保存下来，通常用变量来存储模型的参数 。 如这里创建了两个
变量： W = tf.Variable(tf.zeros([784, 10 ］）） 、 b = tf.Variable(tf.zeros([lO］）） 。 
他们都是 Softmax 模型的参数 。 创建变量时通常需要指定某些初始值 。 这里 W
的初始值是一个 784× 10 的全零矩阵， b 的初始值是一个 10 维的 0 向量。



















'''