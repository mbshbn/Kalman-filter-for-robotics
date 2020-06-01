# Kalman-filter-for-robotics


## Localization
It consists of the initial belief, measurement updates (sense) and motion updates.
The probability consist the probability of the robot being in all possible places. A uniform distribution means there is less information and entropy is high which is undesirable.

### The Measurement Update (uses product):
With a product and the Bayes rule (p(A|B) = p(B|A) p(A) / p(B)) to compute the posterior distribution form the prior distribution, and normalize the result. Here we assued that the robot has the map of its world, called `world`, and `Z` is the measurement.
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


### The Motion Update (prediction, uses total probability):
With a convolution (=addition or sum_B(p(A|B) p(B)) )) and  total The probability (p(A) = sum_B(p(A|B) p(B)) )( sum_B(p(A|B) p(B)) ):

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
## Gaussian (1D)
```
def f(mu, sigma2, x):
    return 1/sqrt(2.*pi*sigma2) * exp(-.5*(x-mu)**2 / sigma2)
```
### update the belief based on prior belief and the new measurement:
The new variance is more certain that other two.
```
new_mean = (var2 *mean1 + var1 * mean2)/(var1 + var2)
new_var = 1/(1/var1+1/var2)
```
