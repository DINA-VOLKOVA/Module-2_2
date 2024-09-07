first = 147
second = 258
third = 369
if first == second and second == third and first == third:
    print('3')
elif first == second or second == third or third == first:
    print('2')
else:
    print('0')

