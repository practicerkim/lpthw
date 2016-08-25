
# coding: utf-8

# In[12]:

print "i will now count my chickens:"
print "hens", 25+30/6
print "roosters", 100-25*3%4

print "now i will count the egss"
print 3+2+1-5+4%2-1/4+6
    
print "is it true that 3+2<5-7?"
print 3+2<5-7

print "what is 3+2?", 3+2
print "what is 5-7", 5-7

print "oh, that's why it's false"

print "how about some more."

print "is it greater?", 5>-2
print "is it greater or equal?", 5>=-2
print "is is less or equal?", 5<=-2


# In[16]:

cars=100
space_in_a_car=4.0
drivers=30
passengers=90
cars_not_driven=cars-drivers
cars_driven=drivers
carpool_capacity=cars_driven*space_in_a_car
average_passengers_per_car=passengers/cars_driven

print "there are",cars,"cars available"
print "there are only",drivers,"drivers available"
print "there will be",cars_not_driven,"empty cars today"
print "we can transport",carpool_capacity,"people today"
print "we have",passengers,"to carpool today"
print "we need to put about",average_passengers_per_car,"in each car"


# In[17]:

# ex5.py
name = 'zed a. shaw'
age = 35
height = 74
weight = 180
eyes = 'blue'
teeth = 'white'
hair = 'brown'

print "lets talk about %s"% name
print "he's %d inches tall" % height
print "he's %d pounds heavy" % weight
print "actually that's not too heavy."
print "he's got %s eyes and %s hair" %(eyes, hair)
print "his teeth are usually %s depending on the coffee" % teeth


# In[4]:

# ex6.py
x = "there are %d types of people." % 10
binary = "binary"
do_not = "don't"
y = "those who know %s and those who %s" % (binary, do_not)

print x
print y

print "i said: %r" % x
print "i also said '%s'" % y

hilarious = False
joke_evaluation = "isn't that joke so funny?! %r"

print joke_evaluation % hilarious

w = "this is the left side of..."
e = "a string with a right side"

print w+e


# In[7]:

#ex7.py
print "mary had a little lamb"
print "its fleece was white as %s" % 'snow'
print "and everywhere that mary went"
print "."*10

end1 = "c"
end2 = "h"
end3 = "e"
end4 = "e"
end5 = "s"
end6 = "e"
end7 = "b"
end8 = "u"
end9 = "r"
end10 = "g"
end11 = "e"
end12 = "r"

print end1+end2+end3+end4+end5+end6,
print end7+end8+end9+end10+end11+end12


# In[9]:

#ex8.py
formatter = "%r %r %r %r"

print formatter % (1,2,3,4)
print formatter % ("one","two","three","four")
print formatter % (True, False, True, False)
print formatter % (formatter, formatter, formatter, formatter)
print formatter % (
    "i had this thing",
    "that you could type up right",
    "but it didnt sing",
    "so i said goodnight"
)


# In[11]:

#ex9.py
days = "mon tue wed thu fri sat sun"
months = "jan\nfeb\nmar\napr\nmay\njun\njul\naug"

print "here are the days",days
print "here are the months",months

print """
theres something going on here.
with the three double-quotes.
well be able to type as much as we like.
even 4lines if we want, or 5, or 6.
"""


# In[9]:

#ex10.py
tabby_cat = "\ti'm tabbed in"
persian_cat = "i'm split\non a line"
backslash_cat = "i'm \\ a \\ cat"

fat_cat="""
i'll do a list:
\t* cat food
\t* fishies
\t* catnip\n\t* grass
"""

print tabby_cat
print persian_cat
print backslash_cat
print fat_cat


# In[10]:

#ex10-1.py
for i in ["/", "-", "|", "\\", "|"]:
    print "%r\t" % i


# In[17]:

#ex11.py
print "how old are you?"
age = raw_input()
print "how tall are you?"
height = raw_input()
print "how much do you weigh?"
weight = raw_input()

print "so, you're %s old, %s tall and %s heavy" % (age, height, weight)


# In[19]:

#ex12.py
age = raw_input("how old are you?")
height = raw_input("how tall are you?")
weight = raw_input("how much do you weigh?")

print "so, you're %s old, %s tall and %s heavy" % (age, height, weight)


# In[21]:

#ex13.py
from sys import argv
script, first, second, third = argv
print "the script is called:", script
print "your first variable is:", first
print "your second variable is:", second
print "your third variable is:", third


