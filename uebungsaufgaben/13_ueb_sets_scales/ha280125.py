dDur = {"D","E", "FIS","G","A", "H","CIS"}
bDur = {"B", "C", "D", "ES", "F", "G", "A"}
print("Diese Noten sind in beiden Tonleitern: ", dDur.intersection(bDur), "\nDiese Noten gibt es nur in D-Dur: ", dDur.difference(bDur), "\nDiese Noten gibt es nur in B-Dur: ", bDur.difference(dDur))