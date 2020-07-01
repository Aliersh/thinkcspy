'''Count how many words in a list have length 5.'''

def countWords(lst):
    count = 0
    for word in lst:
        if len(word) == 5:
            count += 1
    return count