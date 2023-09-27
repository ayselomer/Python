# Write code below 💖
import random 

choices = ['✊', '✋', '✌']

print('1) ✊ Rock ')
print('2) ✋ Paper')
print('3) ✌ Scissors')





you = int(input('\nChoose one: '))

while (you != 1 and you !=2 and you !=3):
  print('error: choose 1, 2 or 3')
  you = int(input('\nChoose one: '))

print('')

computer = random.randint(1, 3)
print(f'computer chose: {choices[computer-1]}' )
print(f'you chose: {choices [you-1]}')

print('')

if computer == 1 and you == 2:
  print('You win')

if computer == 1 and you == 3:
  print('Computer wins')

if computer == 2 and you == 1:
    print('Computer wins')
  
if computer == 2 and you ==3:
    print('You win')
  
if computer == 3 and you == 1:
  print('You win')

if computer == 3 and you == 2:
  print('Computer wins')

if ((computer == 1 and you == 1) or (computer == 2 and you == 2) or (computer == 3 and you ==3)):
  print('draw')





