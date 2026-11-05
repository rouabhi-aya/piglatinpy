from unittest import TestCase

from translator import PigLatinTranslator


class TestPigLatinTranslator(TestCase):

    def test_get_phrase(self):
        translator = PigLatinTranslator("hello world")
        phrase= translator.get_phrase()
        self.assertEqual(phrase, "hello world")
        pass
