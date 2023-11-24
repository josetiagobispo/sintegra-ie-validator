class InscricaoEstadualMT(InscricaoEstadual):
    '''
    Classe para verificação da inscrição estadual do Mato Grosso.
    '''
    def is_valid(self):
        if len(self.inscricao) != 11 or not self.inscricao.isdigit():
            return False

        base_inscricao = self.inscricao[:-1]  # Exclui o dígito verificador
        digito_verificador = int(self.inscricao[-1])
        pesos = [3, 2, 9, 8, 7, 6, 5, 4, 3, 2]

        soma = sum(int(base_inscricao[i]) * pesos[i] for i in range(10))
        resto = soma % 11
        if resto == 0 or resto == 1:
            digito_calculado = 0
        else:
            digito_calculado = 11 - resto

        return digito_calculado == digito_verificador
