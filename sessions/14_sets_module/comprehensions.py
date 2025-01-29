#################################################################
# eine Liste mit fortlaufenden Werten erstellen
my_list = []

for i in range(20):
    my_list.append(i)

# alternativ auch als Ein-Zeiler mittels 'List-Comprehension'
my_list_2 = [(i * 100) for i in range(20)]

print(my_list)
print(my_list_2)

#################################################################

my_string = 'abcdefghijklmnopqrstuvwxyz'
my_dictionary = {string_val:list_val for list_val, string_val in zip(my_list, my_string) }

# for (list_val, string_val) in zip(my_list, my_string):
    # print(f'Liste: {list_val}, Buchstabe: {string_val}')

print(my_dictionary)
