def is_prime(num):
    i = 0 
    sum =0
    for i in range (1,num):
        if num%i==0:
            sum+=1
    
    if sum>2:
        print("this is not prime")
    else:
        print("this is prime")
        
is_prime(76)