def count_words(text):
    words= text.split()
    return len(words)
def count_char(text):
    char= dict()
    text= text.lower()
    text= text.replace('\n', '')
    text= text.replace(' ','')
    for c in text:
        if char.get(c)==None:
            char.update({f"{c}": 1})
        else:
            count= char[c] + 1
            char.update({f"{c}": count})
    return char
def dict_to_list(dict):
    list=[]
    for key, value in dict.items():
        list.append({"char": key, "num": value})
    return list