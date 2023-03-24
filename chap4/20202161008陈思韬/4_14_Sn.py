import random

n = random.randint(1,10)

x = 1
s = 0
for i in range(1,n+1):
    s += x
    x = 10*x+1

print("n = {0}，sn = {1}".format(n,s))
