filename = raw_input('input filename: ')
print "we're going to erase %s" % filename
print "if you don't want that, hit ctrl-c (^c)"
print "if you do want that, hit return"

raw_input('?')

print "opening the file..."
target = open(filename, 'w')

print "truncating the file. goodbye!"
target.truncate()

print "now i'm going to ask you for three lines"
line1 = raw_input("line1: ")
line2 = raw_input("line2: ")
line3 = raw_input("line3: ")

print "i'm going to write these to the file."
target.write(line1)
target.write('\n')
target.write(line2)
target.write('\n')
target.write(line3)
target.write('\n')

print "and finally, we close it"
target.close()
