p = [0,1,0,0,0]
U = 2

def move (p,U):
    q =[]
    for i in range(len(p)):
        q.append(p[(i-U) % len(p)])
        return q

move(p,U)
