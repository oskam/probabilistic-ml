import numpy as np
import scipy
import scipy.special


faculties_prop = [.02, .05, .15, .1, .15, .1, .3, .07, .06]

prob = [1-x for x in faculties_prop]
result = np.prod(np.array(prob))
print(result)

n = 1


print(scipy.special.factorial(5))
def multinomial(x,n,p):
    result = scipy.special.factorial(n)/((scipy.special.factorial(1)*scipy.special.factorial(2))) * p**0
    return result
#
print(multinomial(x,n,p))