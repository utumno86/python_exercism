import unittest

from rna_transcription import to_rna


<<<<<<< HEAD
# Tests adapted from `problem-specifications//canonical-data.json` @ v1.0.1

class DNATests(unittest.TestCase):
=======
# test cases adapted from `x-common//canonical-data.json` @ version: 1.0.0

class DNATests(unittest.TestCase):
    def test_transcribes_guanine_to_cytosine(self):
        self.assertEqual(to_rna('G'), 'C')
>>>>>>> 371894dab186cec701ce325dcc4d002c02d93cbd

    def test_transcribes_cytosine_to_guanine(self):
        self.assertEqual(to_rna('C'), 'G')

<<<<<<< HEAD
    def test_transcribes_guanine_to_cytosine(self):
        self.assertEqual(to_rna('G'), 'C')

=======
>>>>>>> 371894dab186cec701ce325dcc4d002c02d93cbd
    def test_transcribes_thymine_to_adenine(self):
        self.assertEqual(to_rna('T'), 'A')

    def test_transcribes_adenine_to_uracil(self):
        self.assertEqual(to_rna('A'), 'U')

    def test_transcribes_all_occurences(self):
<<<<<<< HEAD
        self.assertEqual(to_rna('ACGTGGTCTTAA'), 'UGCACCAGAAUU')

    def test_correctly_handles_single_invalid_input(self):
        with self.assertRaises(ValueError):
            to_rna('U')

    def test_correctly_handles_completely_invalid_input(self):
        with self.assertRaises(ValueError):
            to_rna('XXX')

    def test_correctly_handles_partially_invalid_input(self):
        with self.assertRaises(ValueError):
            to_rna('ACGTXXXCTTAA')
=======
        self.assertMultiLineEqual(to_rna('ACGTGGTCTTAA'), 'UGCACCAGAAUU')

    def test_correctly_handles_single_invalid_input(self):
        self.assertEqual(to_rna('U'), '')

    def test_correctly_handles_completely_invalid_input(self):
        self.assertMultiLineEqual(to_rna('XXX'), '')

    def test_correctly_handles_partially_invalid_input(self):
        self.assertMultiLineEqual(to_rna('ACGTXXXCTTAA'), '')
>>>>>>> 371894dab186cec701ce325dcc4d002c02d93cbd


if __name__ == '__main__':
    unittest.main()
