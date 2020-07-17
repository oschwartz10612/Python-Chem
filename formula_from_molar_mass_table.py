from helper import getMolarMass

mass = 135.13
table = {
    "C": 44.44,
    "H": 3.73,
    "N": 51.83
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
