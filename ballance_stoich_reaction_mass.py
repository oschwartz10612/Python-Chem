from chempy import balance_stoichiometry  # Main reaction in NASA's booster rockets:
from pprint import pprint
from helper import sigRound, getMolarMass

#Ammonia  chemically reacts with oxygen gas  to produce nitric oxide  and water .
#What mass of water is produced by the reaction of  of oxygen gas?

reac, prod = balance_stoichiometry({'NH3', 'O2'}, {'NO', 'H2O'})

want = 'H2O'
have = {
    "name": "O2",
    "mass": 5.6
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
