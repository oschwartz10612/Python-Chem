from chempy import balance_stoichiometry  # Main reaction in NASA's booster rockets:
from pprint import pprint

reac, prod = balance_stoichiometry({'C8H18', 'O2'}, {'CO2', 'H20'})

print('Reactants:')
pprint(dict(reac))
print('Products:')
pprint(dict(prod))