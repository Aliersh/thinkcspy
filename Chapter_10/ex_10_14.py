'''Write a function replace(s, old, new) that replaces all occurences of old with new in a string s:
test(replace('Mississippi', 'i', 'I'), 'MIssIssIppI')

s = 'I love spom!  Spom is my favorite food.  Spom, spom, spom, yum!','o','a'

test(replace(s, 'om', 'am'),
       'I love spam!  Spam is my favorite food.  Spam, spam, spam, yum!')

test(replace(s, 'o', 'a'),
       'I lave spam!  Spam is my favarite faad.  Spam, spam, spam, yum!')

Hint: use the split and join methods.'''

    def replace(s, old, new):
        slist = s.split()
        nlist = []
        for word in slist:
            if old in word:
                nword = word.replace(old,new)
                nlist.append(nword)
            else:
                nlist.append(word)
        nstr = ' '.join(nlist)
        return nstr

print(replace('I love spom!  Spom is my favorite food.  Spom, spom, spom, yum!','om','am'))