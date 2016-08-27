#ex24.py
poem = """
\tThe lovely world
with logic so firmly planted
cannot discern \n the needs of love
nor comprehend passion from intuition
and requires an explanation
\n\twhere there is none.
"""

print "-------------"
print poem
print "-------------"

five = 10 - 2  + 3 - 6
print "this should be five: %s" % five

#beans=0
#jars=0
#crates=0

def secret_formula(started):
    jelly_beans = started * 500
    jars = jelly_beans / 1000
    crates = jars / 100
    #print('%s %s %s' % (jelly_beans, jars, crates))
    return jelly_beans, jars, crates

start_point = 10000
#beans, jars, crates = secret_formula(start_point)
secret_formula(start_point)
print jars

#print "with a starting point of: %d" % start_point
#print "we'd have %d beans, %d jars, and %d crates" % (jelly_beans, jars, crates)

#start_point = start_point / 10

#print "we can also do that this way:"
#print "we'd have %d beans, %d jars and %d crates" % secret_formula(start_point)
