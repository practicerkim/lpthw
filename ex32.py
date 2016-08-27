# -*- coding: utf-8 -*-

the_count = [1,2,3,4,5]
fruits = ['apples', 'oranges', 'pears', 'apricots']
change = [1, 'pennies', 2, 'dimes', 3, 'quarters']

for number in the_count:
    print number
print '\n'
for fruit in fruits:
    print fruit     # 배열의 요소들을 하나씩 출력한다고 생각하면 될 듯
print '\n'
for i in change:
    print i
print '\n'
elements = []

for i in range(0,6):
    #print i
    elements.append(i)

for i in elements:
    print i
