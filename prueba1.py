#Serie: 1, 2, 3, 4, 5, 6, 7...
S = "Serie:"
N = int(input("Digite el número de elementos de la serie: "))
for i in range (1,N+1):
    if i < N:
        S = S+str(i)+","
    else:
        S = S+str(i)
print(S)


