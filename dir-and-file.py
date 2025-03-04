import sys
import os

#ex1
dir = []
fil = []
path = input()
for i in os.listdir(path):
    if os.path.isdir(os.path.join(path, i)):
        dir.append(i)
for i in os.listdir(path):
    if os.path.isfile(os.path.join(path, i)):
        fil.append(i)
print(dir)
print(fil)


#ex2
path = input()
access = {
        'exist': os.path.exists(path),
        'read': os.access(path, os.R_OK),
        'write': os.access(path, os.W_OK),
        'exec': os.access(path, os.X_OK)
    }

if access['exist'] and access['read'] and access['write'] and access['exec']:
    print("Full access")

#ex3
    path = input()
if os.path.exists(path):
    print(os.path.basename(path), os.path.dirname(path))
    
#ex4
    l =0
with open('text.txt', 'r') as file:
    for line in file:
        l += 1    
print(l)

#ex5
l = list(map(int, input().split()))
with open('text.txt', 'w') as file:
    for i in l:
        file.write(str(i)+ "\n")

#ex6
alpha = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
for i in alpha:
    f = i + ".txt"
    with open(f, 'w') as file:
        file.write("hello")

#ex7
with open("A.txt", 'r') as src, open("text.txt", 'w') as dest:
    dest.write(src.read())

#ex8
path = input()
access = {
        'exist': os.path.exists(path),
        'read': os.access(path, os.R_OK),
        'write': os.access(path, os.W_OK),
        'exec': os.access(path, os.X_OK)
    }

if access['exist'] and access['read'] and access['write'] and access['exec']:
    print("Full access")
os.remove(path)