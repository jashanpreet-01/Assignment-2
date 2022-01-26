                   #########  PYTHON ASSIGNMENT 2 ###########

#########Question 1

str = "Python is a case sensitive language"

##a
print(len(str))

##b
print(str[::-1])

##c
print(str[10:27])

##d
print(str.replace("a case sensitive", "object oriented"))

##e
print(str.index("a"))

##f
print(str.replace(" ", ""))

######Question 2

Name = "Jashanpreet singh"
SID = 21104021
DepN = "Electrical"
CGPA = 9.7
# INFO = print(input("Name", "SID", "DepN", "CGPA"))
print("Hey,", Name, "Here!")
print("My SID is", SID)
print("I am from", DepN, "department and my CGPA is", CGPA)

######Question 3
a = 56
b = 10

##a
print(a&b)

##b
print(a|b)

##c
print(a^b)

##d
print(a<<2 and b<<2)

##e
print(a>>2 and b>>4)


######Question 4

n1 = float(input("1st Number: "))
n2 = float(input("2nd Number: "))
n3 = float(input("3rd Number: "))
print("Greatest of the above three is: ", max(n1, n2, n3))


######Question 5

str = input("Enter your string here:")
print("Is 'name' present in the string?")
if "name" in str:
    print("Yes")
else:
    print("No")


#############Question 6

a = float(input("Length of Side1: "))
b = float(input("Length of Side2: "))
c = float(input("Length of Side3: "))
A = int(a)
B = int(b)
C = int(c)
print("Integral value of A: ",A)
print("Integral value of B: ",B)
print("Integral value of C: ",C)
print("Can the triangle be formed?")
if A>=(B+C) or B>=(C+A) or C>=(A+B):
    print("No, Triangle cannot be formed")
else:
    print("Yes, Triangle can be formed")