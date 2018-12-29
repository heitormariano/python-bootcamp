num01 = 10
num02 = 5
result01 = num01 * num02
print('The result [01] is {}'.format(result01))


num01 = 400
num02 = 2
result02 = num01 // num02  # // --> integer division
print('The result [02] is {}'.format(result02))

num01 = 5
num02 = 10
num03 = 60
num04 = 20

result03 = num01 + num02 * num03
print('The result [03] is {}'.format(result03))

result04 = num01 + num02 * num03 / num04
print('The result [04] is {}'.format(result04))

print('Order of Operations:')
print('1 - Parentheses')
print('2 - Exponents')
print('3 - Multiplication')
print('4 - Division')
print('5 - Addition')
print('6 - Subtraction')

result05 = (num01 + num02) * num03 / num04
print('The result [05] is {}'.format(result05))

result06 = num01 * num02 * num03 / num04
print('The result [06] is {}'.format(result06))

result07 = num01 + num02 - num03 + num04
print('The result [07] is {}'.format(result07))
