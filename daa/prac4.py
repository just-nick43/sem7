def binomialCoeff(n, k):
    if k == 0 or k == n:
        return 1
    return binomialCoeff(n-1, k-1) + binomialCoeff(n-1, k)

n = int(input("Enter the value of n: "))
k = int(input("Enter the value of k: "))
print("Value of C(%d,%d) is (%d)" % (n, k, binomialCoeff(n, k)))