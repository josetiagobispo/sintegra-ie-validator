
class InscricaoEstadualAC(InscricaoEstadual):
    '''
    Classe para verificação da inscrição estadual do Acre.
    '''
    def is_valid(self):
        if len(self.inscricao) != 13 or not self.inscricao.isdigit():
            return False
        if not self.inscricao.startswith('01'):
            return False
        pesos_1 = [4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]
        pesos_2 = [5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]
        soma = sum(int(digito) * peso for digito, peso in zip(self.inscricao[:-2], pesos_1))
        resto = soma % 11
        primeiro_digito_verificador = 11 - resto if resto > 1 else 0
        if primeiro_digito_verificador != int(self.inscricao[-2]):
            return False
        soma = sum(int(digito) * peso for digito, peso in zip(self.inscricao[:-1], pesos_2))
        resto = soma % 11
        segundo_digito_verificador = 11 - resto if resto > 1 else 0
        return segundo_digito_verificador == int(self.inscricao[-1])
