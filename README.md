# Kalman-filter-for-robotics


## Localization
It consists of the initial belief, measurement updates (sense) and motion updates.
The probability consists of the probability of the robot being in all possible places. A uniform distribution means there is less information and entropy is high which is undesirable.

### The Measurement Update (uses product):
With a product and the Bayes rule (p(A|B) = p(B|A) p(A) / p(B)) to compute the posterior distribution form the prior distribution, and normalize the result. Here we assume that the robot has the map of its world, called `world`, and `Z` is the measurement. See `move_sense.py`
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
With a convolution (=addition or sum_B(p(A|B) p(B)) )) and  total The probability (p(A) = sum_B(p(A|B) p(B)) )( sum_B(p(A|B) p(B)) ). See `move_sense.py`.

  if the motion is exact:
  ```

  def move_exact(p, U):
      q = []
      print(len(p))
      for i in range(len(p)):
          q.append(p[(i-U)%len(p)])
      return q
  ```
  However, in reality, it is not possible. For the inexact motion, we have
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

## Kalman Filter for 1D
### Gaussian (1D)
See `unimodal_gaussian.py`
```
1/sqrt(2.*pi*sigma2) * exp(-.5*(x-mu)**2 / sigma2)
```

### (Measurement Update) Update the belief based on prior belief and the new measurement:
The new variance is more certain than the other two. See `update_predict.py`.
```
new_mean = (var2 *mean1 + var1 * mean2)/(var1 + var2)
new_var = 1/(1/var1+1/var2)
```
### (Prediction) Update the belief based on prior belief and the new motion:
The new variance shows more uncertainty than the other two. See `update_predict.py`.
```
new_mean = mean1 + mean2
new_var = var1 + var2
```
## Kalman Filter for higher dimensions
It is based on the Multivariate Gaussian. See `Kalman_prediction.py`.
```
# measurement update
y = Z - (H * x)
S = H * P * H.transpose() + R
K = P * H.transpose() * S.inverse()
x = x + (K * y)

P = (I-(K * H)) * P

# prediction (motion update)
x = (F * x) + u
P = F * P * F.transpose()
```


This repo is based on the [Udacity Self-driving car engineering Nanodegree](https://www.udacity.com/course/self-driving-car-engineer-nanodegree--nd013) course.
