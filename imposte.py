SCAGLIONE1=20000
SCAGLIONE2=50000
TASSA_SC1=0.23
TASSA_SC2=0.35
TASSA_SC3=0.43
reddito = float(input ("Che reddito hai? ")) #inserimento reddito
print("Il tuo reddito è ",reddito,"euro")
if reddito <= SCAGLIONE1 :
    aliquota = reddito * TASSA_SC1
if reddito <= SCAGLIONE2 :
    aliquota = SCAGLIONE1 * TASSA_SC1 + (reddito - SCAGLIONE1)* TASSA_SC2
else:
    aliquota = SCAGLIONE1 * TASSA_SC1 + (SCAGLIONE2-SCAGLIONE1)*TASSA_SC2 + (reddito - SCAGLIONE2) * TASSA_SC3
print("Le tue tasse sono ",aliquota,"euro")
