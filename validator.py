class ValidatorHesla:
    def validuj(self,heslo):
        if(len(heslo)<=5):
            return False
        for znak in heslo:
            if '0' <=znak <= '9':
                return True
        return False
