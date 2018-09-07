"""
stringjumble.py
Author: Emma Dunbar
Credit: stackoverflow.com(spliting, and joining),quora.com(reversing)

Assignment:

The purpose of this challenge is to gain proficiency with 
manipulating lists.

Write and submit a Python program that accepts a string from 
the user and prints it back in three different ways:

* With all letters in reverse.
* With words in reverse order, but letters within each word in 
  the correct order.
* With all words in correct order, but letters reversed within 
  the words.

Output of your program should look like this:

Please enter a string of text (the bigger the better): There are a few techniques or tricks that you may find handy
You entered "There are a few techniques or tricks that you may find handy". Now jumble it:
ydnah dnif yam uoy taht skcirt ro seuqinhcet wef a era erehT
handy find may you that tricks or techniques few a are There
erehT era a wef seuqinhcet ro skcirt taht uoy yam dnif ydnah
"""
s=input("Please enter a string of text (the bigger the better): ")
print('You entered "' + s + '". Now jumble it:')
list0=list(s)
list0.reverse()
list2="".join(list0)
print(list2)
list3 = s.split(" ")
list3.reverse()
list4=" ".join(list3)
print(list4)
list5 = s.split(" ")
for word in list5:
    word1=list(word)
    word1.reverse()
    word2="".join(word1)
    print(word2, end=" ")