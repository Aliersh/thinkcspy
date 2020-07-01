'''Count how many words occur in a list up to and including the first occurrence of the word “sam”.'''

def count(lst):
    count = 0
    index = 0
    while index < len(lst) and lst[index] != 'sam':
        count += 1
        index += 1
    return count