# In[22]:

#ex14.py
#jupyter에서 실행시 오류 / 인수를 넣을 수 없기 때문에
from sys import argv

script, username = argv
prompt='>'

print "hi %s, i'm the %s script" % (username, script)
print "i'd like to ask you a few questions"
print "do you like me %s?" % username
likes = raw_input(prompt)

print "where do you live %s?" % username
lives = raw_input(prompt)

print "what kind of computer do you have?"
computer = raw_input(prompt)

print """
alright, so you said %r about liking me.
you live in %r. not sure where that is.
and you have a %r computer. nice.
""" % (likes, lives, computer)


# In[ ]:

#ex15.py
from sys import argv
script, filename = argv

txt = open(filename)
print "here's your file %r:" % filename
print txt.read()

print "type the filename again:"
file_again = raw_input(">")

txt_again = open(file_again)
print txt_again.read()


# In[ ]:

#ex15_1.py
#jupyter에서 사용가능 / argv를 사용하지 않고, raw_input을 사용

filename = raw_input('>')
txt = open(filename)
print "here's your file %r:" % filename
print txt.read()

print "type the filename again:"
file_again = raw_input('>')

txt_again = open(file_again)
print txt_again.read()


# In[9]:

#ex16.py
filename = raw_input('input filename: ')
print "we're going to erase %s" % filename
print "if you don't want that, hit ctrl-c (^c)"
print "if you do want that, hit return"

answer=raw_input('erase?: ')
if (answer=='y'):
    print "opening the file..."
    target = open(filename, 'w')
    print "truncating the file. goodbye!"
    target.truncate()
    
target = open(filename, 'w')
print "\nnow i'm going to ask you for three lines"
line1 = raw_input("line1: ")
line2 = raw_input("line2: ")
line3 = raw_input("line3: ")

print "i'm going to write these to the file."
target.write('%s \n %s \n %s \n'% (line1, line2, line3))
#target.write('\n')
#target.write(line2)
#target.write('\n')
#target.write(line3)
#target.write('\n')

print "and finally, we close it"

target.close()


# In[35]:

#ex18.py
def print_two(*args):
    arg1, arg2 = args
    print "arg1: %r, arg2: %r" % (arg1, arg2)
    
def print_two_again(arg1, arg2):
    print "arg1: %r, arg2: %r" % (arg1, arg2)
    
def print_one(arg1):
    print "arg1: %r" % arg1

def print_none():
    print "i got nothin"


# In[42]:

print_two('zed', 'shaw')
print_two_again('zed', 'shaw')
print_one('hey')
print_none()


# In[43]:

#ex19.py
def cheese_and_crackers(cheese_count, boxes_of_crackers):
    print "you have %d cheeses!" % cheese_count
    print "you have %d boxes of crackers!" % boxes_of_crackers
    print "man that's enough for a party!"
    print "get a blanket.\n"
    
cheese_and_crackers(20,30)

amount_of_cheese = 10
amount_of_crackers = 50

cheese_and_crackers(amount_of_cheese, amount_of_crackers)

cheese_and_crackers(10+20, 5+6)

cheese_and_crackers(amount_of_cheese+100, amount_of_crackers+1000)


# In[45]:

cheese_and_crackers(int(raw_input()), int(raw_input()))


# In[49]:

#ex20.py
def print_all(a):
    print a.read()
    
def rewind(a):
    a.seek(0)
    
def print_a_line(line_count, a):
    print line_count, a.readline()
    
input_file = raw_input('file name?: ')    
current_file = open(input_file)

print "the whole file"
print_all(current_file)

print "rewind, like a tape"
rewind(current_file)

current_line = 1
print_a_line(current_line, current_file)

current_line = current_line + 1
print_a_line(current_line, current_file)


# In[56]:

#ex21.py
def add(a, b):
    print "adding %f + %f" % (a, b)
    return a + b

def subtract(a, b):
    print "subtract %d - %d" % (a, b)
    return a - b

def multiply(a, b):
    print "multiply %d * %d" % (a, b)
    return a * b

def divide(a, b):
    print "divide %d / %d" % (a, b)
    return a / b

print "math time"

age = add(float(raw_input()), float(raw_input()))
height = subtract(78, 4)
weight = multiply(90, 2)
iq = divide(100.0, 3.0)

age, height, weight, iq

