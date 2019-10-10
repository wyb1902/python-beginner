#RSA算法

p = 17 #秘密
q = 23 #秘密
n = p*q #公开
e = 3   #公开
d = 1 #d的初始值 秘密
while (e*d)%((p-1)*(q-1)) != 1: #求出符合e*d mod (p-1)*(q-1)=1的d值
    d=d+1
print(d,e*d,(p-1)*(q-1),(e*d)%((p-1)*(q-1)))

print("公钥：P=("+str(e)+","+str(n)+")")
print("私钥：S=("+str(d)+","+str(n)+")")

#RSA加密算法

Alice = 232 #原文
Bob1 = Alice1 = pow(232, e) % n #公钥加密，密文

#RSA解密算法
Bob = pow(Bob1, d) % n

print(Alice, Bob)
if Bob == Alice:
    print('成功')
else:
    print('失败')

