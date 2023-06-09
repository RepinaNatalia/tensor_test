# Дан текстовый файл test_file/task1_data.txt
# Он содержит текст, в словах которого есть цифры.
# Необходимо удалить все цифры и записать получившийся текст в файл test_file/task1_answer.txt


# Здесь пишем код

# Ниже НИЧЕГО НЕ НАДО ИЗМЕНЯТЬ
f = open("test_file/task1_data.txt", 'r', encoding='utf-8')
d = f.readlines()
i = 0
s = []
for i in range (len(d)):
    a = d[i]
    j = 0
    f =""
    for j in range(len(d[i])):
        if d[i][j].isdigit() == False:
           f += d[i][j]
        else:
            f += ""
    s += f
poem = ''.join(s)
file = open("test_file/task1_answer.txt", "w", encoding='utf-8')
file.write(poem)
file.close()

with open("test_file/task1_answer.txt", 'r', encoding='utf-8') as file1:
    with open("test_file/task1_ethalon.txt", 'r', encoding='utf-8') as file2:
        answer = file1.readlines()
        ethalon = file2.readlines()
        assert answer == ethalon, "Файл ответа не совпадает с эталонном"
print('Всё ок')
