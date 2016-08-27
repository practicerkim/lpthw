#-*-encoding:utf-8-*-
from sys import exit

def gold_room():
    print "this room is full of gold. how much do you take?"
    new_next = []

    while True:
        next = raw_input('> ')
        for i in next:
            if not "0" <= i <= "9":
                gold_room()
                #break
            else:
                new_next.append(i)

        new_next = ''.join(new_next)    # 리스트를 문자열로 바꾸는 명령어

        if next == new_next:
            if int(next) < 50:
                print "nice, you're not greedy, you win!"
                exit()
            else:
                print "you greedy bastard!"
                exit()

gold_room()
