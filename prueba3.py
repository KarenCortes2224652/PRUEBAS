#Serie: 2,4,8,16,32,64...
S = "Serie:"
N = int(input("Ingrese un valor: "))
for i in range (1,N+1):
    if i<N:
     S = S + str(2**i)+","
    else:
       S = S + str(2**i) 
print(S)

    