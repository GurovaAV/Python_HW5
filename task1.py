# Напишите программу, удаляющую из текста все слова, содержащие "абв"

path = 'task1_text.txt'
data = open (path, 'r', encoding = 'utf-8')
text = ""
for line in data:
    text = line
data.close

text_spltd = text.split()
findme = 'абв'

with open ('task1_out.txt', 'w', encoding = 'utf-8') as f:
    f.write(str(' '.join(list(filter(lambda word: findme not in word, text_spltd)))))
