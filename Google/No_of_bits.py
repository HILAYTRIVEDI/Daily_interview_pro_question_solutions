def one_bits(num):
    count = 0
    while(num > 0):
        if(num % 2 == 1):
            count += 1
            num = int(num/2)
        elif(num % 2 == 0):
            count += 1
            break
        else:
            continue
    return count


print(one_bits(7))
