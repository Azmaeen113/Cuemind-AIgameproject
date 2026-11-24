import unittest

from game import config as C
from game.rules import Match


class MatchRulesTests(unittest.TestCase):
    def setUp(self):
        self.match = Match.new(("A", "B"), seed=1)

    def test_clean_pot_scores_and_keeps_turn(self):
        after = self.match.table.copy()
        after.pocket_of[1] = 0
        after.alive[1] = False
        after.first_hit[0] = 1

        report = self.match.apply_result(after)

        self.assertEqual(report.points, C.ball_points(1))
        self.assertFalse(report.foul)
        self.assertTrue(report.keeps_turn)
        self.assertEqual(self.match.turn, 0)
        self.assertEqual(self.match.scores[0], C.ball_points(1))

    def test_scratch_is_penalized_and_grants_ball_in_hand(self):
        after = self.match.table.copy()
        after.pocket_of[0] = 0
        after.pocket_of[1] = 1
        after.alive[0] = False
        after.alive[1] = False
        after.first_hit[0] = 1

        report = self.match.apply_result(after)

        self.assertTrue(report.foul)
        self.assertEqual(report.points, C.ball_points(1) - C.FOUL_POINTS)
        self.assertEqual(self.match.clocks[0], C.MATCH_CLOCK - C.FOUL_SECONDS)
        self.assertEqual(self.match.fouls[0], 1)
        self.assertTrue(self.match.ball_in_hand)
        self.assertEqual(self.match.turn, 1)

    def test_no_contact_is_a_foul_and_passes_turn(self):
        after = self.match.table.copy()
        after.first_hit[0] = -1

        report = self.match.apply_result(after)

        self.assertTrue(report.no_contact)
        self.assertTrue(report.foul)
        self.assertEqual(report.points, -C.FOUL_POINTS)
        self.assertEqual(self.match.turn, 1)
        self.assertTrue(self.match.ball_in_hand)

    def test_clock_expiration_ends_match_when_both_clocks_are_empty(self):
        self.match.clocks = [0.1, 0.0]

        expired = self.match.tick(0.1)

        self.assertTrue(expired)
        self.assertTrue(self.match.over)
        self.assertEqual(self.match.clocks[0], 0.0)


if __name__ == "__main__":
    unittest.main()
