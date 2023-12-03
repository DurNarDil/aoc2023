from variables import *

lineList = input.split("\n")
digitSum = 0
for index,line in enumerate(lineList):
    value = game_info(line)
    if value:
      digitSum = digitSum + index +1
    
print(digitSum)
                
