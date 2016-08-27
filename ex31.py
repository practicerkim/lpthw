print "you enter a dark room with two doors. do you go through door #1 ro door #2?"

door = raw_input('> ')

if door == "1":
    print "giant bear in front of you. what do you do?"
    print "1. take the cake."
    print "2. scream at the bear."
    print "something else creative?"

    bear = raw_input('action?: ')

    if bear == '1':
        print "dead"
    elif bear == '2':
        print "dead"
    else:
        print "well, doing %s is probably better. bear runs away" % bear

elif door == '2':
    print "you stare into the endless abyss at Cthulu's retina"
    print "1. blueberries"
    print "2. yellow jacket clothespins"
    print "3. understanding revolvers yelling melodies"

    insanity = raw_input("> ")

    if insanity == "1" or insanity == "2":
        print "your body survives powered by a mind of jello. good job!"
    else:
        print "the insanity rots your eyes into a pool of muck. good job!"

else:
    print " you stumble around and fall on a knife and die. good job!"
