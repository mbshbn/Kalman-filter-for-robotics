#Modify the move function to accommodate the added
#probabilities of overshooting or undershooting
#the intended destination.

p=[0, 1, 0, 0, 0]
world=['green', 'red', 'red', 'green', 'green']
measurements = ['red', 'green']
pHit = 0.6
pMiss = 0.2
pExact = 0.8
pOvershoot = 0.1
pUndershoot = 0.1
U = 1


def sense(p, Z):
    q=[]
    for i in range(len(p)):
        hit = (Z == world[i])
        q.append(p[i] * (hit * pHit + (1-hit) * pMiss))
    s = sum(q)
    for i in range(len(q)):
        q[i] = q[i] / s
    return q

def move_exact(p, U):
    q = []
    print(len(p))
    for i in range(len(p)):
        q.append(p[(i-U)%len(p)])
    return q

def move_inexact(p,pExact,pOvershoot,pUndershoot,U):
    q=[]
    for i in range(len(p)):
        s = pExact * p[(i-U) % len(p)]
        s = s + pOvershoot *  p[(i-U-1) % len(p)]
        s = s + pUndershoot * p[(i-U+1) % len(p)]
        q.append(s)
    return q

print(move_exact(p, U))
print(move_inexact(p,pExact,pOvershoot,pUndershoot,U))
