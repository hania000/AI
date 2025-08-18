#Assignment 1

#Question 1

#Convert tenperature from celsius to fahrenheit

celsius=input("temperature=")

print("temperature in fahrenheit is:",int(celsius)*float(9/5)+int(32))

#Question 2 

#Calculate area of a rectangular


l =input("enter lenght=")
b =input("enter breadth=")
print("area of reactangle is:",int(l)*int(b))

#Question 3

#Calcuate Compound Interest

P=input("enter Principle=")
R=input("enter Rate=")
T=input("enter Time=")
print("compound interest is:",int(P)*(int(1)+float(int(R)/100))**int(T)-int(P))

#Question 4

#Calculate perimeter of a rectangular

L=input("Enter length=")
B=input("Enter breadth=")
print("Perimeter of rectangle is:",int(L)+int(B))

#Question 5 

#Calculate average of three numbers

A=input("Enter number=")
B=input("Enter number=")
C=input("Enter number=")
print("average of numbers is:",(int(A)+int(B)+int(C))/3)

#Question 6

#Calculate square and cube of a number

A =input("Enter number=")
print("Square of number is:", int(A)*int(A))
print("Cube of number is:", int(A)*int(A)*int(A))

#Question 7 

#Distribute items equally

N =input("Enter number of candies=")
M =input("Enter number of students=")
print("Distribution of candies equally:",int(N),int(M))
print("Cadies left:", int(N) % int(M))

#Question 8

#CALCULATE PROFIT OR LOSS

A=input("Enter cost price=")
B=input("Enter selling price=")
if A < B : 
    print("profit")
else :  
    print("loss")
    
#Question 9 

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

#Question 10

#Calculate Salary

B=input("Enter basic salary=")

HRA=(0.20*int(B))
DA=(0.15*int(B))
Totalsalary=int(B)+float(HRA)+float(DA)

print("HRA:",HRA)
print("DA:",DA)
print("total salary:",Totalsalary)

#Question 11

#Calculate age in monthes and days

A=input("Enter your age=")
print("age in months:", int(A)*12)
print("age in days:", int(A)*365)

#Question 12

#Convert currency (USD TO PKR)

R=input("Enter amount in USD=")
USD=int(R)*283.5
print("PKR=",USD)

#Question 13

#calculate sum of first N natural numbers

N=input("Enter a number=")
sum=int(N)*(int(N)+1)/2
print("sum",sum)


#Question 14

#Calculate percentage of correct answers

T=input("Enter total number of questions=")
C=input("Enter number of correct questions=")

percentage=(int(C)/int(T))*100
print("percentage",percentage)


#Question 15

#calculate speed , distance , time

d=input("Enter distance=")
t=input("Enter time=")
print("Speed is:", int(d)/int(t))


#Question 16

#calculate body mass

W=input("Enter weight=")
H=input("Enter height=")
print("BMI is:", float(W)/(float(H)*2))

#Question 17 

#converts minutes to hours and minutes

M =input("Enter minutes=")
print("No of hours:", int(M)//60)
print("No of minutes:", int(M)%60)




    
    








