# Создайте программу для игры в ""Крестики-нолики""

import random
import os

def print_array(table):
    os.system('cls')
    for i in range(1, 10):
        print(f"{table[i - 1]} ", end="")
        if not i%3: print()

def zapolnenie(array, array_iskl, flag):
    x = int(input("Выберете клетку: "))
    if x in array_iskl:
        for i in range(len(array)):
            if array[i] == x:
                # array[i] = 'ppp'
                if flag: array[i] = "X"
                else: array[i] = "O"
        array_iskl.remove(x)
    else:
        print("Такой клетки нет, либо она занята")
        zapolnenie(array, array_iskl, flag)
        

def win_game(array, flag):
    if (array[0] == array[1] == array[2] or
     array[3] == array[4] == array[5] or
     array[6] == array[7] == array[8] or
     array[0] == array[3] == array[6] or
     array[1] == array[4] == array[7] or
     array[2] == array[5] == array[8] or
     array[0] == array[4] == array[8] or
     array[2] == array[4] == array[6]) :
        return True
    else:
        return False
        

def igra(array, array_iskl, flag):
    print_array(array)
    if array_iskl == []:
        print("Никто не выиграл")
        return
    
    if flag:
        print("Ходит первый игрок")
        igrok = "первый"
    else: 
        print("Ходит второй игрок")
        igrok = 'второй'

    
    zapolnenie(array, array_iskl, flag)
    if win_game(array, flag):
        print_array(array)
        print(f"Выиграл {igrok} игрок \n ИГРА ЗАВЕРШЕНА")
        return
    igra(array, array_iskl, not flag)

table = [int(i) for i in range(1, 10)]
table_iskl = [int(i) for i in range(1, 10)]

flag =random.randint(0,1)
igra(table, table_iskl, flag)