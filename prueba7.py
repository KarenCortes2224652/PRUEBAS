#Serie: 3, 8, 13, 18, 23, 28...
S = "Serie:"
N = int(input("Ingrese un valor: "))
for i in range (1,N+1):
    if i<N:
     S = S + str (3+(i-1)*5)+","
    else:
       S = S + str(3+(i-1)*5)
print(S)