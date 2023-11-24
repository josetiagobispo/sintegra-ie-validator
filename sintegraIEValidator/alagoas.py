from .base import InscricaoEstadual
class InscricaoEstadualAL(InscricaoEstadual):
    '''
    Classe para verificação da inscrição estadual de Alagoas.
    '''
    def is_valid(self):
        if len(self.inscricao) != 9 or not self.inscricao.isdigit() or not self.inscricao.startswith('24'):
            return False
        pesos = [9, 8, 7, 6, 5, 4, 3, 2]
        soma = sum(int(digito) * peso for digito, peso in zip(self.inscricao[2:-1], pesos))
        produto = soma * 10
        resto = produto - (produto // 11 * 11)
        digito_verificador = 0 if resto == 10 else resto
        return digito_verificador == int(self.inscricao[-1])
