'''
Created on Aug 27, 2018
# avg2.py
# A simple program to average two exam scores
# Illustrates use of multiple input
Example from chapter 2
@author: ECOLINNA
'''
def main():
    print "This program computes the average of two exam scores."
    
    score1, score2 = input("Enter two scores separated by a comma: ")
    average = (score1 + score2) / 2.0
    
    print "The average of the score is: ", average
    
main()

