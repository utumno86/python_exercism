import unittest

import hamming


<<<<<<< HEAD
# Tests adapted from `problem-specifications//canonical-data.json` @ v2.0.1

class HammingTest(unittest.TestCase):

    def test_empty_strands(self):
        self.assertEqual(hamming.distance("", ""), 0)

=======
# test cases adapted from `x-common//canonical-data.json` @ version: 1.0.0

class HammingTest(unittest.TestCase):

>>>>>>> 371894dab186cec701ce325dcc4d002c02d93cbd
    def test_identical_strands(self):
        self.assertEqual(hamming.distance("A", "A"), 0)

    def test_long_identical_strands(self):
        self.assertEqual(hamming.distance("GGACTGA", "GGACTGA"), 0)

    def test_complete_distance_in_single_nucleotide_strands(self):
        self.assertEqual(hamming.distance("A", "G"), 1)

    def test_complete_distance_in_small_strands(self):
        self.assertEqual(hamming.distance("AG", "CT"), 2)

    def test_small_distance_in_small_strands(self):
        self.assertEqual(hamming.distance("AT", "CT"), 1)

    def test_small_distance(self):
        self.assertEqual(hamming.distance("GGACG", "GGTCG"), 1)

    def test_small_distance_in_long_strands(self):
        self.assertEqual(hamming.distance("ACCAGGG", "ACTATGG"), 2)

    def test_non_unique_character_in_first_strand(self):
<<<<<<< HEAD
        self.assertEqual(hamming.distance("AAG", "AAA"), 1)

    def test_non_unique_character_in_second_strand(self):
        self.assertEqual(hamming.distance("AAA", "AAG"), 1)
=======
        self.assertEqual(hamming.distance("AGA", "AGG"), 1)

    def test_non_unique_character_in_second_strand(self):
        self.assertEqual(hamming.distance("AGG", "AGA"), 1)
>>>>>>> 371894dab186cec701ce325dcc4d002c02d93cbd

    def test_same_nucleotides_in_different_positions(self):
        self.assertEqual(hamming.distance("TAG", "GAT"), 2)

    def test_large_distance(self):
        self.assertEqual(hamming.distance("GATACA", "GCATAA"), 4)

    def test_large_distance_in_off_by_one_strand(self):
        self.assertEqual(hamming.distance("GGACGGATTCTG", "AGGACGGATTCT"), 9)

<<<<<<< HEAD
=======
    def test_empty_strands(self):
        self.assertEqual(hamming.distance("", ""), 0)

>>>>>>> 371894dab186cec701ce325dcc4d002c02d93cbd
    def test_disallow_first_strand_longer(self):
        with self.assertRaises(ValueError):
            hamming.distance("AATG", "AAA")

    def test_disallow_second_strand_longer(self):
        with self.assertRaises(ValueError):
            hamming.distance("ATA", "AGTG")


if __name__ == '__main__':
    unittest.main()
