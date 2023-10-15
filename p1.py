frase = "Programar eS LO más parecido Que tenEMos a un suPERpoder"
longitud= len(frase)
print(longitud)

mitad = longitud // 2

if longitud % 2 == 0:
  p_contra= frase[mitad-2: mitad+2]
  print(p_contra)
else:
  p_contra= frase[mitad-1: mitad+2]
  print(p_contra)

lista1= frase.split()
print(lista1)

palabra1= lista1[0][:2]
palabra2= lista1[-1] 

añade=  p_contra + palabra1 + palabra2
print(añade)

contra=añade.replace(" ","")
print(contra)

contra.replace("a", "@")

contra=contra[-2].upper()
print(contra)