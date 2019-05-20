import aleatorio as a
import media as m

lista = a.geraListaInteiro(6)
print(lista)

media = m.media(lista)
mediana = m.mediana(lista)
print("a media da minha lista é " + str(media))
print("a mediana da minha lista é " + str(mediana))

