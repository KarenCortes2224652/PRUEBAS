#Serie: 1/3, 2/5, 9/7, 64/9, 625/11...
S = "Serie:"
N = int(input("Ingrese un valor: "))
for i in range (1,N+1):
    if i<N:
     S = S + str((i+5)*1)+","
    else:
       S = S + str((i+5)*1)
print(S)