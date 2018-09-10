'''
Created on Aug 28, 2018
IMPROVING BY USING ARRAYS
@author: ECOLINNA
'''

from graphics import *

class DieView:
    """ DieView is a widget that displays a graphical representation
    of a standard six-sided die."""
    def __init__(self, win, center, size):
        """Create a view of a die, e.g.:
    d1 = GDie(myWin, Point(40,50), 20)
    creates a die centered at (40,50) having sides
    of length 20."""
        # first define some standard values
        self.win = win # save this for drawing pips later
        self.background = "white" # color of die face
        self.foreground = "black" # color of the pips
        self.psize = 0.1 * size # radius of each pip
        hsize = size / 2.0 # half the size of the die
        offset = 0.6 * hsize # distance from center to outer pips    
        # create a square for the face
        cx, cy = center.getX(), center.getY()
        p1 = Point(cx-hsize, cy-hsize)
        p2 = Point(cx+hsize, cy+hsize)
        rect = Rectangle(p1,p2)
        rect.draw(win)
        rect.setFill(self.background)
        # Create 7 circles for standard pip locations
        '''
        self.pip1 = self.__makePip(cx-offset, cy-offset)
        self.pip2 = self.__makePip(cx-offset, cy)
        self.pip3 = self.__makePip(cx-offset, cy+offset)
        self.pip4 = self.__makePip(cx, cy)
        self.pip5 = self.__makePip(cx+offset, cy-offset)
        self.pip6 = self.__makePip(cx+offset, cy)
        self.pip7 = self.__makePip(cx+offset, cy+offset)
        
        # Using Lists to Store Objects
        One way of doing it below
        pips = []
        pips.append(self.__makePip(cx-offset, cy-offset))
        pips.append(self.__makePip(cx-offset, cy))
        pips.append(self.__makePip(cx-offset, cy+offset))
        pips.append(self.__makePip(cx, cy))
        pips.append(self.__makePip(cx+offset, cy-offset))
        pips.append(self.__makePip(cx+offset, cy))
        pips.append(self.__makePip(cx+offset, cy+offset))
        self.pips = pips
        '''
        # THE MOST Straight forward way of doing this
        self.pips = [ self.__makePip(cx-offset, cy-offset),
                        self.__makePip(cx-offset, cy),
                        self.__makePip(cx-offset, cy+offset),
                        self.__makePip(cx, cy),
                        self.__makePip(cx+offset, cy-offset),
                        self.__makePip(cx+offset, cy),
                        self.__makePip(cx+offset, cy+offset) ]


        # Create a table for which pips are on for each value
        self.onTable = [ [], [3], [2,4], [2,3,4],
            [0,2,4,6], [0,2,3,4,6], [0,1,2,4,5,6] ]
        
        # Draw an initial value
        self.setValue(1)
    def __makePip(self, x, y):
        "Internal helper method to draw a pip at (x,y)"
        pip = Circle(Point(x,y), self.psize)
        pip.setFill(self.background)
        pip.setOutline(self.background)
        pip.draw(self.win)
        return pip
    
    def setValue(self, value):
        "Set this die to display value."
        # turn all pips off
        '''self.pip1.setFill(self.background)
        self.pip2.setFill(self.background)
        self.pip3.setFill(self.background)
        self.pip4.setFill(self.background)
        self.pip5.setFill(self.background)
        self.pip6.setFill(self.background)
        self.pip7.setFill(self.background)
        '''
        # turn all pips off
        
        for pip in self.pips:
            pip.setFill(self.background)
         
        # turn correct pips on
        '''
        if value == 1:
        self.pip4.setFill(self.foreground)
        elif value == 2:
        self.pip1.setFill(self.foreground)
        self.pip7.setFill(self.foreground)
        elif value == 3:
        self.pip1.setFill(self.foreground)
        self.pip7.setFill(self.foreground)
        self.pip4.setFill(self.foreground)
        elif value == 4:
        self.pip1.setFill(self.foreground)
        self.pip3.setFill(self.foreground)
        self.pip5.setFill(self.foreground)
        self.pip7.setFill(self.foreground)
        elif value == 5:
        self.pip1.setFill(self.foreground)
        self.pip3.setFill(self.foreground)
        self.pip4.setFill(self.foreground)
        self.pip5.setFill(self.foreground)
        self.pip7.setFill(self.foreground)
        else:
        self.pip1.setFill(self.foreground)
        self.pip2.setFill(self.foreground)
        self.pip3.setFill(self.foreground)
        self.pip5.setFill(self.foreground)
        self.pip6.setFill(self.foreground)
        self.pip7.setFill(self.foreground)'''
        
        # turn correct pips on
        for i in self.onTable[value]:
            self.pips[i].setFill(self.foreground)
        
        '''
        for x in something
        
        x takes the place of that value 
        in all of the posible places in something that is a list
        '''
            
            