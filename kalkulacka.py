import math

class Kalkulacka:

    def secti(self,a,b):
        """
        Metoda secte dve cisla
        :param a: prvni cislo
        :param b: druhe cislo
        :return: vysledek secteni dvou cisel
        """
        return a+b

    def odecti(self,a,b):
        """
        Odecte dve cisla
        :param a: prvni cislo
        :param b: druhe cislo
        :return: vysledek odecteni dvou cisel
        """
        return a -b

    def odmocni(self,a):
        """
        Odmocnina
        :param a:
        :return:
        """
        return math.sqrt(a)

    def vydel(self,a,b):
        """

        :param a:
        :param b:
        :return:
        """
        if b == 0:
            raise ZeroDivisionError
        return a/b

