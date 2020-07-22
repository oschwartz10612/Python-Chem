import math
from pint import UnitRegistry
ureg = UnitRegistry()

#An unknown compound has the following chemical formula:

sub = 3 #Subscript of what we have
moles1 = 7.24
moles2 = 21.35

res = round(sub*(moles1/moles2), 1)

print(res)