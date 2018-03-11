# This program computes multiplication of two algorithms using Karatsuba's algorithm in a
# a recursive fashion.
# Author - Ashutosh Grewal
# Date - Mar 10, 2018

import math

# Define the numbers whose product we wish two compute.
#number1 = 3141592653589793238462643383279502884197169399375105820974944592 
#number2 = 2718281828459045235360287471352662497757247093699959574966967627 
number1 = 371 
number2 = 234

# Find the # of digits in a number
def getDigits(num):
    numDigits = int(math.log10(num)) + 1
    return numDigits

# Perform Karastuba's multiplication
def doKaratsubaMultiplication(num1, num2):
    print("****Start****")
    print("num 1",num1,"num 2",num2); 

    #If either number is 0, the answer is 0
    if num1 == 0 or num2 == 0:
        return 0;

    num1Digits = getDigits(num1)
    num2Digits = getDigits(num2)

    print ("num 1 has", num1Digits,"digits while num 2 has", num2Digits)

    #Find the maximum # of digits from either #
    maxDigits = max(num1Digits, num2Digits)

    print("The max digits from either # is", maxDigits)

    #If either of the #s has a single digit, this is the base case for
    #this recursion. Just return the multiplication product by usual
    #computation.
    if maxDigits == 1:
        print("Base case")
        result = num1 * num2
        print("result =", result)
        return result; 

    #If neither of the #s has a single digit, this is the recursive case.
    print("Recursive case")

    #Splitting the Numbers using 10 to the power of (maxDigits - 1)/2 as the divisor
    divisor = 10**(int(maxDigits/2))
    print("The divisor 10**(maxDigits/2) is",divisor)

    #num1 = num1Highnum1Low
    num1High = num1 / divisor 
    num1Low = num1 % divisor

    #num2 = num2Highnum2Low
    num2High = num2 / divisor
    num2Low = num2 % divisor

    print("num 1",num1,"divided by",divisor," has",num1High," as" 
            " quotient and",num1Low,"as remainder")
    print("num 2",num2,"divided by",divisor," has",num2High," as" 
            " quotient and",num2Low,"as remainder")

    #The # that gets multipled by divisor to power of 2. 
    #Note - raising it to maxDigits will not be correct if maxDigits was odd.
    highBitsMultiplication = doKaratsubaMultiplication(num1High, num2High)

    #The # that is used without any multiplication.
    lowBitsMultiplication = doKaratsubaMultiplication(num1Low, num2Low)

    #The # that is multipled by divisor.
    highLowMultiplication = doKaratsubaMultiplication((num1High + num1Low), (num2High + num2Low)) - highBitsMultiplication - lowBitsMultiplication 

    print("highBitsMultiplication = ",highBitsMultiplication)
    print("lowBitsMultiplication = ",lowBitsMultiplication)
    print("highLowMultiplication = ",highLowMultiplication)

    #Karastuba's calculation
    result = highBitsMultiplication * (divisor**2) + highLowMultiplication * (divisor) + lowBitsMultiplication 
    print("result =", result)
    print("****End****")

    return result;

print(number1,"*",number2,"=",doKaratsubaMultiplication(number1,number2))
