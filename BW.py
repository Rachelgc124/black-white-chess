#functions
def Init_board():                   #☑️
    '''读入棋盘大小n,按照要求初始化棋盘
    【.-未被占用/X-被黑棋占用/O-被白棋占用】'''
    #输入棋盘
    global dimension
    dimension = int(input("Enter the board dimension:"))
    #判断是否符合条件
    while 1:
        if not dimension % 2 == 0:
            print("Please enter an even number")
            dimension = int(input("Enter the board dimension:"))
            continue
        if not (dimension >= 4 and dimension <= 26):
            print("Please enter dimension range from 4 to 26")
            dimension = int(input("Enter the board dimension:"))
            continue
        else:
            break
    #初始化棋盘
    global black 
    global white 
    global none 
    global title1
    global board
    global judge4
    judge4 = True
    
    black = "X"
    white = "O"
    none = "."
    title1 = [" "]
    for i1 in range(dimension):
        title1.append(chr(i1+97))

    board = []
    i2 = 0
    while i2 < dimension:
        board.append([])
        i2 += 1
    t1 = [x for x in (none*dimension)]
    for i3 in range(dimension):
        board[i3].append(chr(i3+97))
        board[i3].extend(t1)
    
    #初始棋盘
    for i4 in range(dimension):
        if i4 == dimension/2 - 1:
            board[i4][int(dimension/2)] = "O"
            board[i4][int(dimension/2 + 1)] = "X"
            continue
        if i4 == dimension/2:
            board[i4][int(dimension/2)] = "X"
            board[i4][int(dimension/2 + 1)] = "O"
            continue
    return

def select_chess():             #☑️
    '''询问选棋'''
    global CP
    global HP
    CP = input("Computer plays (X/O) :")
    while 1:
        if CP == "X":
            HP = "O"
            break
        if CP == "O":
            HP = "X"      
            break
        else:
            print("Please enter X/O")
            CP = input("Computer plays (X/O) :")
    return 

def printBoard():               #☑️
    '''输出棋盘'''
    print(" ".join(title1))
    for i5 in range(dimension):
        print(" ".join(board[i5]))
    return

def computer_move():
    '''计算机下棋'''
    #比较分值
    position_score(CP)
    #修改棋盘
    board[r[0]][r[1]] = CP
    flip(CP)
    #输出
    print("Computer places " + CP + " at " + str(board[r[0]][0]) + str(title1[r[1]]) + ".")  
    printBoard()
    return

def human_move():
    '''用户下棋'''
    strhp = input("Enter move for " + HP + " (RowCol):")
    global row1
    global col1
    row1 = strhp[0]
    col1 = strhp[1]
    global con
    if check_legal_move(row1,col1,HP):
        #修改棋盘
        for i6 in range(dimension):
            if board[i6][0] == row1:
                if board[i6][title1.index(col1)] == none:
                    board[i6][title1.index(col1)] = HP
                else:
                    con = "Human gave up."
                    print("Invalid move.")    
                    return gameover(1)
        #输出
        flip(HP)
        printBoard()
        return
    else:
        con = "Human gave up."
        print("Invalid move.")    
        return gameover(1)

def rule(row,col,color):
    '''检测'''
    u_color = ""
    if color == black:
        u_color = white
    else:
        u_color = black

    judge1 = False
    direction = ((-1,-1), (-1,0), (-1,1), (0,-1), (0,1), (1,-1), (1,0), (1,1))
    global dic1
    dic1 = {}
    for i8 in range(dimension):
        if board[i8][0] == row:
            for (x1,y1) in direction:
                n = 1
                while (0 < title1.index(col)+y1*(n+1) <= dimension) and (0 <= i8+x1*(n+1) < dimension) and (board[i8+x1*n][title1.index(col)+y1*n] == u_color):
                    if board[i8+x1*(n+1)][title1.index(col)+y1*(n+1)] == color:
                        k = 1
                        while k <= n:
                            if (x1,y1) not in dic1:
                                dic1[(x1,y1)] = [[i8+x1*k,title1.index(col)+y1*k]]
                            else:
                                dic1[(x1,y1)] += [[i8+x1*k,title1.index(col)+y1*k]]
                            k += 1
                        judge1 = True
                        break
                    n += 1
    return judge1

def check_legal_move(row,col,color):
    '''检测颜色为color的棋子落在棋盘格(row,col)上是否合法'''
    #检验位置是否合法
    if rule(row,col,color):
        return True
    else:
        return False

