from os import system
from process_data import clearScr, generate_table, get_data_from_file, write_to_file
import os
MAIN_MENU = "=====================\n0. Закрыть программу\n1. Показать выходную таблицу\n2. Показать цены и названия\n3. Показать рыночные цены\n4. Записать в файл\n====================="
while True:
    print(MAIN_MENU)
    choice:int = int(input("Введите номер команды: "))
    if choice == 0:
        exit()
    elif choice == 1:
        print(generate_table())
        clearScr()
    elif choice == 2:
        print(get_data_from_file('handbook.txt', 'handbook'))
        clearScr()
    elif choice == 3:
        print(get_data_from_file('prices.txt', 'prices'))
        clearScr()
    elif choice == 4:
        choice_2 = int(input("1. Записать выходную\n2. Записать коды и название\n3. Записать рыночные цены\n"))
        if not choice_2:
            print("Error")
            clearScr()
        else:
            if choice_2 == 1:
                write_to_file(generate_table(), 'out.txt')
                clearScr()
            elif choice_2 == 2:
                write_to_file(get_data_from_file('handbook.txt', 'handbook'), 'handbookOut.txt')
                clearScr()
            elif choice_2 == 3:
                write_to_file(get_data_from_file('prices.txt', 'prices'), 'pricesOut.txt')
                clearScr()
