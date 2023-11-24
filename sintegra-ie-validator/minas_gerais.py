class InscricaoEstadualMG(InscricaoEstadual):
    '''
    Classe para verificação da inscrição estadual de Minas Gerais.
    '''
    def is_valid(self):
        if len(self.inscricao) != 13 or not self.inscricao.isdigit():
            return False

        # Primeiro dígito verificador
        numero = self.inscricao[:3] + "0" + self.inscricao[3:11]  # Igualar as casas
        pesos = [1, 2] * 6  # Padrão de pesos alternando entre 1 e 2
        soma = sum(int(numero[i]) * pesos[i] for i in range(12))
        d1 = (10 - (soma % 10)) % 10
        if d1 != int(self.inscricao[11]):
            return False

        # Segundo dígito verificador
        numero = self.inscricao[:12]  # Utiliza o número incluindo o D1
        pesos = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11] * 2  # Padrão de pesos
        soma = sum(int(numero[i]) * pesos[i] for i in range(12))
        resto = soma % 11
        d2 = 0 if resto <= 1 else 11 - resto

        return d2 == int(self.inscricao[12])
