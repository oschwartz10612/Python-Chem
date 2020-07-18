from chempy import balance_stoichiometry  # Main reaction in NASA's booster rockets:
from pprint import pprint
from helper import sigRound

reac, prod = balance_stoichiometry({'C8H18', 'O2'}, {'H2O', 'CH3COOH'})


want = 'H2O'
have = {
    "name": "C8H18",
    "moles": 2.2
}
sigs = 2

reac = dict(reac)
prod = dict(prod)
everything = {**reac, **prod}

moles = everything[want]/everything[have["name"]]*have["moles"]
print(sigRound(moles, sigs))
