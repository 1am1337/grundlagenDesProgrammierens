# ===============================
# Python Cheatsheet
# ===============================

# Float (Gleitkommazahl)
mein_float = 1.0
print('---------------------')
print('float:', mein_float)
print('mein float + 1:', mein_float + 1)
print('mein float - 1:', mein_float - 1)
print('mein float * 2:', mein_float * 2)
print('mein float / 2:', mein_float / 2)
print('mein float % 2:', mein_float % 2)
print('mein float // 2:', mein_float // 2)
print('mein float ** 2:', mein_float ** 2)

# Integer (Ganzzahl)
mein_integer = 2
print('---------------------')
print('mein integer:', mein_integer)

# Booleans
mein_bool = True
mein_bool2 = False
print('---------------------')
print('mein bool:', mein_bool)
print('True and False:', mein_bool and mein_bool2)
print('False and False:', False and False)
print('True and True:', True and True)
print('---')
print('True or False:', mein_bool or mein_bool2)
print('False or False:', False or False)
print('True or True:', True or True)

# String
mein_string = "hallo"
print('-' * 21)
print('mein_string:', mein_string)
print(f'erster Buchstabe von mein_string: {mein_string[0]}')
print(f'die ersten drei Buchstaben von mein_string: {mein_string[:3]}')
print(f'die letzten Buchstaben von mein_string ab dem vierten: {mein_string[3:]}')
print(f'jeder zweite Buchstabe von mein_string: {mein_string[::2]}')
print(f'der String rückwärts: {mein_string[::-1]}')

# Liste (veränderbar)
meine_liste = [1, 2, 3, 4]
print('-' * 21)
print('meine_liste:', meine_liste)
meine_liste.append(10)
print('etwas meine_liste anfügen:', meine_liste)
print('etwas meine_liste anfügen v2:', meine_liste + [100, 200, 300])

# Tuple (nicht veränderbar)
mein_tuple = (1, 2, 3, 4)
print('-' * 21)
print('mein_tuple:', mein_tuple)
print('mein_tuple + (100, 200, 300):', mein_tuple + (100, 200, 300))
print('mein_tuple:', mein_tuple)

# Dictionary (Key-Value-Paare)
mein_dictionary = {
    'Haarfarbe': 'schwarz',
    'Augenfarbe': 'dunkelbraun'
}
print('-' * 21)
print('mein_dictionary:', mein_dictionary)
print('Haarfarbe:', mein_dictionary['Haarfarbe'])
mein_dictionary['Körpergröße'] = 182
print('hinzufügen:', mein_dictionary)

# Set (nur einzigartige Werte)
mein_set = {2, 4, 6, 8, 10, 10}
print('-' * 21)
print('mein_set:', mein_set)
mein_set.add(20)
mein_set.add(20)
print('mein_set mit neuem element:', mein_set)

# ===============================
# Conditionals & Loops
# ===============================

# if-Statement
if True:
    print('test')

# while-Schleife
counter = 0
while counter < 5:
    print(counter)
    counter += 1

# for-Schleife über Liste
print('-' * 21)
for element in meine_liste:
    print(element)

# for-Schleife mit range()
print('-' * 21)
for i in range(3, 20, 2):
    print(i)

# ===============================
# Module
# ===============================
import math
print(math.cos(math.pi * 0.5))
