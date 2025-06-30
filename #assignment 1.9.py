#assignment 1.9

#Calculate total marks and percentage

sub1=input("Enter marks in sub1=")
sub2=input("Enter marks in sub2=")
sub3=input("Enter marks in sub3=")
sub4=input("Enter marks in sub4=")
sub5=input("Enter marks in sub5=")

TM= (int(sub1)+int(sub2)+int(sub3)+int(sub4)+int(sub5))

print(TM)
print("percentage:",int(TM)/500*100)
print("average:",(int(sub1)+int(sub2)+int(sub3)+int(sub4)+int(sub5))/5)
