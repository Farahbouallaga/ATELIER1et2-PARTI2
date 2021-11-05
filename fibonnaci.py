def fibonnaci(n):
    if n<=1:	
        return n
    else:
        
         return fibonnaci(n-1)+fibonnaci(n-2)
n=int(input("ENTRE VOTRE NUM"))
for n in range (n):
 print(fibonnaci(n),end=" ")
