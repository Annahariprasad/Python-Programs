import math

def estimate_pi():
    total = 0
    k = 0
    factor = 2*math.sqrt(2)/9801
    while True:
        num = ((math.factorial(4*k))*(1103+26390*k))
        den = pow(math.factorial(k),4)*pow(396,(4*k))
        term = factor*num/den
        total += term
        if(abs(term) < 1e-15):
            break
        k += 1
    return 1/total

print("Name : Anna Hariprasad")
print("Regno : 19X51A0503\n")
print("pi value : ",estimate_pi())
