# Создайте программу для игры в "Крестики-нолики"

# Если честно, я посмотрела несколько исполнений игры в гугле, выбрала самое понятное мне,  проработала и сократила его. 

# Вводим функцию, которая рисует игровую доску
def draw_board(board):
    print("-" * 13)
    for i in range(3):
        print("|", board[0 + i * 3], "|", board[1 + i * 3], "|", board[2 + i * 3], "|")
        print("-" * 13)

# Функция, позволяющая сделать ход игрокам и проверить его корректность
def take_input(smb):
    while True:
        player_answer = input("Выберите поле, куда поставить " + smb + "? ")
        if not (player_answer in "123456789"):
            print("Некорректный ввод. Повторите: ")
            continue
        player_answer = int(player_answer)
        if str(board[player_answer - 1]) in "XO":
            print("Эта клетка уже занята!")
            continue
        board[player_answer - 1] = smb     # записываем в выбранную ячейку нужный символ
        break
                
# Функция проверки выигрышного положения
def check_win(board):
    win_coord = (
        (0, 1, 2),
        (3, 4, 5),
        (6, 7, 8),
        (0, 3, 6),
        (1, 4, 7),
        (2, 5, 8),
        (0, 4, 8),
        (2, 4, 6),
    )
    for each in win_coord:
        if board[each[0]] == board[each[1]] == board[each[2]]:  # совпадение символов в каждой из выигрышных комбинаций
            return board[each[0]]
    else:
        return False

board = list(range(1, 10))

count = 0
while True:
    draw_board(board)
    if count % 2 == 0:
        take_input("X")
    else:
        take_input("O")
    count += 1
    if count > 3:
        winner = check_win(board)
        if winner:
            print(winner, "выиграл!")
            break
    if count == 9:
        print("Ничья!")
        break