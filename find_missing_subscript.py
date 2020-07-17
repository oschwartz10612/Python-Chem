import math
from pint import UnitRegistry
ureg = UnitRegistry()

sub = 1
moles1 = 5.7
moles2 = 2.81

res = round(sub*(moles1/moles2), 1)

print(res)