#Создаём функцию, шифрующую текст
#Параметры функции: алфавит(язык), исходный текст, ключ, количество символов в алфавите
def cesar(alph, txt, key, cnt_char):

    punctuation_marks = '.,!?:;()-'
    #Инициализируем пустую строку с зашифрованным текстом и пустой словарь
    new_txt = ''
    d = {}

    #Наполняем словарь символами алфавита, индексируя их
    for i in range(cnt_char):
        d.setdefault(i,alph[i])

    #Начинаем шифровать текст
    for i in range(len(txt)):
        
        #Проверяем символ на пробел, знаки препинания и перевод строки
        if txt[i] == " ":
            i -= 1
            new_txt += " "
            
        elif txt[i] in punctuation_marks:
            i -= 1
            new_txt += txt[i]
        elif txt[i] == "\n":
            i += 1
            new_txt += '\n'
        else:
            char = txt[i]
            #Проверяем, больше ли сумма (ключ + индекс символа) количества букв в алфавите
            if alph.index(char)+key > (cnt_char - 1):
                #Если больше, то символ шифруется символом из начала алфавита
                new_txt += d.get((alph.index(char) + key) - cnt_char)
            else:
                new_txt += d.get(alph.index(char)+key)
            
    return new_txt

#Инициализация алфавитов кириллицы и латиницы
alph_ru = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"
alph_eng = "abcdefghijklmnopqrstuvwxyz"
file_name = input("Введите название файла(без расширения): ")
file_name_without_txt = file_name
file_name += '.txt'

f = open(file_name, 'r', encoding='UTF-8')
txt = f.read()
txt = txt.lower()
f.close()

# Проверка, к какому алфавиту относится первая буква текста
for i in range(len(txt)):
    if (txt[i] in alph_ru) or (txt[i] in alph_eng):
        break
print(txt[i])

if txt[i] in alph_ru:
    cnt_char = len(alph_ru)
    key = int(input("Введите ключ: "))
    f_new = open(file_name_without_txt + '_encoding.txt', 'w', encoding='UTF-8')
    f_new.write(cesar(alph_ru, txt, key, cnt_char))
    f_new.close()
    print("Зашифрованный текст: ", cesar(alph_ru, txt, key, cnt_char))
    
elif txt[i] in alph_eng:
    cnt_char = len(alph_eng)
    key = int(input("Введите ключ: "))
    f_new = open(file_name_without_txt + '_encoding.txt', 'w', encoding='UTF-8')
    f_new.write(cesar(alph_eng, txt, key, cnt_char))
    f_new.close()
    print("Зашифрованный текст: ", cesar(alph_eng, txt, key, cnt_char))
