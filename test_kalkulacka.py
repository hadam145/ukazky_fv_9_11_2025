from unittest import TestCase
from kalkulacka import Kalkulacka

class TestKalkulacka(TestCase):

    kalkulacka = Kalkulacka()

    def test_secti(self):
        self.assertEqual(30, self.kalkulacka.secti(10,20))
        self.assertEqual(99, self.kalkulacka.secti(10, 90))
        self.assertEqual(-5, self.kalkulacka.secti(-2, -3))
        self.assertEqual(1, self.kalkulacka.secti(0, 1))

    def test_odecti(self):
        self.assertEqual(-10, self.kalkulacka.odecti(10, 20))

    def test_odmocni(self):
        self.assertEqual(2, self.kalkulacka.odmocni(4))

    def test_vydel(self):
        # self.assertRaises(ZeroDivisionError,self.kalkulacka.vydel(5,0))
        self.assertEqual(1 ,self.kalkulacka.vydel(5, 5))
