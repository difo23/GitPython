for cuenta in range(5):
    n = int(input("Introduce la cantidad n para calcular la terna %d" %(cuenta+1)))
    m = int(input("Introduce la cantidad m para calcular la terna %d" %(cuenta+1)))
    if n > m:             
        a = n**2 - m**2
        b = 2*n * m
        c = n**2 + m**2
    else:            
        a = m**2 - n**2
        b = 2*n * m
        c = n**2 + m**2

print(" Terna Pitagorica %d: es igual a: (%d,%d,%d)" % ((cuenta+1), a, b, c))