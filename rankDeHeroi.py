nomeHeroi = "Cauly"
xpHeroi = 8000
frase1 = "O herói de nome "
frase2 = " está no nível de "
rankHeroi = ["Ferro", "Bronze", "Prata", "Ouro", "Platina", "Ascendente", "Imortal", "Radiante"]

if xpHeroi < 1000:
    print(frase1 + nomeHeroi + frase2 + rankHeroi[0] + ".")

elif xpHeroi > 1001 and xpHeroi <= 2000:
    print(frase1 + nomeHeroi + frase2 + rankHeroi[1] + ".")

elif xpHeroi > 2000 and xpHeroi <= 5000:
    print(frase1 + nomeHeroi + frase2 + rankHeroi[2] + ".")

elif xpHeroi > 5000 and xpHeroi <= 7000:
    print(frase1 + nomeHeroi + frase2 + rankHeroi[3] + ".")

elif xpHeroi > 7000 and xpHeroi <= 8000:
    print(frase1 + nomeHeroi + frase2 + rankHeroi[4] + ".")

elif xpHeroi > 8000 and xpHeroi <= 9000:
    print(frase1 + nomeHeroi + frase2 + rankHeroi[5] + ".")

elif xpHeroi > 9000 and xpHeroi <= 10000: 
    print(frase1 + nomeHeroi + frase2 + rankHeroi[6] + ".")

else:
    xpHeroi >= 10001
    print(frase1 + nomeHeroi + frase2 + rankHeroi[7] + ".")
