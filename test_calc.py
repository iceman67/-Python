import calc
from calc import sub, lsum

x, y = 10, 20
print ("add two numbers ", calc.sum(x, y))

print ("subtract two numbers ", sub(x,y))

y = list(range(5))
print ("add all numbers in list ",  lsum(y))