'''
Created on Aug 27, 2018

# change.py
# A program to calculate the value of some change in dollars

Chapter 3


@author: ECOLINNA
'''
def main():
    print "Change Counter"
    print
    print "Please enter the count of each coin type."
    quarters = input("Quarters: ")
    dimes = input("Dimes: ")
    nickels = input("Nickels: ")
    pennies = input("Pennies: ")
    total = quarters * .25 + dimes * .10 + nickels * .05 + pennies * .01
    print 
    print "The total value of your change is", total
main()