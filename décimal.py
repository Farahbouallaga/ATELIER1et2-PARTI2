def decimal(n):
    B=0
    ord=0
    while n!=0:
        reste=n%2	
        p=10**ord  
        B=B+reste*p
        ord=ord+1
        n=n//2
        return B
n=int(input("enter un num"))
decimal(n)
print("your num decimal is",decimal(n))
