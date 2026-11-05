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
        pass
