from scipy.stats import binom as b
#this is basically a binomial distribution problem, so I found a module to handle this kind of operations and I went through the documentation to find the most suited functions for this problem (in this case'cdf' or 'comulative distribution function')
def lia(k,n):
    son_AaBb=0.25 #the probability of having a double heterozygote when crossing two double heterozygotes is 0.25
    k_sons=2**k
    final_prob=1-b.cdf(n-1,k_sons,son_AaBb)
    return final_prob
k=6
n=15
result=lia(k,n)
print(result)