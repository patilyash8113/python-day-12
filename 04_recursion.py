# A function calling itself to solve the problem called  recursion.

'''
0 1 1 2 3 5 8 13
0 1 2 3 4 5 6 7....

fib(0)=0
fib(1)=1
fib(2)=fib(1)+fib(0)
fib(3)=fib(1)+fib(2)
fib(4)=fib(2)+fib(3) 
fib(n)=fib(n-2)+fib(n-1)
# '''

# def fib(n):
#     #base case of recursion
#     if(n==0 or n==1):
#         return n
#     return fib(n-2)+ fib(n-1)
# print(fib(6))

#fib(4)+fib(5)
#  so fib(4) is broken into two parts 
# fin(2) and fib(3) and fib(5) written as it is.

# fib(4)+fib(5)
# fib(2)+fib(3)+fib(5)
# fib(0)+fib(1)+fib(3)+fib(5)
# 0+1+fib(1)+fib(2)+fib(3)+fib(4)
# 0+1+1+fib(0)+fib(1)+fib(1)+fib(2)+fib(4)
# 0+1+1+0+1+1+fib(0)+fib(1)+fib(2)+fib(3)
# 0+1+1+0+1+1+0+1+fib(0)+fib(1)+fib(3)
# 0+1+1+0+1+1+0+1+0+1+fib(1)+fib(2)
# 0+1+1+0+1+1+0+1+0+1+1+fib(0)+fib(1)
# 0+1+1+0+1+1+0+1+0+1+1+0+1

#why do we use recursion ?
#because it is firectly solving the problems..

# 0 1 1 2 3 5 8 13 21
# 0 1 2 3 4 5 6 07 08

# FIB(0)=0
# fib(1)=1
# FIB(2)=FIB(0)+FIB(1)
# FIB(3)=FIB(1)+FIB(2)
# FIB(4)=FIB(2)+FIB(3)
# FIB(5)=FIB(3)+FIB(4)
# fib(6)=FIB(4)+FIB(5)
# FIB(n)=FIB(n-2)+fib(n-1)

def fib(n):
    if(n==0 or n==1):
        return n
    return fib(n-2) + fib(n-1)
print(fib(6))

fib(4)+fib(5)
fib(2)+fib(3)+fib(5)
fib(0)+fib(1)+fib(3)+fib(5)
0+1+fib(1)+fib(2)+fib(3)+fib(4)
0+1+1+fib(1)+fib(0)+fib(1)+fib(2)+fib(4)
0+1+1+1+0+1+fib(1)+fib(0)+fib(2)+fib(3)
0+1+1+1+0+1+1+0+fib(1)+fib(0)+fib(3)
0+1+1+1+0+1+1+0+1+0+fib(1)+fib(2)
0+1+1+1+0+1+1+0+1+0+1+fib(1)+fib(0)
0+1+1+1+0+1+1+0+1+0+1+1+0