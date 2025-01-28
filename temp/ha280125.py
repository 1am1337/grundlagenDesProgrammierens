dDur = {"d","e","fis","g","a","h","c"}
bDur = {"b","c","d","es","f","g","a"}
print("Diese Töne sind in beiden Tonleiten enthalten: ", dDur.intersection(bDur))
print("Diese Töne gibt es nur in D-Dur:", dDur.difference(bDur))
print("Diese Töne gibt es nur in B-Dur:", bDur.difference(dDur))