from random import randrange

board=[[1,2,3],[4,5,6],[7,8,9]]
free_board=[[1,2,3],[4,5,6],[7,8,9]]


#   This function saves the current player and pc inputs.
def display_board(board):
  print("+-------+-------+-------+")
  print("|","|","|","|", sep='       ')   
  print('|',board[0][0], "|",  board[0][1] , "|" , board[0][2],'|', sep="   ")
  print("|","|","|","|", sep='       ')
  print("+-------+-------+-------+")
  print("|","|","|","|", sep='       ')
  print('|',board[1][0], "|",  board[1][1] , "|" , board[1][2],'|', sep="   ")
  print("|","|","|","|", sep='       ')
  print("+-------+-------+-------+")
  print("|","|","|","|", sep='       ')
  print('|',board[2][0], "|",  board[2][1] , "|" , board[2][2],'|', sep="   ")
  print("|","|","|","|", sep='       ')
  print("+-------+-------+-------+")


#   This function ccollects the player's input and place's it on the board
def enter_move(board):
  if len(f) == 0:
    return False
  elif len(f) != 0:
      i = int(input("Choose a number to input 'O': "))
      if i == 1:
        x = 0
        y = 0
      elif i == 2:
        x = 0
        y = 1
      elif i == 3:
        x = 0
        y = 2
      elif i == 4:
        x = 1
        y = 0
      elif i == 6:
        x = 1
        y = 2
      elif i == 7:
        x = 2
        y = 0
      elif i == 8:
        x = 2
        y = 1
      elif i == 9:
        x = 2
        y = 2
      
      move = board[x][y]
      print( "you enterd O at ", move)
      if move in board[x]:
        board[x][y]="O"
        #return display_board(board) #for debugging
      else:
        print("Invalid move")
        return enter_move(board)  


#   This function records the positions on the board that are free (empty).
def free_field(board):
  global free_fields
  free_fields=[]
  for i in range(3):
    #print ("i = ", i) #for debugging
    for j in range(3):
      #print ("j = ", j) #for debugging
      if board[i][j] in free_board[i]:
        free_fields.append([i]+[j])
  #print ("free fields= ", free_fields) #for debugging
  
  return free_fields


#   This function define the requirment for winning.
def victory_for(board, sign):
  if (board[0][0] == sign and board[0][1] == sign and board[0][2] == sign):
    return True
  elif (board[1][0] == sign and board[1][1] == sign and board[1][2] == sign):
    return True
  elif(board[2][0] == sign and board[2][1] == sign and board[2][2] == sign):
    return True
  elif(board[0][0] == sign and board[1][0] == sign and board[2][0] == sign):
    return True
  elif(board[0][1] == sign and board[1][1] == sign and board[2][1] == sign):
    return True
  elif(board[0][2] == sign and board[1][2] == sign and board[2][2] == sign):
    return True
  elif(board[0][0] == sign and board[1][1] == sign and board[2][2] == sign):
    return True
  elif(board[0][2] == sign and board[1][1] == sign and board[2][0] == sign):
    return True
  else:
    return False
    

#   This function defines the requirment for a draw.
def draw_move(board):
  if board[0][0] != 1 and board[0][1] != 2 and board[0][2] != 3 and board[1][0] != 4 and board[1][1] != 5 and board[1][2] != 6 and board[2][0] != 7 and board[2][1] != 8 and board[2][2] != 9:
    return True
  else:
    return False


#   This function enables the pc to enter a move in a free space on the board.
#   Note the PC always plays "X" first in the middle of the board, i.e position (5).    
def ai_move(board):
  if board[1][1]!="X":
    print ("PC played 'X' in ", 5)
    board[1][1]="X"
    return display_board(board)
  if len(f) == 0:
    #print ("len free fields= ", len(free_fields)) #for debugging
    return False
  elif len(f) != 0:
    #print ("len free fields= ", len(free_fields)) #for debugging
    e= randrange(0,len(free_fields))
    a = free_fields[e][0]
    b = free_fields[e][1]
    valid = board[a][b]
    print ("PC played 'X' in ", valid)
    if valid in free_board[a]:
       board[a][b]="X"
       return display_board(board)
    else:
       ai_move(board)


# From this point on all functions are used accordingly in order to run the game succecfully.
for i in range(10):
  f=free_field(board)
  if ai_move(board):
    free_field(board)
    print (ai_move(board))  

  f=free_field(board)
  if enter_move(board):
    free_field(board)
    enter_move(board)
    
    
  if victory_for(board, "X"):
    print ("PC wins :(")
    break
  if victory_for(board, "O"):
    print ("YOU WIN!!! :)")
    break
  if draw_move(board):
    print ("It's a Draw")
    break
