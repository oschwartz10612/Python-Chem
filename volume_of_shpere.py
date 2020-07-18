from helper import sigRound
import math
from pint import UnitRegistry
ureg = UnitRegistry()

d = 10 * ureg.cm

val = (4/3) * 3.14159 * (d/2)**3

ml = val.to(ureg.l)

print(round(ml.magnitude, 3))