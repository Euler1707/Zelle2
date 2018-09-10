'''
Created on Aug 27, 2018

Chapter 2 example

convert.py
@author: ECOLINNA
'''

#    A program to convert celcius temps to Fahrenheit

def main():
    celcius = input("What is the Celsius temperature? ")
    fahrenheit = 9.0 / 5.0 * celcius + 32
    print "The temperature is", fahrenheit, "degrees Fahrenheit."

main()