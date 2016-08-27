#-*-encoding:utf-8-*-
from sys import exit

def gold_room():
    print "this room is full of gold. how much do you take?"

    next = raw_input('> ')
    if "a" <= next <= "z" or "A" <= next <= "Z" in next:
        dead("man, learn to type a number.")
    elif int(next) < 50:
        print "nice, you're not greedy, you win!"
        exit()
    else:
        dead("you greedy bastard!")

def dead(why):
    print why, "good job!"
    exit(0)
gold_room()
