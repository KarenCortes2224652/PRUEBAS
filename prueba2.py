#Serie: 1,4,9,16,25,36,49...
S = "Serie:"
N = int(input("Ingrese un valor: "))
for i in range (1,N+1):
    if i<N:
     S = S + str(i**2)+","
print(S,N**2 )