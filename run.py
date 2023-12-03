from variables import *

lineList = input.split("\n")
digitSum = 0
for index,line in enumerate(lineList):
      digitSum += get_game_power(line)
    
print(digitSum)
                
