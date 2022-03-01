'''
def rule(row,col,color):
    '''检测'''
    #定义以棋子为(0,0)周围坐标;color为自己棋子的颜色
    global direction
    direction = ((-1,-1), (-1,0), (-1,1), (0,-1), (0,1), (1,-1), (1,0), (1,1))
    #第一个合法条件：周围某一方向有对方棋子(+while)
    global lst1
    lst1 = []           #❕所有符合条件一有对方棋子的方向
    judge1 = False
    for i8 in range(dimension):   
        if board[i8][0] == row:
            for (x1,y1) in direction:
                if 0 < title1.index(col)+y1 <= dimension and 0 <= i8+x1 < dimension:
                    if board[i8+x1][title1.index(col)+y1] == color:
                        continue
                    elif board[i8+x1][title1.index(col)+y1] == none:
                        continue
                    else:
                        lst1.append((x1,y1))
        if not lst1 == None:
            judge1 = True
            break     
    judge4 = False
    #第二个合法条件：直线末端有本方棋子(在条件1成立的情况下)
    if judge1:
        global dic1
        global lst2
        dic1 = {}         #❕存放某方向上对方棋子的所有位置（不一定满足条件二）
        lst2 = []         #同时满足条件一、二的方向
        for i9 in range(dimension):
            if board[i9][0] == row:
                for (x2,y2) in lst1:
                    n = 1
                    while 1 <= n <= dimension:
                        if 0 < title1.index(col)+y2*n <=dimension and 0 <= i9+x2*n < dimension:
                            if board[i9+x2*n][title1.index(col)+y2*n] == none:
                                n += 1
                                continue
                            if board[i9+x2*n][title1.index(col)+y2*n] == color:     #u_color对方的颜色
                                lst2.append((x2,y2))
                            else: 
                                if (x2,y2) not in dic1:
                                    dic1[(x2,y2)] = [[i9+x2*n,title1.index(col)+y2*n]]
                                else:
                                    dic1[(x2,y2)] += [[i9+x2*n,title1.index(col)+y2*n]]
                        n += 1
            if not lst2 == None:
                judge4 = True
                break
    return judge4
'''


def rule(row,col,color):
    if color == black:
        u_color == white
    else:
        u_color == black

    judge1 = False
    direction = ((-1,-1), (-1,0), (-1,1), (0,-1), (0,1), (1,-1), (1,0), (1,1))
    global dic1
    dic1 = {}

    n = 1
    for i8 in range(dimension)
        for (x1,y1) in direction:
            while 0 < title1.index(col)+y1*n <= dimension and 0 <= i8+x1*n < dimension and board[i8+x1*n][title1.index(col)+y1*n] == u_color:
                if (x1,y1) not in dic1:
                    dic1[(x1,y1)] = [[i8+x1*n,title1.index(col)+y1*n]]
                else:
                    dic1[(x1,y1)] += [[i8+x1*n,title1.index(col)+y1*n]]
                if board[i8+x1*(n+1)][title1.index(col)+y1*(n+1)] == color:
                    juege1 = True
                    break
                n += 1
    return judge1
