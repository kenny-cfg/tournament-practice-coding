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
