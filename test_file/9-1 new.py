# Дан текстовый файл test_file/task1_data.txt
# Он содержит текст, в словах которого есть цифры.
# Необходимо удалить все цифры и записать получившийся текст в файл test_file/task1_answer.txt


# Здесь пишем код

# Ниже НИЧЕГО НЕ НАДО ИЗМЕНЯТЬ
f = open("test_file/task1_data.txt", 'r', encoding='utf-8')
d = f.readlines()
#print(*f)
#print(d)
i = 0
s = []
for i in range (len(d)):
    a = d[i]
    a0 = a.replace('0', '')
    a1 = a0.replace('1', '')
    a2 = a1.replace('2', '')
    a3 = a2.replace('3', '')
    a4 = a3.replace('4', '')
    a5 = a4.replace('5', '')
    a6 = a5.replace('6', '')
    a7 = a6.replace('7', '')
    a8 = a7.replace('8', '')
    a9 = a8.replace('9', '')
    i += 1
    s += a9
#print(s)
w = ''.join(s)
#print(w)

with open("test_file/task1_answer.txt", 'r', encoding='utf-8') as file1:
    with open("test_file/task1_ethalon.txt", 'r', encoding='utf-8') as file2:
        answer = file1.readlines()
        ethalon = file2.readlines()
        assert answer == ethalon, "Файл ответа не совпадает с эталонном"
print('Всё ок')