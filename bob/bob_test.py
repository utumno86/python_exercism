<<<<<<< HEAD
=======
# -*- coding: utf-8 -*-

from __future__ import unicode_literals
>>>>>>> 371894dab186cec701ce325dcc4d002c02d93cbd
import unittest

import bob


<<<<<<< HEAD
# Tests adapted from `problem-specifications//canonical-data.json` @ v1.0.0

class BobTests(unittest.TestCase):
    def test_stating_something(self):
        self.assertEqual(bob.hey("Tom-ay-to, tom-aaaah-to."), "Whatever.")

    def test_shouting(self):
        self.assertEqual(bob.hey("WATCH OUT!"), "Whoa, chill out!")

    def test_shouting_gibberish(self):
        self.assertEqual(bob.hey("FCECDFCAAB"), "Whoa, chill out!")

    def test_asking_a_question(self):
        self.assertEqual(
            bob.hey("Does this cryogenic chamber make me look fat?"), "Sure.")

    def test_asking_a_numeric_question(self):
        self.assertEqual(bob.hey("You are, what, like 15?"), "Sure.")

    def test_asking_gibberish(self):
        self.assertEqual(bob.hey("fffbbcbeab?"), "Sure.")

    def test_talking_forcefully(self):
        self.assertEqual(
            bob.hey("Let's go make out behind the gym!"), "Whatever.")

    def test_using_acronyms_in_regular_speech(self):
        self.assertEqual(
            bob.hey("It's OK if you don't want to go to the DMV."),
            "Whatever.")

    def test_forceful_question(self):
        self.assertEqual(
            bob.hey("WHAT THE HELL WERE YOU THINKING?"), "Whoa, chill out!")

    def test_shouting_numbers(self):
        self.assertEqual(bob.hey("1, 2, 3 GO!"), "Whoa, chill out!")

    def test_only_numbers(self):
        self.assertEqual(bob.hey("1, 2, 3"), "Whatever.")

    def test_question_with_only_numbers(self):
        self.assertEqual(bob.hey("4?"), "Sure.")

    def test_shouting_with_special_characters(self):
        self.assertEqual(
            bob.hey("ZOMG THE %^*@#$(*^ ZOMBIES ARE COMING!!11!!1!"),
            "Whoa, chill out!")

    def test_shouting_with_no_exclamation_mark(self):
        self.assertEqual(bob.hey("I HATE YOU"), "Whoa, chill out!")

    def test_statement_containing_question_mark(self):
        self.assertEqual(
            bob.hey("Ending with ? means a question."), "Whatever.")

    def test_non_letters_with_question(self):
        self.assertEqual(bob.hey(":) ?"), "Sure.")

    def test_prattling_on(self):
        self.assertEqual(
            bob.hey("Wait! Hang on. Are you going to be OK?"), "Sure.")

    def test_silence(self):
        self.assertEqual(bob.hey(""), "Fine. Be that way!")

    def test_prolonged_silence(self):
        self.assertEqual(bob.hey("          "), "Fine. Be that way!")

    def test_alternate_silence(self):
        self.assertEqual(bob.hey("\t\t\t\t\t\t\t\t\t\t"), "Fine. Be that way!")

    def test_multiple_line_question(self):
        self.assertEqual(
            bob.hey("\nDoes this cryogenic chamber make me look fat?\nno"),
            "Whatever.")

    def test_starting_with_whitespace(self):
        self.assertEqual(bob.hey("         hmmmmmmm..."), "Whatever.")

    def test_ending_with_whitespace(self):
        self.assertEqual(
            bob.hey("Okay if like my  spacebar  quite a bit?   "), "Sure.")

    def test_other_whitespace(self):
        self.assertEqual(bob.hey("\n\r \t"), "Fine. Be that way!")

    def test_non_question_ending_with_whitespace(self):
        self.assertEqual(
            bob.hey("This is a statement ending with whitespace      "),
            "Whatever.")

=======
class BobTests(unittest.TestCase):

    def test_stating_something(self):
        self.assertEqual(
            'Whatever.',
            bob.hey('Tom-ay-to, tom-aaaah-to.')
        )

    def test_shouting(self):
        self.assertEqual(
            'Whoa, chill out!',
            bob.hey('WATCH OUT!')
        )

    def test_asking_a_question(self):
        self.assertEqual(
            'Sure.',
            bob.hey('Does this cryogenic chamber make me look fat?')
        )

    def test_asking_a_numeric_question(self):
        self.assertEqual(
            'Sure.',
            bob.hey('You are, what, like 15?')
        )

    def test_talking_forcefully(self):
        self.assertEqual(
            'Whatever.',
            bob.hey("Let's go make out behind the gym!")
        )

    def test_using_acronyms_in_regular_speech(self):
        self.assertEqual(
            'Whatever.', bob.hey("It's OK if you don't want to go to the DMV.")
        )

    def test_forceful_questions(self):
        self.assertEqual(
            'Whoa, chill out!', bob.hey('WHAT THE HELL WERE YOU THINKING?')
        )

    def test_shouting_numbers(self):
        self.assertEqual(
            'Whoa, chill out!', bob.hey('1, 2, 3 GO!')
        )

    def test_only_numbers(self):
        self.assertEqual(
            'Whatever.', bob.hey('1, 2, 3')
        )

    def test_question_with_only_numbers(self):
        self.assertEqual(
            'Sure.', bob.hey('4?')
        )

    def test_shouting_with_special_characters(self):
        self.assertEqual(
            'Whoa, chill out!',
            bob.hey('ZOMG THE %^*@#$(*^ ZOMBIES ARE COMING!!11!!1!')
        )

    def test_shouting_with_umlauts(self):
        self.assertEqual(
            'Whoa, chill out!', bob.hey('ÜMLÄÜTS!')
        )

    def test_calmly_speaking_with_umlauts(self):
        self.assertEqual(
            'Whatever.', bob.hey('ÜMLäÜTS!')
        )

    def test_shouting_with_no_exclamation_mark(self):
        self.assertEqual(
            'Whoa, chill out!', bob.hey('I HATE YOU')
        )

    def test_statement_containing_question_mark(self):
        self.assertEqual(
            'Whatever.', bob.hey('Ending with ? means a question.')
        )

    def test_prattling_on(self):
        self.assertEqual(
            'Sure.', bob.hey("Wait! Hang on. Are you going to be OK?")
        )

    def test_silence(self):
        self.assertEqual(
            'Fine. Be that way!', bob.hey('')
        )

    def test_prolonged_silence(self):
        self.assertEqual(
            'Fine. Be that way!', bob.hey('    \t')
        )

    def test_starts_with_whitespace(self):
        self.assertEqual(
            'Whatever.', bob.hey('         hmmmmmmm...')
        )

    def test_ends_with_whitespace(self):
        self.assertEqual(
            'Sure.', bob.hey('What if we end with whitespace?   ')
        )
>>>>>>> 371894dab186cec701ce325dcc4d002c02d93cbd

if __name__ == '__main__':
    unittest.main()
