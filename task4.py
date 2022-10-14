# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных

def rle_encoding(data):
        encoding = ""
        prev_char = ""
        count = 1

        for char in data:
            if char != prev_char:
                if prev_char: encoding += str(count) + prev_char
                count = 1
                prev_char = char
            else:
                count += 1
        else:
            encoding += str(count) + prev_char
            return encoding

def rle_decoding(data):
    decoding = ""
    count = ""
    for char in data:
        if char.isdigit():
            count += char
        else:
            decoding += char * int(count)
            count = ""
    return decoding

choice = int(input("Выберите, что вы хотите сделать с данными: сжать (1) или восстановить (2): "))

if choice == 1:
    path = 'task4_text_cmprssn.txt'
    data = open (path, 'r', encoding = 'utf-8')
    text = None
    for line in data:
        text = line
        print(text)
    data.close

    print(rle_encoding(text))

    with open ('task4_text_rcvr.txt', 'w', encoding = 'utf-8') as f:
        f.write(str(rle_encoding(text)))
else:
    path = 'task4_text_rcvr.txt'
    data = open (path, 'r', encoding = 'utf-8')
    text = None
    for line in data:
        text = line
        print(text)
    data.close

print(rle_decoding(text))

with open ('task4_text_cmprssn.txt', 'w', encoding = 'utf-8') as f:
    f.write(str(rle_decoding(text)))

