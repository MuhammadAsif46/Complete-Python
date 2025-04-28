sets_values = {'mon', 'tue', 'wed', 'thu'}
print(sets_values)
print(type(sets_values))

print(len(sets_values))
print('mon' in sets_values)
print('fri' in sets_values)

sets_values.add('sun')
print(sets_values)

my_list = ['mon', 'tue', 'wed', 'thu', 'mon']
my_set = set(my_list)
print(my_set)