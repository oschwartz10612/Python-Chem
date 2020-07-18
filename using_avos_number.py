from helper import sigRound, getMolarMass
from pint import UnitRegistry
ureg = UnitRegistry()


mass1 = 2.5 * ureg.g
mass2 = 7.35*10**22 * ureg.kg

molarMass1 = mass1.to_base_units()*(6.02214*10**23)

print(sigRound(molarMass1.to(ureg.g).magnitude, 3))

moles = mass2.to_base_units()/molarMass1

print(sigRound(moles, 3))