from helper import sigRound, find_sigFigs

emptyWeight = 4.2
weight = 60.273
volume = 184.0

numberOfSigDecimals = 1


mass = weight - emptyWeight

res = mass / volume

sigs = []
sigs.append(find_sigFigs(round(mass, numberOfSigDecimals)))
sigs.append(find_sigFigs(round(volume, numberOfSigDecimals)))
sigs.sort()

print(sigs[0])
print(sigRound(res, sigs[0]))