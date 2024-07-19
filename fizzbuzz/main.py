def fizzbuzz(n):
    counter = []
    
    for i in range(1, n + 1):
        if(i % 3 == 0 and i % 5 == 0):
            counter.append("FizzBuzz")
        elif(i % 3 == 0):
            counter.append("Fizz")
        elif(i % 5 == 0):
            counter.append("Buzz")
        else:
            counter.append(str(i))
    
    return counter

print(fizzbuzz(15))