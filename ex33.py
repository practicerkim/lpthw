# -*- coding: utf-8 -*-

i = 0
numbers = []

while i < 6:
    print "at the top i is %d" % i
    #print "at the top i is", i
    numbers.append(i)
    i+=1
    print "list: numbers[] %s" % numbers
    #print "list: numbers[]", numbers
    print "at the bottom i is %d" % i
    print '\n'

print "the numbers"
for a in numbers:
    print a

print '\n'

print numbers

"""
Study Drills
1. Convert this while- loop to a function that you can call, and replace 6 in the test
(i < 6) with a variable.

2. Now use this function to rewrite the script to try different numbers.

3. Add another variable to the function arguments that you can pass in that lets you
change the + 1 on line 8, so you can change how much it increments by.

4. Rewrite the script again to use this function to see what effect that has.

5. Now, write it to use for- loops and range instead. Do you need the incrementor in the
middle anymore? What happens if you do not get rid of it?
"""
