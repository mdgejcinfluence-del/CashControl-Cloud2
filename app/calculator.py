# Interface Patron conforme Étape 4 du PDF CashControl
def calculate_net(recettes, depenses, fixe_jour, commissions, frais_fixes):
    return recettes - (depenses + fixe_jour + commissions + frais_fixes)
