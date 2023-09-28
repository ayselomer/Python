# Write code below 💖

a = int(input('a: '))
b = int(input('b: '))

def add(a, b):
  return a + b

def sub(a, b):
  return a - b

def mul(a, b):
  return a * b

def div(a, b):
  return a/b

q = input('+, -, *, /')

if q == '+':
  print(add(a, b))

if q == '-':
  print(sub(a, b))

if q == '*':
  print(mul(a, b))

else:
  print(div(a, b))



