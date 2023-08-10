import unittest

from tournament_winner import tournament_winner


class TestTournamentWinner(unittest.TestCase):
    def test_works(self):
        competitions = [
            ['Panthers', 'Lionesses'],
            ['Lionesses', 'Dolphins'],
            ['Dolphins', 'Panthers']
        ]
        results = [0, 0, 1]

        winner = tournament_winner(competitions, results)

        self.assertEqual('Dolphins', winner)


"""
competitions = [

['Panthers', 'Lionesses'], # Lionesses away-team won - 3 points

['Lionesses', 'Dolphins'], # Dolphins away team won - 3 point

['Dolphins', 'Panthers'], # Dolphins home team won - 3 points

]

results = [0, 0, 1]

Dolphins should be the winner
"""