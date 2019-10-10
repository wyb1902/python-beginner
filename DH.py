import numpy as np
#D-H密钥交换算法
n1 = np.random.randint(1, high=10000)#由A生成 秘密
n2 = np.random.randint(1, high=10000)#由B生成 秘密
print('n1,n2', n1, n2)
a = pow(125, n1) % 68
b = pow(125, n2) % 68

print(a, b)

a1 = pow(b, n1) % 68
b1 = pow(a, n2) % 68
print(a1, b1)
if a1 == b1:
    print('a1 equal b1')
else:
    print('a1 not equal b1')

