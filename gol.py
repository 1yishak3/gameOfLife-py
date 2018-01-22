#!/usr/bin/env python3
########################################
# @yishak                              #
########################################
from tkinter import *
import copy
def the_game(board):
    next_board=copy.deepcopy(board)
    if len(board)==1:
        next_board[0][0]=" "
    else:
        i=0
        while i<len(board):
            j=0
            while j<len(board[0]):
                
                if i==0 and (j!=0 and j!=len(board[0]) - 1):
                    c1=(board[i][j-1:j+2].count("X"))-1
                    c2=0
                    c3=(board[i+1][j-1:j+2].count("X"))
                elif i==len(board)-1 and (j!=0 and j!=len(board[0]) - 1):
                    c1=(board[i][j-1:j+2].count("X"))-1
                    c2=(board[i-1][j-1:j+2].count("X"))
                    c3=0
                elif i==0 and (j==0 or j==len(board[0]) - 1):
                    if j==0:
                        c1=(board[i][j:j+2].count("X"))-1
                        c2=0
                        c3=(board[i+1][j:j+2].count("X"))
                    elif j==len(board[0])-1:
                        c1=(board[i][j-1:j+1].count("X"))-1
                        c2=0
                        c3=(board[i+1][j-1:j+1].count("X"))

                elif i==len(board)-1 and (j==0 or j==len(board[0]) - 1):
                    if j==0:
                        c1=(board[i][j:j+2].count("X"))-1
                        c2=(board[i-1][j:j+2].count("X"))
                        c3=0
                    elif j==len(board[0])-1:
                        c1=(board[i][j-1:j+1].count("X"))-1
                        c2=(board[i-1][j-1:j+1].count("X"))
                        c3=0

                elif i!=0 and i!=len(board) and (j!=0 and j!=len(board[0]) - 1):
                    c1=(board[i][j-1:j+2].count("X"))-1
                    c2=(board[i-1][j-1:j+2].count("X"))
                    c3=(board[i+1][j-1:j+2].count("X"))
                elif i!=0 and i!=len(board) and (j==0 or j==len(board[0])-1):
                    if j==0:
                        c1=(board[i][j:j+2].count("X"))-1
                        c2=(board[i-1][j:j+2].count("X"))
                        c3=(board[i+1][j:j+2].count("X"))
                    elif j==len(board[0])-1:
                        c1=(board[i][j-1:j+1].count("X"))-1
                        c2=(board[i-1][j-1:j+1].count("X"))
                        c3=(board[i+1][j-1:j+1].count("X"))
                if board[i][j]=="X":
                    neighbors=c1+c2+c3
                    if neighbors<2:
                        next_board[i][j]=" "
                    elif neighbors==2 or neighbors==3:
                        next_board[i][j]="X"
                    elif neighbors>3:
                        next_board[i][j]=" "
                elif board[i][j]==" ":
                    neighbors=c1+c2+c3+1
                    if neighbors==3:
                        next_board[i][j]="X"
                    else:
                        pass
                j=j+1
            i=i+1
    board=copy.deepcopy(next_board)
    return board

def run_game(board):
    row=len(board)
    col=len(board[0])
    margin=5
    width=500
    height=500
    timer=25
    root = Tk()
    canvas = Canvas(root, width=500, height=500)
    canvas.pack()
    def cell_edges(rows, columns, board):
        
        g_width  = width - 2*margin
        g_height = height - 2*margin
        x1 = margin + g_width * columns /col 
        y1 = margin + g_height * rows / row
        x2 = margin + g_width * (columns+1) / col
        y2 = margin + g_height * (rows+1) / row
        #print(x1,y1,x2,y2)
        return (x1, y1, x2, y2)

    def draw_board(canvas,board):
        for rows in range(row):
            for columns in range(col):
                if board[rows][columns]==" ":
                    (x1, y1, x2, y2) = cell_edges(rows, columns, board)
                    canvas.create_rectangle(x1, y1, x2, y2, fill="white")
                else:
                    (x1, y1, x2, y2) = cell_edges(rows, columns, board)
                    canvas.create_rectangle(x1, y1, x2, y2, fill="black")
        return
    #def redrawAll(canvas, board):
        #draw_board(canvas, board)

    def redrawAllWrapper(canvas, board):
        canvas.delete(ALL)
        draw_board(canvas, board)
        canvas.update()
    def timerFiredWrapper(canvas, board):
        the_game(board)
        redrawAllWrapper(canvas, board)
        canvas.create_text(250, 250, text="YITZHAQ_M", fill="red")
        # pause, then call timerFired again
        canvas.after(timer, timerFiredWrapper, canvas,the_game(board))
    timerFiredWrapper(canvas,board)
    root.mainloop()
    return

run_game([
        [" "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "],
        [" "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "],
        [" "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "],
        [" "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "],
        [" "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "],
        [" "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "],
        [" "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "],
        [" "," "," "," "," ","X","X","X","X","X","X","X","X","X","X"," "," "," "," "," "],
        [" "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "],
        [" "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "],
        [" "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "],
        [" "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "],
        [" "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "],
        [" "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "],
        [" "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "],
        [" "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "],
        [" "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "],
        [" "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "],
        [" "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "],
        [" "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "]
    ])

    


