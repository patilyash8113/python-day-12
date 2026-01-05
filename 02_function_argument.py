# def add(a,b):#there is parameters in columns
#     return a+b

# c=add(5,3)#This are arguments in columns
# print(c)

#2nd way for functions

# def add(a,b):
#     x=a,b
#     return x
# c = add(3,5)
# print(c)


#default arguments
def add(a,b,plus=0):
    x=a+b+plus
    return x
c=add(3,5,5)
print(c)

#keyword argument
c1=add(b=5,a=3)

def student(age,name):
    print(age,name)
student(age=21,name="yash")
    