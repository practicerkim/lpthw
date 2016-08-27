# -*- coding: utf-8 -*-
def break_words(stuff):
    """This function will break up words for us."""
    words = stuff.split(' ')
    return words
#word를 반환하여 다른 함수에서 사용할 수 있도록 하겠다.
# print words만 입력하면 words를 매개변수로 받는 함수에서 사용할 수가 없다.
def sort_words(words):
    """Sorts the words."""
    return sorted(words)

def print_first_word(words):
    """Prints the first word after popping it off."""
    word = words.pop(0)
    print word

def print_last_word(words):
    """Prints the last word after popping it off."""
    word = words.pop(- 1)
    print word

def sort_sentence(sentence):
    """Takes in a full sentence and returns the sorted words."""
    words = break_words(sentence)
    return sort_words(words)

def print_first_and_last(sentence):
    """Prints the first and last words of the sentence."""
    words = break_words(sentence)
    print_first_word(words)
    print_last_word(words)

def print_first_and_last_sorted(sentence):
    """Sorts the words then prints the first and last one."""
    words = sort_sentence(sentence)
    print_first_word(words)
    print_last_word(words)


sample = "all good things come to those who wait."
a = break_words(sample)
print a
print '\n'
print_first_word(a)
print a
print '\n'
print_last_word(a)
print a
print '\n'
b = sort_words(a)
print b
print '\n'

print break_words(sample)
print_first_and_last(sample)
print '\n'

print sort_sentence(sample)
print_first_and_last_sorted(sample)
