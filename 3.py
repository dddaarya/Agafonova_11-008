def summirize(num):
    st = str(num)
    summ = 0
    for i in st:
        summ += int(i)
    if summ > 9:
        return summirize(summ)
    else:
        return summ

print(summirize(555))
