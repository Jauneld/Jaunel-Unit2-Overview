#Jaunel Deans 
#September 26, 2023
#We are calcuating with Python

name = input("Hello user. What is your name? ")
print("Nice to meet you, " + name + ". We are going to make some arithmetic calcutaions.")

# What are the arithmetic opeartors?
##  Addition operator is + (5+2 = 7)
##  Subtraction operator is - (5-2 = 3)
##  Multiplication opearator is * (5*2 = 10)
##  Division operator is / (5/2 = 2.5)
##  Integral/Integer division operator is // ~ doesn't round #, just whole # (5//2 = 2)
##  Remainder operator is % (5%2 = 1)
##  Exponent operator is ** (5**2 = 25)
##  Assignment operator is = 

num1 = int(input("Enter a number: ")) #only number(floats and integers can be calculated)
num2 = int(input("Enter another number: "))


sum = (num1 + num2) #addition 
multi = (num1*num2) #multiplication
divi = (num1/num2) #division 
sub = (num1-num2) #subtraction
remain = (num1%num2) #finds the remainder
integral = (num1//num2) #gives the whole number in the division
power = (num1**num2) #calculates exponents. num1 to the power num2

print("The sum of" , str(num1) , "and" ,str(num2), "is:" , str(sum))
print("The product of" , str(num1) , "and" ,str(num2), "is:" , str(multi))
print("The quotient of" , str(num1) , "and" ,str(num2), "is:" , str(divi))
print("The difference between" , str(num1) , "and" ,str(num2), "is:" , str(sub))
print("The remainder of" , str(num1) , "and" ,str(num2), "is:" , str(remain))
print("The whole number in the quotient of" , str(num1) , "and" ,str(num2), "is:" , str(integral))
print( str(num1) , "to the power of" ,str(num2), "is:" , str(power))
