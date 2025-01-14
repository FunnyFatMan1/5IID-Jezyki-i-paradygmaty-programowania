#Napisz funkcję rekurencyjną, która oblicza n-ty wyraz ciągu Fibonacciego.
def fib (n):
    if n < 0:
        return False
    elif n==0:
        return 0
    elif n==1:
        return 1
    else:
        return fib(n-1) + fib(n-2)
n=2
wynik= fib(n)
print(wynik)