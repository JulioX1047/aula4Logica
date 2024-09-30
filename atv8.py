somas=0

for i in range(1,6):
    nota= float(input("Informe sua nota "))
    somas+=nota
    cont=5
    med=somas/cont
if med >=6 :
        print(f"Aprovado com a media : {med}")
else :
        print(f"Reprovado com a media :{med}  ")    