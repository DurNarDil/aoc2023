from variables import *

lineList = input.split("\n")
digitSum = 0
for line in lineList:
    digits = concat_first_last_digit(line)
    # digits = concat_first_last_digit_or_spelled_out(line)
    digitSum = digitSum + int(digits)
    
print(digitSum)
                
