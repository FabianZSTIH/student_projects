#zmienna licznik
licznik = 0
#pętla while do chwili aż licznik mniejszy od 5
while licznik<5:
	print ("wartosc licznika",licznik)
	licznik = licznik + 1
	odpowiedz = input("czy chcesz kontynuowac? tak/nie\n")
	if odpowiedz.lower()=="nie":
		break
print  ("koniec programu")
