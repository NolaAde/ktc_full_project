float('12')

float('123.456789')

your_age = input('Enter your age: ')
age = float(your_age)
if age > 13:
    print('You are %s years too old' % (age - 13))

#int(123.456)

#int('123')

#int('123.456')

#len('this is a test string')

creature_list = ['unicorn', 'cyclops', 'fairy', 'elf', 'dragon','troll']
print(len(creature_list))

enemies_map = {'Batman' : 'Joker','Superman' : 'Lex Luthor','Spiderman' : 'Green Goblin'}
print(len(enemies_map))

fruit = ['apple', 'banana', 'clementine', 'dragon fruit']
length = len(fruit)
for d in range(0, length):
    print('the fruit at index %s is %s' % (d, fruit[d]))
#     number = [5, 4, 10, 30, 22]
# print(max(number))

strings = 's,t,r,i,n,g,S,T,R,I,N,G'
print(max(strings))

print(max(10, 300, 450, 50, 90))

numbers = [5, 4, 10, 30, 22]
print(min(numbers))

guess_this_number = 61
player_guess = [12, 15, 70, 45]
if max(player_guess) > guess_this_number:
    print('Boom! You all lose')
else:
    print("You win. Noooooooooooooooooooooooooooooooo")