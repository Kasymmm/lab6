import math
import time

#ex1
numb = list(map(int, input().split()))
print(math.prod(numb))

#ex2
s = input()
u=0
l=0
for char in s:
    if char.isupper():
        u+=1
for char in s:
    if char.islower():
        l+=1
print("uppers: ",u)
print("lowers: ",l)

#ex3
s = input()
def pal(s):
    for i in s:
        d = ''.join(i.lower())
    return d == d[::-1]
if pal(s):
    print("palindrom")
else:
   print("not palindrom") 

#ex4
msec = int(input())
a = int(input())
print(f"Square root of {a} after {msec} milliseconds is {math.sqrt(a)}")

#ex5
t1 = (True, True, True)
t2 = (True, False, False)

if all(t1):
    print("t1 - True")
else:
    print("t1 - False")

if all(t2):
    print("t2 - True")
else:
    print("t2 - False")