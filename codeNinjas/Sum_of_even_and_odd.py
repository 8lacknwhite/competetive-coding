x = list(map(int,str(input())))
a =0
b= 0
digit = 0
i = 0
while i < len(x):
    digit = x[i]
    if digit%2 == 0:
        a += digit
    else:
        b += digit
    i+=1
print(a, " ", b)
