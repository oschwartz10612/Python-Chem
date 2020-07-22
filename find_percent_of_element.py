from helper import sigRound

sub1 = 41.8
sub2 = 57.5
sub3 = 2.99
sigFigs = 3

total = sub1+sub2+sub3

print(sigRound(sub1/total*100, sigFigs))
print(sigRound(sub2/total*100, sigFigs))
print(sigRound(sub3/total*100, sigFigs))

