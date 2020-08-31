# def factorial(N):
#     if N == 1:
#         return 1
#     else:
#         return N * factorial(N-1)

# print(factorial(5))  # 120


def exp(x,n):
    if n == 0:
        return 1
    else:
        return x*exp(x,n-1)
exponential = exp(2,3)
print(exponential)  # 8
