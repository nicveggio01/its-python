def comportamento_semaforo(numeroveicolinordsud, numeroveicoliestovest, totale_veicoli, tempo_nord_sud, tempo_est_ovest, tempo_minimo_ns=60, soglia=70, tempo_totale=100):

    if numeroveicolinordsud > soglia:
        tempo_nord_sud= tempo_minimo_ns
        tempo_est_ovest=tempo_totale - tempo_minimo_ns
    elif numeroveicolinordsud and numeroveicoliestovest > soglia:
        tempo_nord_sud= tempo_totale/2
        tempo_est_ovest=tempo_totale/2
    elif numeroveicoliestovest > soglia:
        tempo_est_ovest= tempo_minimo_ns
        tempo_nord_sud= tempo_totale - tempo_minimo_ns
    else:
        numeroveicoliestovest and numeroveicolinordsud < soglia
        tempo_nord_sud= (numeroveicolinordsud/totale_veicoli)*100
        tempo_est_ovest= (numeroveicoliestovest/totale_veicoli)*100

        return tempo_nord_sud, tempo_est_ovest
numeroveicolinordsud = int(input("inserisci il numero di veicoli in direzione nord-sud: "))
numeroveicoliestovest = int(input("inserisci il numero di veicoli in direzione est-ovest: "))
totale_veicoli = numeroveicolinordsud + numeroveicoliestovest

tempo_nord_sud, tempo_est_ovest = comportamento_semaforo(numeroveicolinordsud, numeroveicoliestovest, totale_veicoli, 0, 0)

print(f"il tempo del verde è: {tempo_nord_sud}% ")
print(f"il tempo del verde è: {tempo_est_ovest}% ")