slownik = {'czesc': 'hello', 'ogien': 'fire', 'komputer': 'computer', 'krzeslo': 'chair'}

print ("Podaj slowo.")

while True:
	slowo=input()
	if slowo in slownik:
		print (slowo, ':', slownik[slowo])
	else:
		print ("slowo nie istnieje w slowniku.")
