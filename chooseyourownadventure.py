print('find the treasure!')
direction = input('choose Left (L) or Right (R)')
d = direction.upper()
if d == 'L':
  print('you are next to a lake with a crocodile.')
  lake = input('swim(S) or wait(W)')
  l = lake.upper()
  if l == 'S':
    print('game over')
  elif l == 'W':
    print('You are now infront of a door')
    door = input('red(r), blue(b), yellow(y): ')
    darwaaza = door.upper()
    if darwaaza == 'R':
      print('game over')
    elif darwaaza == 'B':
      print('game over')
    elif darwaaza == 'Y':
      print('you win!')
    else:
      print('choose R, B, or Y')
  else:
    print('choose S or W')
elif d == 'R':
  print('game over')
else:
  print('choose L or R')