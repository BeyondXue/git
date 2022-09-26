# 判断奇偶数
'''
n=int(input("输入数字:"))
if n%2==0:
    print(f"{n}是偶数")
else:
    print(f"{n}是奇数")
'''

# 输出绝对值
'''
n=int(input("输入数字:"))
if n>0:
    print(f"{n}的绝对值是 {n}")
else:
    print(f"{n}的绝对值是 {-n}")
'''

# 输出两数字里较大的
'''
m=int(input("输入数字1:"))
n=int(input("输入数字2:"))
 #print(m>n? m:n)
if m>n:
    print(f"{m},{n}里面较大的数字是{m}")
else:
    print(f"{m},{n}里面较大的数字是{n}")
'''

# 输出成绩等级 A-E
'''
n=float(input("输入成绩:"))
if 90<=n<=100:
    print('A')
elif 80<=n<=89:
    print('B')
elif 70<=n<=79:
    print('C')
elif 60<=n<=69:
    print('D')
else:
    print('E')
'''

# 输出数字0-7作为星期
'''
n=float(input("输入整数:"))
if n==0:
    s='Sunday'
elif n==1:
    s='Monday'
elif n==2:
    s = 'Tuesday'
elif n==3:
    s = 'Wednesday'
elif n==4:
    s='Thursday'
elif n==5:
    s = 'Friday'
elif n==6:
    s='Sturday'
else:
   s="输入错误"
print(s)
'''

# 一元二次方程
'''
import math
a=int(input("输入a: "))
b=int(input("输入b: "))
c=int(input("输入c: "))
if a!=0:
    d=b**2-4*a*c
    if d>0:
        d=math.sqrt(d)  #计算d的开根
        x1=(-b+d)/(2*a)
        x2 = (-b - d) / (2 * a)
        print(f"两个实数解为: x1={x1},x2={x2}")
    elif d==0: #只有一个实数解
        print(f"只有一个实数解为: x1=x2=",-b/(2*a))
    elif d<0:
        print("方程无实数解")
    else:
        print("不是一元二次方程")
'''

# whlie求和
'''
n=int(input("输入n: "))
sum=0
i=1
while i<=n:
    sum+=i
    i+=1
print(f"1~{n}的和为:{sum}")
'''

# 计算平均成绩
'''
sum=0
i=1
n=int(input("输入班级人数: "))
while i<=n:
    m=int(input(f"输入第{i}个同学的成绩: "))
    sum+=m
    i+=1
print(f"班级共有{n}人,总成绩为: {sum},平均成绩为: ",sum/n)
'''

# 正整数翻转1
'''
采用字符串
s=(input("输入整数: "))
s=s[::-1]
print(s)
'''

# 正整数翻转2
'''
n=int(input("输入正整数: "))
s=""
while n !=0:
    m=n%10
    s+=str(m)
    n=n//10
print(s)
'''

# 有理数除法精确计算

# 计算素数
'''
n = int(input("输入正整数: "))
i = 2
while i < n :
    if n % i == 0:
        break
    i += 1
if n == i:
    print(f"{n}是素数")
else:
    print(f"{n}不是素数")
'''

# 找最小公倍数
'''
m = int(input("输入正整数1: "))
n = int(input("输入正整数2: "))
c=0
if m > n:
    c = m
elif m == n:
    print(f"{m},{n}的最小公倍数是:{m}")
else:
    c = n
    sum = m * n
    while c <= sum:
        if c % m == 0 and c % n == 0:
            break
        c += 1
    print(f"{m},{n}的最小公倍数是:{c}")
'''

# 找最小公约数
'''
m = int(input("输入正整数1: "))
n = int(input("输入正整数2: "))
c=0
if m > n:
    c = n
elif m == n:
    print(f"{m},{n}的最大公约数是:{m}")
else:
    c = m
    while c >=1:
        if c % m == 0 and c % n == 0:
            break
        c -= 1
    print(f"{m},{n}的最大公约数是:{c}")
'''

# 无限while循环
'''
while True:
    n = int(input("输入成绩[0,100]之间: "))
    if 0 <= n <= 100:
        break
print(f"成绩 = {n}")
'''

# 计算 a+aa+aaa+...+a..m 的和
# 第n个数字=10*m+a
'''
a = int(input("输入a: "))
n = int(input("输入n: "))
sum = 0
m = 0
for i in range(n):
    m = 10 * m + a  # 每一项的值
    sum += m
    if i < n-1:
        print(m, end="+")
    else:
        print(m,end="=")
print(sum)
'''


# 啤酒两块一瓶，四个盖子换一瓶，两个空瓶换一瓶，十块钱可以喝几瓶
def beersnumbers(m):
    count = m // 2  # 啤酒数
    ping = 5  # 瓶子数
    gai = 5  # 盖子数
    # if count>0:


# 找出1-100里面的素数
count = 0
flag=1
for i in range(1, 101):
    for j in range(2,i):
        if i % j == 0:
            flag=-1
            break
        else:
            flag=1
    if flag==1:
        print(i)

#
