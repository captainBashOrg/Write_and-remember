
print( "Записать и запомнить")

def custom_write(file_name, strings):
    file = open(file_name, 'w', encoding="utf-8")
    file_poz = file.tell()


    strings_positions = {} # Создаём пустой словарь

    #keys = () # Создаём переменную под пустой кортеж

    num_str = 0
    for s in strings:
        file_poz = file.tell()
        #print(file_poz, s)
        file.write(s + '\n')
        keys = (num_str, file_poz)

        strings_positions[keys] = s

        num_str +=1

    file.close()
    return strings_positions






#void main(void)



info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!',
    'Tell me, why, why, why...'
    ]

result = custom_write('test.txt', info)
for elem in result.items():
  print(elem)



