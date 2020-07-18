from chempy import balance_stoichiometry  # Main reaction in NASA's booster rockets:
from pprint import pprint
from helper import sigRound, getMolarMass

reac, prod = balance_stoichiometry({'NH3', 'H3PO4'}, {'(NH4)3PO4'})

want = '(NH4)3PO4'
have = {
    "name": "NH3",
    "mass": 4.1
}
sigs = 3

reac = dict(reac)
prod = dict(prod)
everything = {**reac, **prod}

have["moles"] = getMolarMass(have["name"], 6)

molesConsumed = have["mass"]/have["moles"]

resConsumed = molesConsumed*(everything[want]/everything[have["name"]])

moles = resConsumed * getMolarMass(want, 6)

print(moles)
