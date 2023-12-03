input='''Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green'''

# Conditions
# data = [
#     {"color": "red", "limit": 12},
#     {"color": "green", "limit": 13},
#     {"color": "blue", "limit": 14}
# ]

colors = {'red':12, 'green':13, 'blue':14}

#returns true if fits conditions
def game_info(input):
    line = input.split(":")
    games = line[1].split(";")
    for game in games:
        result = process_game(game)
        if not result:
            return False
    return True
        
def process_game(input):
    balls = input.split(",")
    for ball in balls:
        parts = ball.strip().split(' ')
        if int(colors[parts[1]]) < int(parts[0]) :
            return False
    return True