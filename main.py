a = int(input('Enter a number : '))
l = []
l.append(a)
while a !="":
    a = input("Enter a number : ")
    if a !="":
        a = int(a)
        l.append(a)

print(l)
b = int(input("Press 1 to interchange first and last elements in a list\nPress 2 to find sum of elements in a list\nPress 3 to find the smallest number in a list\nPress 4 to find the largest number in the list\nPress 5 to print even numbers in a list\nPress 6 to print odd numbers in a list\n:"))

print(b)

if b ==1:
    l[0], l[-1] = l[-1], l[0]
    print(l)

if b ==2:
    sum = 0
    for i in l:
        sum = sum + i
    print(sum)

if b ==3:
    l.sort()
    sml = l[0]
    print(sml)

if b==4:
    l.sort()
    lgt = l[-1]
    print(lgt)
if b ==5:
    l.sort()
    evn = []
    for i in l:
        if i%2 == 0:
            evn.append(i)
    print(evn)
if b ==6:
    l.sort()
    oddd = []
    for i in l:
        if i%2 !=0:
            oddd.append(i)
    print(oddd)
