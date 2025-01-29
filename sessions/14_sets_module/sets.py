################################################################
# sets erstellen
my_set = {1, 2, 3, 4, 2}
print(my_set)

# sets modifizieren
my_set.add(900)
my_set.add(4)

print(my_set)

my_other_set = {3, 4, 5, 6, 7}
my_set.update(my_other_set)

print(my_set)

my_set.remove(900)
print(my_set)

my_set.discard(3)
print(my_set)

# wirft error, wenn element nicht vorhanden
# my_set.remove(900)
# print(my_set)

my_set.discard(3)
print(my_set)

my_set.pop()
print(my_set)

# funktioniert nicht mit einem leeren set
# for i in range(len(my_set) + 1):
#     print(f'Entferntes Element: {my_set.pop()}, set: {my_set}')

# anzahl der elemente ausgeben
print(len(my_set))

################################################################
# set-operationen
print()

a = {1, 2, 3, 4, 5, 6}
b = {5, 6, 7, 8, 9, 10}

print('a:', a)
print('b:', b)

print('Vereinigungsmenge:', a.union(b))
print('Schnittmenge:', a.intersection(b))
print('Differenz von a und b:', a.difference(b))
print('Symmetrische Differenz von a und b:', a.symmetric_difference(b))
print('Symmetrische Differenz von a und b:', (a.union(b)).difference(a.intersection(b)))

print('ist a eine Teilmenge von b?\t', a <= b)

c = {'a', 'b', 'c', 'd'}
d = {'a', 'b', 'c', 'd'}

print(f'ist {c} eine Teilmenge von {d}?\t{c <= d}')

print(f'ist \'a\' in {c}? \t {'a' in c}')
