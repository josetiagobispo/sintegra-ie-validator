from .base import InscricaoEstadual
class InscricaoEstadualGO(InscricaoEstadual):
    '''
    Classe para verificação da inscrição estadual de Goiás.
    '''
    def is_valid(self):
        if len(self.inscricao) != 9 or not self.inscricao.isdigit():
            return False

        base_inscricao = self.inscricao[:-1]  # Exclui o dígito verificador
        digito_verificador = int(self.inscricao[-1])
        pesos = [9, 8, 7, 6, 5, 4, 3, 2]
        soma = sum(int(digito) * peso for digito, peso in zip(base_inscricao, pesos))
        resto = soma % 11
        if resto == 0 or resto == 1:
            digito_calculado = 0
        else:
            digito_calculado = 11 - resto

        return digito_calculado == digito_verificador
