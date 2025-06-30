#assignment 1.3

#Calcuate Compound Interest

P=input("enter Principle=")
R=input("enter Rate=")
T=input("enter Time=")
print("compound interest is:",int(P)*(int(1)+float(int(R)/100))**int(T)-int(P))
