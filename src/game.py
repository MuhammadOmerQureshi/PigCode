from player import Player
from intelligence import Intelligence
from high_score import HighScore
from histogram import Histogram
from dice_hand import DiceHand
from dice import Dice


class Game:
    def __init__(self, players):
        self.players = players
        self.high_score = HighScore(Histogram())

    def play_round(self):
        while True:
            for player in self.players:
                result = self.play_turn(player)
                if result == "quit":
                    return "quit"
                if player.score >= 100:
                    return player

    def play_turn(self, player):
        print(f"\n{player.name}'s turn 🎮")
        while True:
            if player.intelligence:
                # Computer player logic
                player.roll_dice()
                if player.decide_hold() or player.dice_hand.turn_score == 0:
                    player.hold()
                    break
            else:
                # Human player logic
                action = self.get_player_action(player)
                if action in ['r', 'h', 'c', 'q']:
                    if action == 'r':
                        if player.roll_dice() == 1:
                            break
                    elif action == 'h':
                        player.hold()
                        break
                    elif action == 'c':
                        player.cheat()
                    elif action == 'q':
                        return "quit"
                    if player.score >= 100:
                        break

    def get_player_action(self, player):
        valid_actions = {'r', 'h', 'c', 'q'}
        while True:
            action = input(f"{player.name}, roll, hold, or cheat? (r/h/c) or quit game (q): ").lower().strip()
            if action in valid_actions:
                return action
            print("Invalid input, please enter 'r', 'h', 'c', or 'q'.")

def setup_game():
    print("Welcome to Dice game")
    player1_name = input("Enter Player 1's name: ").strip()
    player1 = Player(player1_name)
    game_mode = input("Play against (1) Computer or (2) another Player? ").strip()

    if game_mode == "1":
        threshold = get_int_input("Choose computer intelligence threshold (1-30): ", 20)
        intelligence = Intelligence(threshold)
        player2 = Player("Computer", intelligence=intelligence)
    else:
        player2_name = input("Enter Player 2's name: ").strip()
        player2 = Player(player2_name)

    return [player1, player2]

def get_int_input(prompt, default):
    try:
        return int(input(prompt))
    except ValueError:
        print(f"Invalid input. Setting to default ({default}).")
        return default

def main():
    players = setup_game()
    game = Game(players)
    while True:
        winner = game.play_round()
        if winner == "quit":
            print("Game has been quit.")
            break
        elif winner:
            print(f"🏆 {winner.name} wins with a score of {winner.score}!")
            game.high_score.update_highscore(winner)
            game.high_score.histogram.display_highscores()

        if input("Do you want to play again? (yes/no): ").lower().strip() != 'yes':
            print("Thanks for playing! 🖐️")
            break
        else:
            for player in players:
                player.reset()

if __name__ == "__main__":
    main()
