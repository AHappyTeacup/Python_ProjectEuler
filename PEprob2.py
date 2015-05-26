memo = {0:1, 1:1}
def fibm(n):
    if not n in memo:
        memo[n] = fibm(n-1) + fibm(n-2)
    return memo[n]

def PEprob2(n):
    a, i = 0, 0
    while fibm(i)<n:
        if fibm(i)%2==0:
            a=a+fibm(i)
        i=i+1
    return a

print(PEprob2(4000000))