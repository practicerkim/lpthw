# -*- coding: utf-8 -*-

def make_array(array_length, incre):
    i = 0
    numbers = []
    print '\nfunction using while statement'
    while i < array_length:

        numbers.append(i)

        i = i + incre
        print numbers
    print "\n"

def make_array_using_for(array_length, incre):
    i = 0
    numbers = []
    print '\nfunction using for statement'
    for i in range(0,array_length):
        numbers.append(i)
        print numbers
        i = i + incre
    print '\n'

a = int(raw_input('length of array: '))
b = int(raw_input('increment option: '))
make_array(a,b)
make_array_using_for(a,b)



#"""
#while i < 6:
#    print "at the top i is %d" % i
#    i+=1
#    numbers.append(i)
#    print "list: numbers[] %s" % numbers
#    print '???n'
#    print "at the bottom i is %d" % i

#print "the numbers"
#for a in numbers:
#    print a

#print '???n'

#print numbers
#"""
