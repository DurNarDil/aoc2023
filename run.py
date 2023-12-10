from variables import *

lineList = input.split("\n")
lineListLenght = len(lineList)
points = 0
for index,line in enumerate(lineList):
      card = Card(line)
      points += card.points
    
print(points)
                
