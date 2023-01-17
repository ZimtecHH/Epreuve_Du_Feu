import re

def calculate(expression):
    # utilise une expression régulière pour remplacer tous les espaces en blanc par des vide
    expression = re.sub(r'\s', '', expression)
    # évalue l'expression en utilisant la fonction eval()
    result = eval(expression)
    return result

print(calculate("4 + 21 * (1 - 2 / 2) + 38"))
