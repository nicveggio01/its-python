i=1
counter=1
sum=0

while True:
    numero:int=input("inserire un valor n > 0 a scelta")
if numero > 0:
    sum+=numero**2
    counter*=1
else:
    print("errore n non valido, ritenta")

print(f"la somma dei quadrati dei numeri inseriti é:{sum}")
print(f"il numero totale dei numeri inseriti è {counter}")