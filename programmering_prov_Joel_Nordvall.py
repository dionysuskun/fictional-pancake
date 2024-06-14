# På en teater kan man antingen köpa ett årskort
# eller köpa en biljett vid varje besök.
# Skapa ett program som läser in priset för ett årskort, priset för en biljett
# samt antalet gånger man planerar att besöka teatern under ett år.
# Därefter skall programmet ange om det lönar sig att köpa årskort eller inte.

biljett = int(input("Pris för biljett: "))
årskort = int(input("Pris för årskort: "))
antal_besök = int(input("Antal teaterbesök per år: "))
skillnad = biljett * antal_besök - årskort


print("En biljett kostar", biljett, "SEK. Priset för ett årskort är", årskort, "SEK.")
print("Mellanskillnaden är", skillnad, "SEK.")

if (skillnad) > 0:
    print("Du tjänar på att köpa ett årskort.")
elif (skillnad) == 0:
    print("Du varken tjänar eller förlorar på att köpa ett årskort.")
else:print("Du tjänar inte på att köpa ett årskort")
    



    


    
    
    
    

