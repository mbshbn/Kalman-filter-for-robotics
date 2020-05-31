
p=[0.2, 0.2, 0.2, 0.2, 0.2]# prior
world=['green', 'red', 'red', 'green', 'green']
measurements = ['red', 'green']
pHit = 0.6
pMiss = 0.2
pExact = 0.8
pOvershoot = 0.1
pUndershoot = 0.1
U = 1

# Compute Posterior distribution form the prior:
def sense(p, Z):
    q=[]
    for i in range(len(p)):
        hit = (Z == world[i])
        q.append(p[i] * (hit * pHit + (1-hit) * pMiss))
    s = sum(q)
    for i in range(len(q)):
        q[i] = q[i] / s
    return q

for k in range(len(measurements)):
    p = sense(p,measurements[k])
    print(p)

# exact motion (not real)
def move_exact(p, U):
    q = []
    print(len(p))
    for i in range(len(p)):
        q.append(p[(i-U)%len(p)])
    return q

# inexact motion
def move(p,pExact,pOvershoot,pUndershoot,U):
    q=[]
    for i in range(len(p)):
        s = pExact * p[(i-U) % len(p)]
        s = s + pOvershoot *  p[(i-U-1) % len(p)]
        s = s + pUndershoot * p[(i-U+1) % len(p)]
        q.append(s)
    return q

print(move_exact(p, U))
print(move(p,pExact,pOvershoot,pUndershoot,U))

# move 2 times
p = move(p,1)
p = move(p,1)

# move N times
for k in range(1000):
    p = move(p,1)
# The result p will be a uniform distribution because we do not have
#any information
print(p)


#measurements = ['red', 'green'],
# The robot sees red, and move 1 block, then sees green, then move again:
# So it starts from 3, then go to 4, and the highest probability
# after the two move will be for the 5th elemnt

measurements = ['red', 'red']
# So it starts from 2, then go to 3, and the highest probability
# after the two move will be for the 4th elemnt

motions = [1,1]

for k in range(len(measurements)):
    p = sense(p, measurements[k])
    p = move(p,pExact,pOvershoot,pUndershoot,motions[k])

print(p)
