'''
Created on Aug 27, 2018
# futval.py
# A program to compute the value of an investment
# carried 10 years into the future
24 CHAPTER 2. WRITING SIMPLE PROGRAMS
# by: John M. Zelle
@author: ECOLINNA
'''


def main():
    print "This program calculates the future value of a 10-eyar investment"
    
    principal = input("enter the initial principal: ")
    apr = input("Enter the annunalized interest rate: ")
    
    for i in range(10):
        principal = principal * (1 + apr)
        
    print "The amount in 10 years is: ", principal
    
main()
