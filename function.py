
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
    
    black = "X"
    white = "O"
    none = "."
    title1 = [" "]
    for i1 in range(dimension):
        title1.append(chr(i1+97))

    board = []
    for i2 in range(dimension):
        board.append([])
    t1 = [x for x in (none*dimension)]
    for i3 in range(dimension):
        board[i3].append(chr(i2+97))
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

def computer_move(color):
    '''计算机下棋'''
    #比较分值
    position_score()
    #修改棋盘
    board[r[0]][r[1]] = CP
    #输出
    printBoard()
    return

def human_move(color):
    '''用户下棋'''
    strhp = input("Enter move for " + HP + " (RowCol):")
    #修改棋盘
    row1 = strhp[0]
    col1 = strhp[1]
    for i6 in range(dimension):
        if board[i6][0] == row1:
            board[i6][title1.index(col1)] = HP
    #输出
    printBoard()
    return

def rule(row,col,color):
    '''检测'''
    #定义以棋子为(0,0)周围坐标;color为对方棋子的颜色
    global direction
    direction = ((-1,-1), (-1,0), (-1,1), (0,-1), (0,1), (1,-1), (1,0), (1,1))
    #第一个合法条件：周围某一方向有对方棋子(+while)
    global lst1
    lst1 = []           #❕有对方棋子的方向
    judge1 = False
    for i8 in range(dimension):   
        if board[i8][0] == row:
            for (x1,y1) in direction:
                if 0 < title1.index(col)+y1 <= dimension and 0 <= i8+x1 < dimension:
                    if board[i8+x1][title1.index(col)+y1] == color:
                        lst1.append((x1,y1))
        if not lst1 == None:
            judge1 = True
            break           
    #第二个合法条件：直线末端有本方棋子(在条件1成立的情况下)
    while judge1:
        global dic1
        global lst2
        dic1 = {}         #❕存放所夹对方棋子
        lst2 = []
        for i9 in range(dimension):
            if board[i9][0] == row:
                for (x2,y2) in lst1:
                    while 2 <= n <= dimension:
                        if 0 < title1.index(col)+y2*n <=dimension and 0 <= i9+x2*n < dimension:
                            if board[i9+x2*n][title1.index(col)+y2*n] == color:
                                if (x2,y2) not in dic1:
                                    dic1[(x2,y2)] = [[i9+x2*n,title1.index(col)+y2*n]]
                                else:
                                    dic1[(x2,y2)] += [[i9+x2*n,title1.index(col)+y2*n]]
                            elif board[i9+x2*n][title1.index(col)+y2*n] == u_color:     #u_color自己的颜色
                                lst2.append((i9+x2*n,title1.index(col)+y2*n))
                        n += 1
            if not lst2 == None:
                judge1 = True
                break
    return judge1

def check_legal_move(row,col,color):
    '''检测颜色为color的棋子落在棋盘格(row,col)上是否合法'''
    #检验位置是否合法
    if rule():
        return True
    else:
        global judge3
        judge3 = True
        print("Invalid move.")           
        return gameover()

def search():
    '''寻找可能的位置'''
    global lst3
    lst3 = []
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
                if rule(''):
                    lst3.append((x5,y5))
            elif board[x5][y5] == black:
                s_black += 1
            elif board[x5][y5] == white:
                s_white += 1
    #满足check_的合法条件
    return

def position_score():
    '''计算“分值”'''
    #可能的位置
    search()
    #各个方向上夹有几个对方棋子，累加赋分
    t = 0
    global r
    for (x4,y4) in lst3:
        if len(dic1[(x4,y4)]) > t:
            t = len(dic1[(x4,y4)])
            r = (x4,y4)
        if len(dic1[(x4,y4)]) == t and x4 < r[0]:
            r = (x4,y4)
    #比较大小（同行选字母小）
    return

def flip(row,col,color):
    '''翻转八个方向上对手的棋子'''
    #定位每一个方向上对手的棋子并翻转
    for (x3,y3) in lst2:
        board[x3][y3] = u_color
    return

def check_board():
    '''检测游戏是否结束'''
    #计算数目：整个棋盘满了/一方的棋子被另一方吃光/双方没有可落子的棋盘格
    search()
    if not judge2:
        print("The chess board has no space avalible.")
        gameover()
    if lst3 == None:
        gameover()
    #一方落在非法位置(见上)
    return

def gameover():
    '''游戏结束，统计得分，输出结果'''
    print("Game over.")
    if judge3:
        return print(CP + " player wins.")
    #电脑得分
    search()
    global c_s
    global h_s
    if CP == black:
        c_s = s_black
        h_s = s_white
        print("X : O = "+ CP + " : " + HP)
    else:
        c_s = s_white
        h_s = s_black
        print("X : O = "+ HP + " : " + CP)
    #玩家得分
    #比较大小
    if c_s > h_s:
        result = str(CP + "player wins.")
    elif c_s < h_s:
        result = str(HP + "player wins.")
    else:
        result = "Draw!"
    return print(result)

def saveinfo():
    '''对弈信息写入文件'''
    #游戏开始时间/单次游戏使用时间/棋盘大小/黑棋玩家/白棋玩家/游戏比分（信息之间使用逗号分隔）
    lst4 = [start_time, (end_time - start_time).seconds, dimension, "", "", ""]
    if CP == black:
        lst4[3] = CP
        lst4[4] = HP
    else:
        lst4[3] = HP
        lst4[4] = CP
    lst4[5] = lst4[3] + "to" + lst4[4]
    import csv
    fil = open('reversi.csv', 'a', newline='')
    csv_writer = csv.writer(fil, dialect='excel')
    csv_writer.writerow(lst4)
    return

