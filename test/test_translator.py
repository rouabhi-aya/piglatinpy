from unittest import TestCase

from translator import PigLatinTranslator


class TestPigLatinTranslator(TestCase):

    def test_get_phrase(self):
        translator = PigLatinTranslator("hello world")
        phrase= translator.get_phrase()
        self.assertEqual("hello world",phrase)

    def test_empty_string(self):
        translator = PigLatinTranslator("")
        translation= translator.translate()
        self.assertEqual("nil",translation)

    def test_translate_word_starting_vowel_ending_Y(self):
        translator = PigLatinTranslator("any")
        translation= translator.translate()
        self.assertEqual("anynay",translation)

    def test_translate_word_starting_vowel_e_ending_Y(self):
        translator = PigLatinTranslator("enemy")
        translation= translator.translate()
        self.assertEqual("enemynay",translation)

    def test_translate_word_starting_vowel_ending_vowel(self):
        translator = PigLatinTranslator("apple")
        translation= translator.translate()
        self.assertEqual("appleyay",translation)