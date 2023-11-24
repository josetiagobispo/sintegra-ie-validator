class InscricaoEstadualPE(InscricaoEstadual):
    '''
    Classe para verificação da inscrição estadual de Pernambuco.
    '''
    def is_valid(self):
        if len(self.inscricao) != 14 or not self.inscricao.isdigit():
            return False

        # Primeiro dígito verificador
        pesos = [8, 7, 6, 5, 4, 3, 2]
        soma = sum(int(self.inscricao[i]) * pesos[i] for i in range(7))
        resto = soma % 11
        d1 = 0 if resto <= 1 else 11 - resto

        # Segundo dígito verificador
        pesos = [9, 8, 7, 6, 5, 4, 3, 2]
        soma = sum(int(self.inscricao[i]) * pesos[i] for i in range(8)) + d1 * 2
        resto = soma % 11
        d2 = 0 if resto <= 1 else 11 - resto

        return d1 == int(self.inscricao[13]) and d2 == int(self.inscricao[14])

