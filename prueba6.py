#Serie: 2, 6, 12, 20, 30, 42, 56...
S = "Serie:"
N = int(input("Ingrese un valor: "))
for i in range (1,N+1):
    if i<N:
     S = S + str((i+1)*i)+","
    else:
       S = S + str((i+1)*i)
print(S)