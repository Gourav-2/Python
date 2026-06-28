'''
Write a program that counts how many vowels are in a given string
'''

text="hello"
vowel=["a","i","o","u","e"]
count=0
for i in text:
    if(i in vowel):
        count+=1

print(count)
