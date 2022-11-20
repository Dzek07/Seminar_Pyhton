from random import randint


def draw_board(board):
   print("-" * 13)
   for i in range(3):
      print("|", board[0+i*3], "|", board[1+i*3], "|", board[2+i*3], "|")
      print("-" * 13)

def take_input(player_move):
   while True:
      player_answer = input("Куда поставим " + player_move+"? ")
      try:
         player_answer = int(player_answer)
      except:
         print("Некорректный ввод. Вы уверены, что ввели число?")
         continue
      if player_answer >= 1 and player_answer <= 9:
         if(str(board[player_answer-1]) not in "XO"):
            board[player_answer-1] = player_move
            break
         else:
            print("Эта клетка уже занята!")
      else:
        print("Некорректный ввод. Введите число от 1 до 9.")

def ii(move):
    while True:
        answer = int(randint(1, 9))
        if(str(board[answer-1]) not in "XO"):
            board[answer-1] = move
            print("ИИ сделал ход")
            break


def check_win(board):
   win_coord = ((0,1,2), (3,4,5), (6,7,8), (0,3,6), (1,4,7), (2,5,8), (0,4,8), (2,4,6))
   for each in win_coord:
       if board[each[0]] == board[each[1]] == board[each[2]]:
          return board[each[0]]
   return False

def main(board, counter):
   if counter == 1:
      corrected = 1
   corrected = 0
   win = False
   while not win:
      draw_board(board)
      if counter % 2 == 0:
         take_input("X")
      else:
         ii("O")
      counter += 1
      if counter > 4:
         tmp = check_win(board)
         if tmp:
            print(tmp, "выиграл!")
            win = True
            break
      if counter == 9 + corrected:
         print("Ничья!")
         break
   draw_board(board)

print("Игра Крестики-нолики")
board = list(range(1,10))
counter = randint(0, 1)
main(board,counter)

