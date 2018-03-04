import numpy as np
import scipy
import scipy.special


faculties_prob = [.02, .05, .15, .1, .15, .1, .3, .07, .06]

prob = [1-x for x in faculties_prob]
result = np.prod(np.array(prob))
print(result)

#1.
# jednokrotne powtórzenie eksperymentu o X+1 możliwych rezultatach,
# gdzie potencjalne rezultaty: 0,1..,X oznaczają oznaczają liczbę kierunków,
# na które student się dostał.
# Pr(Y_1 = 1, Y_2 = 0,....,Y_(X+1) = 0 )  =
# = 1!/[n_1!*...*n_(X+1)!]  * (P_1)^1* (P_2)^0 * .... *(P_(X+1))^0 =
# = 1!/1! * P_1 = Pr(Y_1 = 0) = (1- p_1)*...*(1-p_X)


result = 1!/

print(scipy.special.factorial(5))
def multinomial(x,n,p):
    result = scipy.special.factorial(n)/((scipy.special.factorial(1)*scipy.special.factorial(2))) * p**0
    return result
#
print(multinomial(x,n,p))