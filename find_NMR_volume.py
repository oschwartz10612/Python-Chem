import math
from pint import UnitRegistry
ureg = UnitRegistry()

h = 2.84 * ureg.cm
d = 1.8 * ureg.mm

vol = math.pi * (d*.5)**2 * h

vol = vol.to(ureg.ul)

# print(round(vol, 1))
print(vol)