from variables import *

lineList = input.split("\n")
lineListLenght = len(lineList)
digitSum = 0
for index,line in enumerate(lineList):
      process_string(line, lineList, index, lineListLenght)
    
print(sum_string_ints(numbers))
                
