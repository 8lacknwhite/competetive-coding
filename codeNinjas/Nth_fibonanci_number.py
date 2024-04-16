from math import *
from collections import *
from sys import *
from os import *

## Read input as specified in the question.
## Print output as specified in the question.
x= int(input())
num1 = 1
num2 =1
next_number = num2
if  x == 1 or x ==2:
    print(1)
else:
    for i in range(2,x):
        num1,num2 = num2, next_number
        next_number = num1+num2
    print(next_number)

        
