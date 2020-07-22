from helper import sigRound, getMolarMass
from pint import UnitRegistry
ureg = UnitRegistry()

#A brick has a mass of x and the Earth has a mass of y.

mass1 = 4 * ureg.kg
mass2 = 6*10**27 * ureg.g

molarMass1 = mass1.to_base_units()*(6.02214*10**23)

print(sigRound(molarMass1.to(ureg.g).magnitude, 3))

moles = mass2.to_base_units()/molarMass1

print(sigRound(moles, 2))