# Übungsaufgabe bis nächste Woche

# - Schreibt ein Programm, in dem ihr zwei Sets definiert. Diese sollen die
#   Notennamen der Tonleitern D-Dur nd B-Dur (b-flat) als Strings enthalten.
# - Das Programm soll ausgeben:
# 	- Welche Töne beide Töne gemeinsam haben.
# 	- Welche Töne es nur in D-Dur gibt.
# 	- Welche Töne es nur in B-Dur gibt.
dDur = {"D","E", "FIS","G","A", "H","CIS"}
bDur = {"B", "C", "D", "ES", "F", "G", "A"}
print("Diese Noten sind in beiden Tonleitern: ", dDur.intersection(bDur), "\nDiese Noten gibt es nur in D-Dur: ", dDur.difference(bDur), "\nDiese Noten gibt es nur in B-Dur: ", bDur.difference(dDur))

