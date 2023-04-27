import math

def BinomialProbability(n,p,x) :
    pro = math.comb(n,x)*math.pow(1-p,n-x)*math.pow(p,x)
    return pro

n = 10
p = 0.05
i = 0
while i < n+1:
	print(f"P({i}) = {BinomialProbability(n,p,i)}")
	i += 1


print(f"\nP(0) = Probability of X <= 1 is P(0) + P(1) = {BinomialProbability(10, 0.05, 0)+BinomialProbability(10, 0.05, 1)}")
