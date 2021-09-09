import re

filenames = ['./9_ABC.csv','./3_ABC.csv','./4_ABC.csv','./8_ABC.csv']

mobile = './mobiles'

patern = r'(\d{3})'
patern_2 = r'\d{7}'

list_of_phones = []

with open(mobile, 'r', encoding='utf8') as file:
    for phone in file:
        match = int(re.search(patern,phone)[0])
        match_2 = int(re.search(patern_2, phone)[0])
        gg = True
        for file_n in filenames:
            with open(file_n, 'r', encoding='utf8') as f:
                _ = f.readline()
                for line in f:
                    string = line.split(';')
                    if match == int(string[0]):
                        if match_2 > int(string[1]) and match_2 < int(string[2]):
                            list_of_phones.append((phone, string[-1]))
                            gg = False
                            break
                    else:
                        continue
            if not gg:
                break
with open(mobile, 'r', encoding='utf8') as f:
    for phone in f:
        gen = (item[0] for item in list_of_phones)
        if phone not in gen:
            list_of_phones.append((phone, 'номер не опознан'))

print(len(list_of_phones))
