"""
Exercise 8 - Rock Paper Scissors
Level - X X X

Make a two-player Rock-Paper-Scissors game.
"""

game_end = False
winner = ""

def gameProcessor(player1, player2, game_end):
    dictionary = {
        1:"Rock",
        2:"Paper",
        3:"Scissors"
    }
    Message = ""
    if player1 == player2:
        Message = "Draw game! Play another round!"
        winner = ""
        game_end = False
    elif player1 == 1 and player2 == 2:
        winner = "Player 2"
        Message = "{} beats {}! {} wins the game!".format(dictionary.get(player2), dictionary.get(player1), winner)
        game_end = True
    elif player1 == 1 and player2 == 3:
        winner = "Player 1"
        Message = "{} beats {}! {} wins the game!".format(dictionary.get(player1), dictionary.get(player2), winner)
        game_end = True
    elif player1 == 2 and player2 == 3:
        winner = "Player 2"
        Message = "{} beats {}! {} wins the game!".format(dictionary.get(player2), dictionary.get(player1), winner)
        game_end = True
    elif player1 == 2 and player2 == 1:
        winner = "Player 1"
        Message = "{} beats {}! {} wins the game!".format(dictionary.get(player1), dictionary.get(player2), winner)
        game_end = True
    elif player1 == 3 and player2 == 1:
        winner = "Player 2"
        Message = "{} beats {}! {} wins the game!".format(dictionary.get(player2), dictionary.get(player1), winner)
        game_end = True
    elif player1 == 3 and player2 == 2:
        winner = "Player 2"
        Message = "{} beats {}! {} wins the game!".format(dictionary.get(player1), dictionary.get(player2), winner)
        game_end = True

    print(Message)

    return(game_end)

while game_end == False:
    print("game_end: " + str(game_end))
    player1 = int(input("player 1, pick a move! [1] - Rock, [2] - Paper, [3] - Scissors: "))
    player2 = int(input("player 2, pick a move! [1] - Rock, [2] - Paper, [3] - Scissors: "))
    
    game_end = gameProcessor(player1, player2, game_end)


