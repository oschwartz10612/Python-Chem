from helper import sigRound, find_sigFigs

data = [0.347,21.0,27.3]

total = 0
for num in data:
    total += num

avarage = total/len(data)

print("Total:")
print(find_sigFigs(total))
print(total)

sigs = int(input("Enter sigs number: \n"))

print(sigRound(avarage, sigs))