def search(color):
    '''寻找可能的位置'''
    global lst3
    lst3 = []       #符合条件的可能的位置
    global s_black
    global s_white
    s_black = 0
    s_white = 0
    global judge2
    judge2 = False
    for x5 in range(dimension):
        for y5 in range(1,dimension+1):
            if board[x5][y5] == none:
                judge2 = True
                if rule(board[x5][0],title1[y5],color):
                    lst3.append((x5,y5))
            elif board[x5][y5] == black:
                s_black += 1
            elif board[x5][y5] == white:
                s_white += 1
    #满足check_的合法条件
    return

def position_score(color):
    '''计算“分值”'''
    #可能的位置
    search(color)
    #各个方向上夹有几个对方棋子，累加赋分
    #比较大小（同行选字母小）
    t = 0
    global r            #分值最大的位置
    for (x4,y4) in lst3:
        if rule(board[x4][0],title1[y4],color):
            m = 0
            for (x6,y6) in dic1.keys():
                m += len(dic1[(x6,y6)])
            if m > t:
                t = m
                r = (x4,y4)
            if m == t and x4 < r[0]:
                r = (x4,y4)          
        else:
            continue
    return

def flip(color):
    '''翻转八个方向上对手的棋子'''
    #定位每一个方向上对手的棋子并翻转
    if color == CP:
        rule(board[r[0]][0],title1[r[1]],CP)
    else:
        rule(row1,col1,HP)
    for (x3,y3) in dic1.keys():
        for (x7,y7) in dic1[(x3,y3)]:
            board[x7][y7] = color
    return

def check_board(color,u_color):
    '''检测游戏是否结束'''
    #计算数目：整个棋盘满了/一方的棋子被另一方吃光/双方没有可落子的棋盘格
    search(u_color)
    global judge5
    judge5 = True
    if not judge2:          #2
        print("The chess board has no space avalible.")
        return gameover(2)
    if s_black == 0:              #3
        print("O player wins.")
        return gameover(3)
    if s_white == 0:           #3
        print("X player wins.")
        return gameover(4) 
    if len(lst3) == 0:         #4.1
        search(color)
        if len(lst3) == 0:
            print("Both players have no valid move.")
            return gameover(5)
        else:
            print(u_color + " player has no valid move.")
            return judge5
    judge5 = False
    return 
    #一方落在非法位置(见上)1

def gameover(n):
    '''游戏结束，统计得分，输出结果'''
    print("Game over.")
    if n == 1:
        global judge4
        judge4 = False
        return print(CP + " player wins.")
    #电脑得分
    global c_s
    global h_s
    global con
    con = ""
    if CP == black:
        c_s = s_black
        h_s = s_white
        con = str(c_s) + " : " + str(h_s)
        print("X : O = "+ str(c_s) + " : " + str(h_s))
    else:
        c_s = s_white
        h_s = s_black
        con = str(h_s) + " : " + str(c_s)
        print("X : O = "+ str(h_s) + " : " + str(c_s))
    #玩家得分
    #比较大小
    if c_s > h_s:
        result = str(CP + " player wins.")
    elif c_s < h_s:
        result = str(HP + " player wins.")
    else:
        result = "Draw!"
    judge4 = False
    return print(result)

def saveinfo():
    '''对弈信息写入文件'''
    #游戏开始时间/单次游戏使用时间/棋盘大小/黑棋玩家/白棋玩家/游戏比分（信息之间使用逗号分隔）
    lst4 = [start_time, (et - st).seconds, str(dimension)+"*"+str(dimension), "", "", ""]
    if CP == black:
        lst4[3] = "computer"
        lst4[4] = "human"
    else:
        lst4[3] = "human"
        lst4[4] = "computer"
    lst4[5] = con
    import csv
    with open('reversi.csv', 'a+', newline='') as fil:
        csv_writer = csv.writer(fil, dialect="excel")
        csv_writer.writerow(lst4)
    return

def do_CP():
    computer_move()
    check_board(CP,HP)
    if judge4:
        if judge5:
            return do_CP()
        else:
            return do_HP()
    else:
        return

def do_HP():
    human_move()
    check_board(HP,CP)
    if judge4:
        if judge5:
            return do_HP()
        else:
            return do_CP()
    else:
        return

#运行
import time
from datetime import datetime
start_time = time.strftime('%Y%m%d %H:%M:%S',time.localtime(time.time()))
st = datetime.now()

Init_board()
select_chess()
printBoard()

if CP == black:
    do_CP()
else:
    do_HP()

end_time = time.strftime('%Y%m%d %H:%M:%S',time.localtime(time.time()))
et = datetime.now()

saveinfo()
