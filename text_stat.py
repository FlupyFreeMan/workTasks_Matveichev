def text_stat(filename):
    try: 
        file = open(filename,'r',encoding='utf-8')
    except FileNotFoundError:
        return {'error': "Файл не найден, проверьте правильность пути"}
    except TypeError:
        return {'error': f"Ошибка типа данных аргумента 'filename'. Введен аргумент типа {type(filename)}, а ожидается {str}"}
    except ValueError:
        return {'error': f"Ошибка введенного аргумента. Значение аргумента равно {filename}. Необходимо ввести арумент в формате \"filename.txt\""}
    except OSError:
        return {'error': "Ошибка введенных данных"}
    else:
        abc1 ={}
        for i in map(chr,range(ord('а'),ord('я')+1)): # создание словаря с кирилицей и добавление туда буквы ё
            abc1[i] = (0,0)
            if i == 'е': abc1['ё'] = (0,0) # добавление "ё"
        abc1 = dict(abc1)
        abc3 = {i: (0,0) for i in map(chr,range(ord('a'),ord('z')+1))} # создание словаря с латиницей
        abc1 = dict(list(abc1.items()) +  list(abc3.items())) # создание словаря с остальными элементами
        cont = {
            'word_amount': 0,
            'paragraph_amount': 0,
            'bilingual_word_amount': 0
        }
        texts = file.read()
        file.close()
        texts = texts.lower() #Заменяем заглавные буквы на прописные, тк не было условий с ними, то я считаю все буквы как прописные
        all_letters = 0 #счетчик букв в тексте
        buffer_num_letters = (0,0) #счетчик букв для поиска слов состоящих из алфавита кирилицы и латиницы одновременно
        cont['paragraph_amount']+=len(texts.split("\n")) #Подсчет количества абзацев
        for i,pr in enumerate(texts.split("\n")): #Абзацы
            cont['word_amount'] += len(pr.split()) - list(pr.split()).count('-') #Подсчет количества слов
            for j, st in enumerate(pr.split()): #Слова в абзацах
                for k, char in enumerate(st): 
                    if char in list(abc1.keys())[0:32]: buffer_num_letters = (buffer_num_letters[0]+1, buffer_num_letters[1]) #подсчет кирилицы в слове
                    if char in list(abc1.keys())[33:]: buffer_num_letters = (buffer_num_letters[0], buffer_num_letters[1]+1) #подсчет латиницы в слове
                    if char in list(abc1.keys()): abc1[char]=(abc1[char][0]+1, abc1[char][1]) # Подсчет букв в словах (с повторениями)
                    if char in abc1.keys(): all_letters+=1 #подсчет количества всех букв
                for k, char in enumerate(list(set(st))):
                    if char in list(abc1.keys()): abc1[char]=(abc1[char][0], abc1[char][1]+1)# Подсчет букв в словах (повторные вхождения не учитываются)
                if buffer_num_letters[0] > 0 and buffer_num_letters[1] > 0: cont['bilingual_word_amount'] += 1 #условие увеличение счетчика если будет в одном слове и латиница и кирилица
                buffer_num_letters = (0,0)
        result_abc = {}
        for i in (abc1.items()):
            result_abc[i[0]] = (round(float(i[1][0]/all_letters),6), round(float(i[1][1]/cont['word_amount']),6)) #преобразование подсчитаного количества букв в частоты использования букв(количество определенных букв/количество всех букв) и доли слов(число слов с определенной буквой/количество слов)
        return dict(list(result_abc.items())+ list(cont.items()))

# print(text_stat(int(1222)))
for i in text_stat("text_kiril.txt").items(): #вывод
    print(i)