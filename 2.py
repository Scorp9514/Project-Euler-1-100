a = 1
b = 2
even_sum = 0
while a+b < 4000000:
    dummy = b
    #print(f"{a+b}")
    if (a+b) %2 == 0:
        even_sum+=(a+b)
    b = a+b
    a = dummy
print(even_sum+2)