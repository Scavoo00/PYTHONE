voti = []
print("Inserisci voti")
print("Termina con exit")
riga = input()
while riga.isdigit() :
    voti.append(int(riga))
    riga = input()
voti.remove(min(voti))
voti.remove(max(voti))
print("La media dei voti è", sum(voti)/len(voti))
for voto in voti :
    print(voto)
