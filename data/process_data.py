import os

def arrayFromFile(file):
    return open(file, 'r', encoding='utf-8').readlines()

def clearScr():
    inp = input("Press enter to continue")
    os.system('cls')

name_dict = {}
for line in arrayFromFile('handbook.txt'):
    data = line.replace('\n', '').split(',')
    name_dict[f'{data[0]}'] = f'{data[1]}'

def get_data_from_file(file, type):
    array = arrayFromFile(file)
    lines = ''
    fromCode = int(input("С какого кода? "))
    toCode = int(input("По какой код? "))
    for line in array:
        data = line.replace('\n','').split(',')
        if int(data[0]) in range(fromCode, toCode+1):
            if type == "prices":
                lines = lines + f"Код: {data[0]:3} | Цена 2007: {data[1]:5} | Цена 2008: {data[2]:5} | Цена 2009: {data[3]:5} | Цена 2017: {data[4]:5} | Рынок: {data[-1]:14}\n"
            elif type == "handbook":
                lines = lines + f'Код: {data[0]:3} | Тип товара: {data[-1]:10}\n'
    return lines

def generate_table():
    array = arrayFromFile('prices.txt')
    lines = ''
    fromCode = int(input("С какого кода? "))
    toCode = int(input("По какой код? "))
    for line in array:
        data = line.replace('\n', '').split(',')
        if int(data[0]) in range(fromCode, toCode+1):
            lines = lines + f"""Рынок: {data[-1]:14} | Товар: {name_dict.get(data[0]):9} | Цена 2007: {data[1]:3} | 2008 грн+: {str(float(data[2])-float(data[1]))[:5]:3} | {str(float(data[2])/float(data[1]) * 100)[:5]:3}% | 2011 год+: {str(float(data[3])-float(data[2]))[:5]:3} | {str( float(data[3])/float(data[2]) * 100)[:5]:3}% | 2017 год+: {str(float(data[4])-float(data[3]))[:5]:3} | {str(float(data[4])/float(data[3]) * 100)[:5]:3}%\n"""
    return lines

def write_to_file(data, path):
    with open(path, 'w+', encoding='utf-8') as myFile:
        myFile.write(data)
    myFile.close()
