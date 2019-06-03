# 生成数列
def fiboList(num):
    numlist = [0,1]
    for i in range(num - 2):
        numlist.append(numlist[-2] + numlist[-1])
    return numlist


# 生成值
def fibo(num):
    if num == 1:
        return 0
    if num == 2 or num ==3 :
        return 1
    else:
        return fibo(num-1)+fibo(num-2)
def fibo_list(num):
    numli = []
    for i  in range(1,num):
        numli.append(fibo(i))
    return numli

