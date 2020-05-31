# Kalman-filter-for-robotics


## Localization
It consists of the initial belief, measurement updates (sense) and motion updates.
The probability consist the probability of the robot being in all possible places. A uniform distribution means there is less information and entropy is high which is undesirable.

### The Measurement Update:
* with a product to compute the posterior distribution form the prior distribution, and normalize the result
  ```
  def sense(p, Z):
      q=[]
      for i in range(len(p)):
          hit = (Z == world[i])
          q.append(p[i] * (hit * pHit + (1-hit) * pMiss))
      s = sum(q)
      for i in range(len(q)):
          q[i] = q[i] / s
      return q
  ```
* with the Bayes rule.

### The Motion Update:
* with a convolution (=addition)
  if the motion is exact:
  ```

  def move_exact(p, U):
      q = []
      print(len(p))
      for i in range(len(p)):
          q.append(p[(i-U)%len(p)])
      return q
  ```
  However, in reality it is not possible. For the inexact motion, we have
  ```
  def move(p,pExact,pOvershoot,pUndershoot,U):
      q=[]
      for i in range(len(p)):
          s = pExact * p[(i-U) % len(p)]
          s = s + pOvershoot *  p[(i-U-1) % len(p)]
          s = s + pUndershoot * p[(i-U+1) % len(p)]
          q.append(s)
      return q
  ```
* with a total probability.
