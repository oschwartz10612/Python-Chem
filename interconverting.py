from helper import getMolarMass
from helper import getSciNotation

#Calculate the mass of diphosphorus pentoxide  that contains a billion  phosphorus atoms.

molarMass = getMolarMass('P2O5', 6)
atoms = 1*10**9
mass = 150
count = 2 # = what you are trying to find for mass and what you have for atoms

moles = mass/molarMass
res = moles * count * (6.0221 * 10**23)

print('Amount of atoms:')
print(getSciNotation(res))

moles = atoms/(6.0221 * 10**23)
res = moles / count * molarMass

print('Mass:')
print(getSciNotation(res))