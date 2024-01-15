from tkinter import *
from random import randint


def CheckBomb(targetField):
    targetX = targetY = -1
    for row in range(len(fieldList)):
        for column in range(len(fieldList[row])):
            if fieldList[row][column] == targetField:
                targetX = row
                targetY = column
    if valueList[targetX][targetY]:
        GameOver()
        targetField['bg'] = '#8b0000'
    else:
        valueList[targetX][targetY] = ""
        CheckWin()
        targetField['state'] = DISABLED
        targetField['bg'] = '#fff'
        targetField['text'] = BombCount(targetX, targetY)
        targetField['fg'] = '#000'

def GameOver():
    for row in range(len(fieldList)):
        for column in range(len(fieldList[row])):
            field = fieldList[row][column]
            if valueList[row][column] == 1:
                field['text'] = ""
                field['bg'] = '#f00'
            field['state'] = DISABLED

def CheckWin():
    aux = False
    for i in valueList:
        if 0 in i:
            aux = True
            break
    if not aux:
        for row in range(len(fieldList)):
            for column in range(len(fieldList[row])):
                field = fieldList[row][column]
                if valueList[row][column] == 1:
                    field['text'] = ""
                    field['bg'] = '#229a00'
                field['state'] = DISABLED

def BombCount(targetX, targetY):
    count = 0
    if not valueList[targetX][targetY]:
        for i in range(-1, 2):
            for j in range(-1, 2):
                if 0 <= targetX + i < len(valueList) and 0 <= targetY + j < len(valueList[0]):
                    try:
                        count += valueList[targetX+i][targetY+j]
                    except:
                        pass
    if count == 0:
        return ""
    return count

# Configurações iniciais
window = Tk()
boardX = boardY = 41
while True:
    try:
        boardX = int(input("Insira a quantidade de blocos horizontais (até 40): "))
        boardY = int(input("Insira a quantidade de blocos verticais (até 40): "))
        if boardX < 40 and boardY < 40:
            break
        else:
            print("Valores inválidos, tente novamente.\n")
    except:
        print("Tipo inserido inválido, tente novamente.\n")
board = [boardX, boardY]
fieldSize = 32
x = board[0] * fieldSize
y = board[1] * fieldSize
window.geometry(f'{x}x{y}')
window.title('MineSweeper')

# Estrutura da janela e botões
fieldList = []
for row in range(board[0]):
    fieldRow = []
    for column in range(board[1]):
        field = Button(window, disabledforeground='#000', activebackground='#bbb', bg='#bbb', fg='#000')
        field['command'] = lambda field = field: CheckBomb(field)
        posX = row * fieldSize
        posY = column * fieldSize
        field.place(x=posX, y=posY, height=fieldSize, width=fieldSize)
        fieldRow.append(field)
    fieldList.append(fieldRow)

# Definição das Bombas
valueList = []
for row in range(board[0]):
    valueRow = []
    for column in range(board[1]):
        aux = randint(1, 7)
        bomb = 1 if aux == 1 else 0
        valueRow.append(bomb)
    valueList.append(valueRow)

window.mainloop()