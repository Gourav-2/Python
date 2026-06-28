'''

Use a while loop to reverse a given number (e.g., 123 → 321).'''


num=123
rew=0
while num!=0:
    last_digit=num%10
    num=num//10
    rew=(rew*10)+last_digit

print(rew)