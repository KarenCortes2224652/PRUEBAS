#Serie: 1/1, 1/2, 1/3, 1/4, 1/5...
S = "Serie:"
N = int(input("Ingrese un valor: "))
for i in range (1,N+1):
    if i<N:
     S = S+"1/" + str(i)+","
    else:
       S = S+"1/" + str(i)
print(S)