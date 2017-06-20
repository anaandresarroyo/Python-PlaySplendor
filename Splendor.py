# -*- coding: utf-8 -*-
"""
Created on Mon Jan 02 19:20:17 2017

@author: Ana Andres-Arroyo

'Artificial intelligence' which plays the board game Splendor.
"""
class Development_Cards:
    def __init__(self, level, color, points, price, detailed_price):
        self.level = level # integer
        self.color = color # string
        self.points = points # integer
        self.price = price # integer
        self.detailed_price = detailed_price # instance of the Gems class
        
class Gems:
    def __init__(self,green,blue,red,white,black,yellow):
        self.ammount = {"green": green, 
                     "blue": blue, 
                     "red": red, 
                     "white": white, 
                     "black": black, 
                     "yellow": yellow,
                     }
    
    
class Table:
    def __init__(self,players):
        print "Creating an instance of the Table class."
        
        self.players = players # number of players (2-4)
        
        self.gems = Gems(green=7, 
                         blue=7, 
                         red=7, 
                         white=7, 
                         black=7, 
                         yellow=5,
                         )
                         
        if self.players = 2:
            self.gems = Gems(4,4,4,4,4,5)
        elif self.players = 3:
            self.gems = Gems(5,5,5,5,5,5)
        elif self.players = 4:
            self.gems = Gems(7,7,7,7,7,5)
        else:
            print "WRONG NUMBER OF PLAYERS!"
                
        
        self.cards = []
        self.cards.append(Development_Cards(level=1, 
                                            color="black", 
                                            points=0, 
                                            price=4,
                                            detailed_price=Gems(1,1,1,1,0,0),
                                            ))
        self.cards.append(Development_Cards(level=1, 
                                            color="black", 
                                            points=0, 
                                            price=5,
                                            detailed_price=Gems(1,2,1,1,0,0),
                                            ))
                                            
class Player:
    def __init__(self):
        print "Creating an instance of the Player class."
        self.gems = Gems(0,0,0,0,0,0)
        
    def take_turn(self):
        self.gems.ammount["white"] += 1
        self.gems.ammount["blue"] += 1
        print "Player takes turn"

class Splendor:
    def __init__(self,players):
        print "Creating an instance of the Splendor class."
        
        
    

if __name__ == "__main__":
    print(__doc__)
    
    sp = Splendor(4)
    pl = Player()
    
    print sp.gems.ammount