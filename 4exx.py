name = input("Hello, you are stuck in the Magical Maze, what is your name?")
print("Hello " + name)
options = "NSEW"
SOL = "SSNWES"
moves = 0
lives = 3

while True:
    if moves == 10:
        lives -= 1
        moves = 0
    if not lives:
        print("Game Over")
        break

try:
    DIR = input("you are stuck, which way do you want to go? (N,S,E,W)").upper()
    print("You have selected " + DIR)

    if DIR not in options:
        print("You have entered a wrong option, try again")
    if
        # need smthg here that stores moves and reads them
        array = ["N", "S", "E", "W"]
        blahblah = SOL
        print("You successfully escaped the maze in 6 moves!!")