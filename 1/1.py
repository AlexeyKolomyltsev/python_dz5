import os

def del_word(word):
    path ='1'+ os.sep + 'file.txt'
    with open(path, 'r+', encoding='utf-8') as read_file:
        stroka = read_file.readline().split()
        stroka = " ".join(filter(lambda x: word not in x, stroka))
        read_file.write("\n"+stroka)
del_word("абв")   
