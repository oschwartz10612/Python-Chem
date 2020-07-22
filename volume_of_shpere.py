from helper import sigRound
import math
from pint import UnitRegistry
ureg = UnitRegistry()

d = 10 * ureg.cm
roundTo = 3

val = (4/3) * 3.14159 * (d/2)**3

res = val.to(ureg.l)

print(round(res.magnitude, roundTo))