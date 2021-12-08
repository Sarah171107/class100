import math
def my_name(name):
    print('hello '+name)
my_name('sarah')
def sr (num):
    squareroot= math.sqrt(num)
    print(squareroot)
sr(9)

def even_odd(num):
    if(num%2==0):
      print('the number is even')
    else:
        print('the number is odd')
even_odd(5)

def add ():
   num1= int(input('type the first number'))
   num2= int(input('type the second number'))
   sum = num1+num2
   print('sum of both the numbers is  '+  str (sum))
#add()

def div ():
    num1=int(input('type the first number'))
    num2=int(input('type the second number'))
    div = num1/num2
    print ('div of both the numbers is'+ str (div))
#div()

def greater ():
    num1=int(input('type the first number'))
    num2=int(input('type the second number'))
    num3=int(input('type the third number'))
    greater=(num1,num2,num3)
    print()
    if(num1>num2 and num1>num3):
     print(' number1 is the greatest')
    elif(num1<num2 and num3):
     print('number2 is the greatest')
    else:
     print('number3 is the greatest')
greater()


    
