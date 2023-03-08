def fibonacci(n): 
    if n<=0: 
        print("Incorrect input or Empty output") 
    elif n<=2: 
        return n-1
    else: 
        return fibonacci(n-1)+fibonacci(n-2)
