attesa=0
tutor=10

while True:
    studente=input("inserire nome dello studente")

    if tutor > 0:
        tutor -= 1
        attesa==0
        print("tutor assegnato con successo")
    else:
        attesa +=1
        print("studente in attesa")
    if tutor==0 and attesa > 50:
        print("Non è possibile fare il tutoraggio agli studenti")
        break
    