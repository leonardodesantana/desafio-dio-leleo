nomeHeroi = "Cauly"
xpHeroi = 8000
frasesOutput = [
    "O herói de nome ",
    " está no nível de ",
    "."
]
ranksHeroi = {
    "Ferro": {
        "rank": "Ferro",
        "eloMin": xpHeroi >= 0,
        "eloMax": xpHeroi < 1000
    },
    "Bronze": {
        "rank": "Bronze",
        "eloMin": xpHeroi >= 1001,
        "eloMax": xpHeroi <= 2000
    },
    "Prata": {
        "rank": "Prata",
        "eloMin": xpHeroi >= 2001,
        "eloMax": xpHeroi <= 5000
    },
    "Ouro": {
        "rank": "Ouro",
        "eloMin": xpHeroi >= 5001,
        "eloMax": xpHeroi <= 7000
    },
    "Platina": {
        "rank": "Platina", 
        "eloMin": xpHeroi >= 7001,
        "eloMax": xpHeroi <= 8000
    },
    "Ascendente": {
        "rank": "Ascendente",
        "eloMin": xpHeroi >= 8001,
        "eloMax": xpHeroi <= 9000
    },
    "Imortal": {
        "rank": "Imortal",
        "eloMin": xpHeroi >= 9001,
        "eloMax": xpHeroi < 10000
    },
    "Radiante": {
        "rank": "Radiante",
        "eloMin": xpHeroi >= 10001,
        "eloMax": float('inf')
    }
}
def encontrarRankHeroi():
    for rank, limites in ranksHeroi.items():
        if limites['eloMin'] and limites['eloMax']:
            return limites['rank']
    return "Herói sem rank."

rankDoHeroi = encontrarRankHeroi()
if rankDoHeroi != "Herói sem rank.":
    print(frasesOutput[0] + nomeHeroi + frasesOutput[1] + rankDoHeroi + frasesOutput[2])
else:  print("Herói fora do ranking!")