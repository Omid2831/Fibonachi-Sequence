# 0,1,1,2,3,5,8,13,21,34

Number_of_nth_terms = int(input("Enter how many nth terms: "))

Sequence = []
a = 1
b = 1
n = 1
Sequence.append(0)
Sequence.append(b)
for i in range (1,Number_of_nth_terms - 1):
    Sequence.append(n)
    n = a + b
    a = b
    b = n

print (Sequence)

nth_term =  int(input("Enter the nth term: "))

a = 1
b = 1
n = 1
for i in range (1,nth_term-1):
    n = a + b
    a = b
    b = n
    if (nth_term == (i+3)):
        print (n)
