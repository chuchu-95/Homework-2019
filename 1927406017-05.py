import random
x = random.randint(1, 9)
y = random.randint(0, 9)
z = random.randint(0, 9)
fig = x*100 + y*10 + z
print(fig)
fig = int(fig)
a = fig//100
b = fig//10 % 10
c = fig % 10
num = c * 100 + b * 10 + a
print(num)



