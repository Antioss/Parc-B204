parc = [
    {"nom": "PC01", "ram": 8, "en_panne": False},
    {"nom": "PC02", "ram": 16, "en_panne": True},
    {"nom": "PC03", "ram": 4, "en_panne": False},
    {"nom": "PC04", "ram": 32, "en_panne": False},
    {"nom": "PC05", "ram": 8, "en_panne": True},
]

def nb_en_panne(parc):
    compteur_panne2 = 0
    for pc in parc:
        if pc["en_panne"] == True:
            compteur_panne2 += 1
    return(compteur_panne2)

def ram_moyenne(parc):
    total = 0
    for pc in parc:
        total += pc["ram"]
    moyenne = total / len(parc)
    return moyenne