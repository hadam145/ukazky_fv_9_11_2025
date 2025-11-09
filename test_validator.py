from unittest import TestCase
from validator import ValidatorHesla

class TestValidatorHesla(TestCase):
    def test_validni_heslo(self):
        validator = ValidatorHesla()
        self.assertTrue(validator.validuj("abc123"))

    def test_kratke_heslo(self):
        validator = ValidatorHesla()
        self.assertFalse(validator.validuj("ab2"))

    def test_heslo_bez_cislice(self):
        validator = ValidatorHesla()
        self.assertFalse(validator.validuj("abcdef"))

    def test_prazdne_heslo(self):
        validator = ValidatorHesla()
        self.assertFalse(validator.validuj(""))
