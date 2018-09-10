'''
Created on Aug 27, 2018

Example in Chapter 1


@author: ECOLINNA
'''

# A simple program illustrating chaotic behaviour

def main():
    print "This program illustrates a chaotic function"
    x = input("Enter a number between 0 and 1: ")
    for i in range(10):
        x = 3.9 * x * (1 - x)
        print x 
        
main()

5
