print ("witaj swiecie")
x=float(input("Podaj wartosc x."))
y=float(input("Podaj wartosc y."))
print(x+y)

if x>10:
	print("x jest wieksze od 10.")
elif x==10 and y==40:
	print("x jest rowne 10 a y jest rowne 40.")
else:
	print("x jest mniejsze od 10.")

for z in range(0,10):
	print(z)
