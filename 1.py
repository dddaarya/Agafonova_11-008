mydict = {2:9, 5:-3, 3:12, 7:3, 4:20, 1:9, 6:9, 11:3, 13:6}


n = int(input())
new_dict = {}
keys = mydict.keys()
for i in range(n):
    if i in keys:
        new_dict[i] = mydict[i]
    else:
        new_dict[i] = '!!'


print(new_dict)
