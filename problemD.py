import random
import string

def create_crossword(words):
    grid = [[None for _ in range(10)] for _ in range(10)] # initialize a blank 10x10 grid with none values 
    
    directions = [
        (0,1), # horizontal from left to right
        (1,0), # vertical from top to bottom 
        (1,1), # diagional from top left to bottom right 
        (0,-1),
        (-1,0),
        (-1,-1),
        (1,-1),
        (-1,1)
    ]