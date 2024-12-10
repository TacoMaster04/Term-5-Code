from tkinter import *

def setTile(row, column):
    global currentPlayer
    
    if (gameOver):
        return
    
    if board [row][column]["text"] != "":
        return
    
    if currentPlayer == playerO:
        currentPlayer = playerX
    else:
        currentPlayer = playerO
        
    board[row][column]["text"] = currentPlayer
    
    label["text"] = f"{currentPlayer}'s turn"

def newGame():
    pass

playerX = "X"
playerO = "O"
currentPlayer = playerX
board = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

colorBlue = "blue"
colorYellow = "yellow"
colorWhite = "white"
colorGrey = "grey"

turns = 0
gameOver = False

window = Tk()
window.title("Tic Tac Toe")

frame = Frame(window)
frame.grid(row=0, column=0)
label = Label(frame, text=f"{currentPlayer}'s turn", font=("Arial", 20), background=colorGrey, foreground=colorWhite)
label.grid(row=0, column=0, columnspan=3, sticky="we")

for row in range(3):
	for column in range (3):
		board [row][column] = Button(frame, text="", font=("Arial", 20), bg=colorGrey, fg=colorWhite, width=4, height=1,
                               command=lambda row = row, column = column: setTile(row, column))
		board [row][column].grid(row=row+1, column=column)
  
restartButton = Button(frame, text="Restart", font=("Arial", 20), bg=colorGrey, fg=colorWhite, command=newGame())
restartButton.grid(row=4, column=0, columnspan=3, sticky="we")

def checkWinner():
    global turns, gameOver
    turns += 1
    for row in range(3):
        if (board[0][row]["text"] == board[1][row]["text"] == board[2][row]["text"]
            and board[0][row]["text"] != ""):
            label.config(text=board[0][col]["text"] + " wins!", fg=colorYellow)
            for col in range(3):
                board[row][col].config(fg=colorYellow, bg=colorGrey)
            gameOver = True
            return

    for col in range(3):
        if (board[0][col]["text"] == board[1][col]["text"] == board[2][col]["text"]
            and board[0][col]["text"] != ""):
            label.config(text=board[0][col]["text"] + " wins!", fg=colorYellow)
            for col in range(3):
                board[row][col].config(fg=colorYellow, bg=colorGrey)
            gameOver = True
            return

checkWinner()
mainloop()