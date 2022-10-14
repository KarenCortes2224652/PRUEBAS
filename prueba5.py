#Serie: 1/2, 1/5, 1/10, 1/17, 1/26...
S = "Serie:"
N = int(input("Ingrese un valor: "))
for i in range (1,N+1):
    if i<N:
     S = S +"1/" + str(i**2 +1)+","
    else:
       S = S +"1/" + str(i**2 +1)
print(S)

