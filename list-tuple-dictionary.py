# lists
products = ['a', 'b', 'parówki']
products.append('mleko')
products.append('mleko')
products.append('mleko')
y = products.count('mleko')
products[0:1] = 'kanapka'

print(y)
print(products, type(products))
print(products[0:2], type(products[0:2]))
print(len(products))

# tuple
towary = ('a', 'b', 'c', 'd')
print(towary, towary[0:2], type(towary))

# dictionary
person = {'wiek': 20, 'imię': 'Pawel', 'nazwisko': 'Humbak'}
print(person, type(person))
print(person['wiek'])
print(person['imię'])
ab =  person.keys()
print(type(ab))
