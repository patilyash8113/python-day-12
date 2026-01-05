# python-day-12

Today i learn function and recursion in python:
1) I learn function
   -function start with def stetement
   -in function we can give multiple inputs using same program or my meaning is suppose i
   write a small program

   def average(a,b,c):
       d=average(a+b+c)/3
   print(d) or
   return d

   average(3,5,6)
   average(5,2,4)
   
   # in this program i give multiple inputs so i dont need to write a multiple copies of this program..

   **(2) I learn function arguments
   In function argument we use return() instead of print() statement
   in this we use return

   def add(a,b):
       return a+b
   c=add(5,7)
   print(c)
   In this program we use return statement that add a and b and in c variable we assign two values
   5 and 7 and i print c

   ***There are also two types in function
   1) default argument
      def add(a,b,plus=0):
    x=a+b+plus
    return x
c=add(3,5,5)
print(c)

 in this we have two ways to assign values
 1st way=we assign value in parameter
 2nd way= we assign value in arguments.
but there is twist if i assign value in parameters then this value is default
and if i assign value in argument now this is default value..

2)c1=add(b=5,a=3)

def student(age,name):
    print(age,name)
student(age=21,name="yash")

In this we give keywords to parameters and arguments.

(3) Lambdaa function
# square=lambda x:x*x
# '''
# as good as writing
# def square (x):
#     return x*x
# '''
# print(square(5))


# sum=lambda x,y:x+y
# '''
# as good as writing 
# def sum(x,y):
#     return x+y
# that is good for convinience
# '''
# print(sum(5,5))

In there we use lambda function we instead of using keyword of default function 
this is not necessary but we use for convenience..

suppose  square=lambda x:x*x 
So here we create simple square variable and ue lambda function and 
print(square(5)) print it.


(4)  rccursion
a function call itself to solve the problems.
this is usefull for tree treversal or Fibonacci

0 1 1 2 3 5 8 13 #this is Fibonacci values.

# def fib(n):
#     #base case of recursion
#     if(n==0 or n==1):
#         return n
#     return fib(n-2)+ fib(n-1)
# print(fib(6))

#this is manuel work to find the value of 6

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

this is the example of we dont need to write this using manuel we just use function to find Fibonacci values.

   
