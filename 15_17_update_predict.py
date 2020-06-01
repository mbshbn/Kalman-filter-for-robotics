# update the mean and variance
# given the mean and variance of the belief
# and the mean and variance of the measurement.

def update(mean1, var1, mean2, var2):
    new_mean = (var2 *mean1 + var1 * mean2)/(var1 + var2)
    new_var = 1/(1/var1+1/var2)
    return [new_mean, new_var]

# predict the new mean
# and variance given the mean and variance of the
# prior belief and the mean and variance of your
# motion.

def predict(mean1, var1, mean2, var2):
    new_mean = mean1 + mean2
    new_var = var1 + var2
    return [new_mean, new_var]

print(update(10.,8.,13., 2.))
print(predict(10.,4.,12., 4.))

measurements = [5., 6., 7., 9., 10.]
motion = [1., 1., 2., 1., 1.]
measurement_sig = 4.
motion_sig = 2.
mu = 0. # this is a wrong belief because it is different than measurements[0]
sig = 10000. # here we know that our mu is wrong
# sig = 0.0000000001 # (false initial belief) here we know that our wrong mu is corrcet, and results in a worse final result

for i in range(len(measurements)):
    [mu,sig] = update(mu, sig , measurements[i],measurement_sig )
    print('update:',mu,sig)
    [mu,sig] = predict(mu,sig, motion[i],motion_sig)
    print('predict:',mu,sig)
