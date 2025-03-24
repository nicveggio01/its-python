voto:int=0
counter=0
sum=0

opzione:str=str(input("vuoi inserire un voto? (si/no): "))
while opzione == "si":

 voto:int=int(input("inserisci un voto"))

if voto > 0:
          
     counter +=1
     sum=sum+voto
else:
         print("errore il numero deve essere maggiore di zero!")
         opzione:str=str(input("vuoi inserire un altro voto?(si/no): ")) 
 
if counter > 0:
        media:float=sum/counter
        print(f"la media dei voti è: {media} ")
    
        
else:
        counter < 0
        print("nessun voto inserito")
        