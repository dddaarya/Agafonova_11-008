import pickle
import datetime

with open('./data.pickle','rb') as file:
    data = pickle.load(file)


def func1(data):
    datadict = dict()
    for item in data:

        sp_item = item['body'].split(' ')
        for w in sp_item:

            if len(w) > 5:

                try:
                    datadict[w] += 1
                except:
                    datadict[w] = 0

    values_list = list(datadict.values())
    keys_list = list(datadict.keys())
    max_num = 0
    word_list = []
    for i in range(10):
        for j in range(len(values_list)):
            if values_list[j] > max_num:
                max_num = values_list[j]
        word_list.append(keys_list[j])
        values_list.pop(j)
            
    return word_list

def get_len(message):
        return len(message['body'])

def func2(data):
    

    len_list = list( map(get_len, data) )

    return sum(len_list) / len(data)

def func3(data:list):
    comment_list = []
    autor_list = []
    max_num = 0
    
    for j in range(10):
        for mes in range(len(data)):
            if data[mes]['edited'] == False and data[mes]['score'] > max_num: 
                max_num = data[mes]['score']
                autor = data[mes]['author']
                text = data[mes]['body']
                ind = mes
        autor_list.append(autor)
        comment_list.append(text)
        max_num = 0
        data.pop(ind)
    return (comment_list, autor_list)
        
def func4(data):
    comment_list = []
    min_num = data[0]['score']
    for j in range(10):
        for mes in range(len(data)):

            if data[mes]['score'] < min_num:

                min_num = data[mes]['score']
                comment = data[mes]['body']
                ind = mes

        comment_list.append(comment)
        
        min_num = data[0]['score']
        data.pop(ind)

    return comment_list

def func5(data , word ):
    word = word.upper()
    cont = 0

    for mes in data:
        up_mes = mes['body'].upper()
        if word in up_mes:
            cont += 1

    return cont / len(data)

def func_alt(data):
    sub_dict = dict()
    for mes in data:
        subreddit = mes['subreddit']
        try:
            sub_dict[subreddit] += 1
        except:
            sub_dict[subreddit] = 1
                
    return sub_dict



func_alt(data)
