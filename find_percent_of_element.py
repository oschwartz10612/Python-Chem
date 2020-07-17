from helper import sigRound

sub1 = 75
sub2 = 78
sub3 = 24
sigFigs = 2

total = sub1+sub2+sub3

print(sigRound(sub1/total*100, sigFigs))
print(sigRound(sub2/total*100, sigFigs))
print(sigRound(sub3/total*100, sigFigs))

