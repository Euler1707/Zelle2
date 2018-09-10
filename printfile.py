'''
Created on Aug 27, 2018


Chapter 4 file processing


@author: ECOLINNA
'''

# printfile.py
# Prints a file to the screen.
def main():
    fname = raw_input("Enter filename: ")
    infile = open(fname,'r')
    data = infile.read()
    print data
main()


