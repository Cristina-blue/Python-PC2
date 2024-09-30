Fibonacci = [0, 1]

while True:
    siguiente = Fibonacci[-1] + Fibonacci[-2] 
    if siguiente > 50:  
        break
    Fibonacci.append(siguiente)  

print("La serie de Fibonacci entre 0 y 50 es:", Fibonacci)
