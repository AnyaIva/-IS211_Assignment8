import random
import datetime
import time
start = datetime.datetime.now()
from self import self


def throw_the_die(sides=6):
    """
    Simulate throwing a die

    :param sides: number of sides
    :return: Values
    """
    return random.randint(1, sides)


class Player:
    def __init__(self, name):
        self.name = name
        self.total = 0
        self.turn_total = 0
        self.roll_hold = 'r'

    def show(self):
        print(f"{self}")

    def __str__(self):
        """String representation"""
        return f"{self.name}'s Total = {self.total}"

    def turn(self):
        """
        Play one turn

        :return:
        """
        turn_total = 0
        roll_hold = 'r'
        while roll_hold != "h":
            die = throw_the_die()
            if die == 1:
                print('You rolled a 1, your turn is over!')
                break

            turn_total += die
            print('You rolled a:', die)
            print('Total points after this turn:', turn_total)
            print('Score if hold:', self.total + turn_total)
            print('Your total score:', self.total)
            roll_hold = input("Roll(r) or Hold(h)? ").lower()

        if roll_hold == 'h':
            # update the player's total
            self.total += turn_total

        self.show()


class ComputerPlayer(Player):

    def __init__(self, name):
        super().__init__(name)

    def turn(self):
        """
        Computer player turn
        :return:
        """
    turn_total = 0

    roll_hold = 'r'
    while roll_hold != 'h':
        die = throw_the_die()
        if die == 1:
            print("Computer rolled a 1, it's turn is over!")

            break

        turn_total += die
        print('Computer rolled a:', die)
        print('Total points after this turn:', turn_total)
        print('Score if hold:', self.total + turn_total)
        print('Computer total score:', self.total)
        roll_hold = input("Roll(r) or Hold(h)? ").lower()

        if turn_total >= 25:
            roll_hold = "h"
        if self.total + turn_total >= 100:
            roll_hold = "h"

    if roll_hold == "h":
        self.total += turn_total

    self.show()


class Game:
    def __init__(self, player1, player2):
        self.players = [player1, player2]
        self.winner = None

    def check_winner(self):
        """
        Returns true if there is winner
        :return:
        """
        for player in self.players:
            if player.total >= 100:
                self.winner = player
                return True

        return False
    def play_game(self):
        current_player = self.players[0]
        while not self.check_winner():
            for player in self.players:
                current_player = player
                current_player.turn()
                if player.total >= 100:
                    break

        print(self.winner.name, "is a winner!")


class TimedGame(Game):

    def __init__(self, player1, player2, time_limit):
        super().__init__(player1, player2)
        self.start_time = datetime.datetime.now()
        self.time_limit = time_limit

    def check_time(self, time_now):
        """
        Check for the time
        :return: True if time expired
        """
        return (time_now - self.start_time).total_seconds() > self.time_limit


def check_winner(self):
    t = time.localtime()
    current_time = time.strftime("%H:%M:%S")
    print(current_time)

    for player in self.players:
        while player.total >= 100:
            self.winner = player
            return True


def play_game(self):
    current_player = self.players[0]
    time_flag = False
    while not self.check_winner() or not time_flag:
        current_player.play()



        if current_player == self.players[0]:
            current_player = self.players[1]
        else:
            current_player = self.players[0]
        if (datetime.datetime.now() - start).seconds > 60:
            print("The scores are:" + str(self.players[0].total) + " " + str(self.players[1].total))
            if self.players[0].total > self.players[1].total:
                print(str(self.players[0].name), "is a winner!")
            else:
                print(str(self.players[1].name), "is a winner!")
            break

    print(self.winner.name, "is a winner!")




def make_player(player_type, player_name):
    """
    Factory function

    :param player_type:
    :param player_name:
    :return:
    """
    if player_type.upper() == 'C':
        return ComputerPlayer(player_name)
    elif player_type.upper() == 'H':
        return Player(player_name)
    else:
        raise ValueError("I don't know what to build!!!!")


if __name__ == '__main__':
    print('Welcome to the game!')
    p1 = make_player('h', "John")
    p2 = make_player('c', "HAL")

    pig_game = Game(p1, p2)
    pig_game.play_game()

