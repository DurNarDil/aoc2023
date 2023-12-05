input='''467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598..'''

# Conditions
numbers = []

def process_string(line, lineList, lineIndex, lineListLenght):
    partNumber = ''
    skipStep = 0
    for index,char in enumerate(line):
        if skipStep > 0:
            skipStep -= 1
            continue
        if char.isdigit():
            partNumber = partNumber + char
            if check_for_symbols(lineIndex, index, lineList, line, lineListLenght):
                skipStep = get_whole_number(line, partNumber, index)
                partNumber = ''
            

# Check around the digit for symbols            
def check_for_symbols(lineIndex, charIndex, lineList, line, lineListLenght):
    lineLenght = len(line)
    safeBehind = charIndex -1 > -1
    safeTop = lineIndex > 0
    safeBottom = lineListLenght - 1 > lineIndex
    safeForward = lineLenght > charIndex
    # Safe to check behind
    if safeBehind:
        if is_symbol(line[charIndex - 1]):
            return True
    if safeBehind and safeTop:
        if is_symbol(lineList[lineIndex - 1][charIndex - 1]):
            return True
    if safeBehind and safeBottom:
        if is_symbol(lineList[lineIndex + 1][charIndex - 1]):
            return True
    
    # Safe to check forward
    if safeForward:
        if is_symbol(line[charIndex + 1]):
            return True
    if safeForward and safeTop:
        if is_symbol(lineList[lineIndex - 1][charIndex + 1]):
            return True
    if safeForward and safeBottom:
        if is_symbol(lineList[lineIndex + 1][charIndex + 1]):
            return True
    
    # Safe to check top and bottom
    if safeBottom:
        if is_symbol(lineList[lineIndex + 1][charIndex]):
            return True
    if safeTop:
        if is_symbol(lineList[lineIndex - 1][charIndex]):
            return True

    return False
    
# Check if char is symbol    
def is_symbol(lineChar):
    if not lineChar.isdigit() and lineChar != '.':
        return True
    return False

# Get the complete number once 
def get_whole_number(line, partNumber,charIndex):
    step = 1
    for charIndex in range(charIndex, len(line)):
        if line[charIndex+1].isdigit():
            partNumber += line[charIndex+1]
            step += 1
        else:
            numbers.append(partNumber)
            return step
        
def sum_string_ints(numbers):
    total = 0
    for value in numbers:
        try:
            # Attempt to convert the string to an integer and add to the total
            total += int(value)
        except ValueError:
            # Handle the case where the string cannot be converted to an integer
            print(f"Skipping non-integer value: {value}")

    return total
            