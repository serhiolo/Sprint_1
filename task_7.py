def digit_root(num):
    while num >= 10:
        total = 0
        for i in str(num):
            total += int(i)
        num = total
        
    return num