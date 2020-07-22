from helper import getMolarMass


#Compound X has a molar mass of Y and the following composition:
# element	mass %
# carbon	40.00%
# hydrogen	6.71%
# oxygen	53.29%
# Write the molecular formula of X.

mass = 180.16
table = {
    "C": 40,
    "H": 6.71,
    "O": 53.29
}

moles = {}
for element, percent in table.items():
    moles[element] = (percent/getMolarMass(element, 3))

lowest = moles[min(moles, key=moles.get)]
for element, percent in moles.items():
    print(percent/lowest)

wholeNumber = int(input("Enter whole number: \n"))

for element, percent in moles.items():
    moles[element] = (round(percent/lowest*wholeNumber))

formula = ''
for element, percent in moles.items():
    formula = formula + element + str(int(percent))

n = round(mass/getMolarMass(formula, 5), 1)
formula = ''
for element, percent in moles.items():
    formula = formula + element + str(int(percent*n))

print(formula)
