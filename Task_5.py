def fibonacci(n): 
    if n<=0 or int(n)!=n: 
        print("Incorrect input") 
    elif n<=2: 
        return n-1
    else: 
        return fibonacci(n-1)+fibonacci(n-2)
