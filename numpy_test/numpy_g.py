# coding=utf-8
#利用arange函数读取数据
# import numpy as np
print(np.arange(10))        #生成从0开始，步长为1，元素个数为10的矩阵
print(np.arange(0,10))      #生成从0到10，步长为1的矩阵
print(np.arange(1,4,0.5))   #生成从1到4，步长为0.5的矩阵
print(np.arange(9,-1,-1))   #生成从9到-1，步长为1的矩阵


'''输出
[0 1 2 3 4 5 6 7 8 9]
[0 1 2 3 4 5 6 7 8 9]
[1.  1.5 2.  2.5 3.  3.5]
[9 8 7 6 5 4 3 2 1 0]
'''