
import math
def main():
    print "This program finds the real solutions to a quadratic\n"
    try:
        a, b, c = input("Please enter the coefficients (a, b, c): ")
        discRoot = math.sqrt(b * b - 4 * a * c)
        root1 = (-b + discRoot) / (2 * a)
        root2 = (-b - discRoot) / (2 * a)
        print "\nThe solutions are:", root1, root2
        
    except OverflowError:
        print "\nNo real roots"
    except ValueError:
        print "\nYou didn't give me three coefficients."
    except NameError:
        print "\nYou didn't enter three numbers"
    except TypeError:
        print "\nYour inputs were not all numbers"
    except:
        print "\nSomething went wrong, sorry!"
        
main()