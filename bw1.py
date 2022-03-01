    t = 0
    m = 0
    global r            #分值最大的位置
    for (x4,y4) in lst3:
        if rule(board[x4][0],title1[y4],color):
            for (x6,y6) in dic1.keys():
                m += len(dic1[(x6,y6)])
            if m > t:
                t = m
                r = (x4,y4)
            if m == t and x4 < r[0]:
                r = (x4,y4)          
        else:
            continue
