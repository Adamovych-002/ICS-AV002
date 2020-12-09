codesFile = open("codes.txt", "r", encoding="utf-8")
codesBase = codesFile.readlines()
codesFile.close()


baseFile = open("base.txt", 'r', encoding="utf-8")
baseBase = baseFile.readlines()
baseFile.close()

codesDict = {}
for code in codesBase:
    data = code.replace('\n','').split(';')
    codesDict[f'{data[0]}'] = data[1]


def newProductLine(data, criterion=None, value=None):
    myData = data.replace(',','.').replace('\n','').split(';')
    if not criterion and not value:
        return f'Рынок: {myData[-1]}\nТовар: {codesDict.get(myData[0])}\nЦена 2007 года: {myData[1][:5]}\n2008 грн+: {str(float(myData[2])-float(myData[1]))[:4]}\n{str(float(myData[2])/float(myData[1]) * 100)[:4]}%\n2011 год+: {str(float(myData[3])-float(myData[2]))[:5]}\n{str( float(myData[3])/float(myData[2]) * 100)[:5]}%\n2017 год+: {str(float(myData[4])-float(myData[3]))[:5]}\n{str(float(myData[4])/float(myData[3]) * 100)[:5]}%\n\n'
    elif criterion == "code":
        if myData[0] == value:
            return f'Рынок: {myData[-1]}\nТовар: {codesDict.get(myData[0])}\nЦена 2007 года: {myData[1][:5]}\n2008 грн+: {str(float(myData[2])-float(myData[1]))[:4]}\n{str(float(myData[2])/float(myData[1]) * 100)[:4]}%\n2011 год+: {str(float(myData[3])-float(myData[2]))[:5]}\n{str( float(myData[3])/float(myData[2]) * 100)[:5]}%\n2017 год+: {str(float(myData[4])-float(myData[3]))[:5]}\n{str(float(myData[4])/float(myData[3]) * 100)[:5]}%\n\n'
    elif criterion == "place":
        if myData[-1] == value:
            return f'Рынок: {myData[-1]}\nТовар: {codesDict.get(myData[0])}\nЦена 2007 года: {myData[1][:5]}\n2008 грн+: {str(float(myData[2])-float(myData[1]))[:4]}\n{str(float(myData[2])/float(myData[1]) * 100)[:4]}%\n2011 год+: {str(float(myData[3])-float(myData[2]))[:5]}\n{str( float(myData[3])/float(myData[2]) * 100)[:5]}%\n2017 год+: {str(float(myData[4])-float(myData[3]))[:5]}\n{str(float(myData[4])/float(myData[3]) * 100)[:5]}%\n\n'
    return "Not found"

with open('outbase.txt', 'w+', encoding="utf-8") as myFile:
    question = input("Поиск по критериям? (y/n) ")
    if question == 'y':
        crit = input("Фильтр по: (code/place) ")
        value = input("Введите значение: ")
        for event in baseBase:
            writeData = newProductLine(event, crit, value)
            myFile.write(writeData)
    else:
        print("- - Полная запись - -")
        for event in baseBase:
            writeData = newProductLine(event)
            myFile.write(writeData)
