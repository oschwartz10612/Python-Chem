import math
import re
from chempy import Substance
from chempy.units import default_units as u

def sigRound(a_number, significant_digits):
    return round(a_number, significant_digits - int(math.floor(math.log10(abs(a_number)))) - 1)

def getMolarMass(formula, roundNumber):
    sub = Substance.from_formula(formula)
    mass = sub.molar_mass(u)
    mass = round(mass, roundNumber)
    return mass

def getSciNotation(number):
    return "{:.4e}".format(number)

def find_sigFigs(x):
    l = len(str(x).replace('.','').strip('0'))
    return l