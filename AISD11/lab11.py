class Board:
   def draw_board(self,board,n):
      if n==3:
         print("-" * 13)
         for i in range(3):
            print("|", board[0+i*3], "|", board[1+i*3], "|", board[2+i*3], "|")
            print("-" * 13)
      elif n==4:
         print("-" * 17)
         for i in range(4):
            print("|", board[0+i*4], "|", board[1+i*4], "|", board[2+i*4], "|",board[3+i*4], "|")
            print("-" * 17)
      elif n==5:
         print("-" * 20)
         for i in range(5):
            print("|", board[0+i*5], "|", board[1+i*5], "|", board[2+i*5], "|", board[3+i*5],  "|",board[4+i*5], "|")
            print("-" * 20)

   def take_input(self,player_token,n):
      valid = False
      while not valid:
         player_answer = input("Куда поставим " + player_token+"? ")
         try:
            player_answer = int(player_answer)
         except:
            print("Некорректный ввод. Вы уверены, что ввели число?")
            continue
         if player_answer >= 1 and player_answer <= n**2:
            if(str(playgame.board[player_answer-1]) not in "XO"):
               playgame.board[player_answer-1] = player_token
               valid = True
            else:
               print("Эта клетка уже занята!")
         else:
           print("Некорректный ввод. Введите число от 1 до ",n**2)

   def check_win(self,board,n):
      if n==3:
         win_coord = ((0,1,2), (3,4,5), (6,7,8), (0,3,6), (1,4,7), (2,5,8), (0,4,8), (2,4,6))
         for each in win_coord:
             if board[each[0]] == board[each[1]] == board[each[2]]:
                return board[each[0]]
         return False
      elif n==4:
         win_coord = ((0, 1, 2, 3) , (4, 5, 6, 7 ) , (8, 9, 10, 11) , (12, 13, 14, 15) , (0, 4, 8, 12 ) , (1, 5, 9, 13 ) , (2, 6, 10, 14) , (3, 7, 11, 15 ) , (0, 5, 10, 15) , (12, 9, 6, 3))
         for each in win_coord:
             if board[each[0]] == board[each[1]] == board[each[2]]== board[each[3]]:
                return board[each[0]]
         return False
      elif n==5:
         win_coord = (0, 1, 2, 3, 4) , (5, 6, 7, 8, 9) , (10, 11, 12, 13, 14) , (15, 16, 17, 18, 19),(20, 21, 22, 23, 24) , (0, 5, 10, 15, 20) , (1, 6, 11, 16, 21) , (2, 7, 12, 17, 22) , (3, 8, 19, 18, 23) , (4, 9, 14, 19, 24) , (0, 6, 12, 18, 24) , (20, 16, 12, 8, 4)
         for each in win_coord:
             if board[each[0]] == board[each[1]] == board[each[2]]== board[each[3]]== board[each[4]]:
                return board[each[0]]
         return False
      
      
class Game:
   def __init__(self,k):
      n=k
      if n==3:
         self.board = list(range(1,10))
      elif n==4:
         self.board = list(range(1,17))
      elif n==5:
         self.board = list(range(1,26))
   board = list(range(1,10))
   def main(self,n):
       counter = 0
       win = False
       gamespace = Board()
       while not win:
           gamespace.draw_board(self.board,n)
           if counter % 2 == 0:
              gamespace.take_input("X",n)
           else:
              gamespace.take_input("O",n)
           counter += 1
           tmp = gamespace.check_win(self.board,n)
           if tmp:
              print(tmp, "выиграл!")
              win = True
              break
           if counter == n**2:
               print("Ничья!")
               break
       gamespace.draw_board(self.board,n)

k=input("Введите размер игрового поля (3x3, 4x4, 5x5): ")
playgame = Game(int(k))
playgame.main(int(k))

