def bruh(num, li):
    lic = li[:]
    for a in lic:
        if num%a == 0:
            num/=a
            lic.remove(a)
            if num/a in li:
                return 1
            li.append(num//a)
            
    return num
seen = []
res = 1
for b in range(1,21):
    res*= bruh(b,seen)
    print(f"b = {b}, bruh =",bruh(b,seen),f", seen={seen}")
    seen.append(b)
print(res)