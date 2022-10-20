import requests

print('hi! welcome to my Harry Potter game B) multiplayer edition ')
print(' ')
number1=input('player 1, please insert a number between 0 - 24 ')
print('')
url = f'https://hp-api.herokuapp.com/api/characters/staff'

request = requests.get(url)

character=request.json()

char1 = character[int(number1)]
print('')

print('thank you, this is your character!:')
print(char1['name'])
print('')

stats1=input('player 1, would you like to see your stats? y/n ')

if stats1=='y' or stats1=='Y':
    print(('Name: ') +(char1['name']))
    print(('Species: ') + (char1['species']))
    if char1['species'] == 'human':
        print('(a human - oh no!)')
    print(('Wizard: ') + str((char1['wizard'])))
    print(('Wand core: ') + (char1['wand']['core']))

if stats1=='n' or stats1=='N':
    print('okay!')

if stats1!='y' and stats1!='Y' and stats1!='n' and stats1!='N':
    print('come on, please just say y or n!! i guess its a no ...')

print('')

number2=input(' now player 2, please insert a different number between 0 - 24 ')
print('')

char2 = character[int(number2)]
print('')

print('thank you, this is your character!:')
print(char2['name'])
print('')

stats2=input('player 2, would you like to see your stats? y/n ')
if stats2=='y' or stats2=='Y':
    print(('Name: ') +(char2['name']))
    print(('Species: ') + (char2['species']))
    if char2['species']=='human' and char1['species']=='human':
        print('another human - oh no!')
    print(('Wizard: ') + str((char2['wizard'])))
    print(('Wand core: ') + (char2['wand']['core']))

if stats2=='n' or stats2=='N':
    print('okay!')

if stats2!='y' and stats2!='n' and stats2!='Y' and stats2!='N':
    print('okay!')

print('')

print('round 1: species! let us see who wins this round')

print(' ')

input1= input('please press enter to continue . . .')

n1 = 0
n2 = 0
if char1['species']=='human' and char2['species']== 'human':
    print('you are both humans; it is a draw')
    print(' ')
    print('scores! player 1: {} , player 2: {}'.format(n1, n2))

if char1['species']=='human' and char2['species'] != 'human':
    print('Character 1 wins this round! Humans trump other species lol')
    print(' ')
    print('scores! player 1: {} , player 2: {}'.format(n1+1, n2))

if char1['species']!='human' and char2['species'] == 'human':
    print('Character 2 wins this round! Humans trump other species lol')
    print(' ')
    print('scores! player 1: {} , player 2: {}'.format(n1, n2+1))





