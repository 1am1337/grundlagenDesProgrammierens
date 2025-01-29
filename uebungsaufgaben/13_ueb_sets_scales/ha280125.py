dDur = {"D","E", "FIS","G","A", "H","C"}
bDur = {"B", "C", "D", "ES", "F", "G", "A"}
print("Diese Noten sind in beiden Tonleitern: ", dDur.intersection(bDur))
print("Diese Noten gibt es nur in D-Dur: ", dDur.difference(bDur))
print("Diese Noten gibt es nur in B-Dur: ", bDur.difference(dDur))
