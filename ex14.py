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
