def check_palin(num):
    if list(str(num)) == list(str(num))[::-1]:
        return True

def check_3d(num):
    for a in range(100,1000):
        if num%a == 0 and len(str(num//a)) == 3:
            return True

        
for b in range(999999,10000,-1):
    if check_palin(b):
        if check_3d(b):
            print(b)
            break
    else:
        continue