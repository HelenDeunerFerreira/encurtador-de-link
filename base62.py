from math import floor

def toBase(num, b = 62):
    if b <= 0 or b > 62:
        return 0
    base = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ';
    r = num % b
    res = base[r];
    q = floor(num / b)
    while q:
        r = q % b
        q = floor(q / b)
        res = base[int(r)] + res
    return res

def to10(num, b = 62):
    base = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ';
    limit = len(num)
    res = 0;
    for i in range(limit):
        res = b * res + base.find(num[i])
    return res
