"""The idea of PEM is to identify frequently occurring prefixes
That is, the larger D gets, we implement g subgroups.
for each subgroup, the prefixes of subgroup j would be
length N shorter than subgroup j + 1"""
               
def Sorting(P):
    P.sort(key=len)
    return P
      



  

def helper(S, N):
    if len(S) <= N:
        return True
    else:
        return False

def PEM(P, g, N):
    a = [[0] * 14 for i in range(g)]  "14 is just an abitrary number that insured no index out of bounds error"
    index2 = 0
    currentN = N
    index1 = 0
    while index2 < (len(P) - 1):
        if helper(P[index2], currentN) == True:
            a[index1][index2] = P[index2]
            index2 += 1
        else:
            currentN += N
            index2 += 1
            index1 += 1
    return a

def intToBinaryString(num, length):
    return bin(num)[2:].zfill(length)
    
P = ["01010000", "0101001", "01010", "0110100", "0101011", "010", "01010", "0100"]
print(PEM(P, 4, 2))