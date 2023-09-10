#!/usr/bin/env python3

def return_evens(num_list):

    nums = [num for num in num_list if num % 2 == 0]
    return nums

def make_exclamation(sentence_list):
    strings = [str + "!" for str in sentence_list]
    return strings