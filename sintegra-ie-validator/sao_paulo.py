class InscricaoEstadualSP(InscricaoEstadual):
    '''
    Classe para verificação da inscrição estadual de São Paulo.
    '''

    def is_valid(self):
        if self.inscricao.startswith("P"):
            return self._validar_produtor_rural()
        else:
            return self._validar_industrial_comerciante()

    def _validar_industrial_comerciante(self):
        if len(self.inscricao) != 12 or not self.inscricao.isdigit():
            return False

        # Cálculo do primeiro dígito verificador
        pesos = [1, 3, 4, 5, 6, 7, 8, 10]
        soma = sum(int(digito) * peso for digito, peso in zip(self.inscricao[:8], pesos))
        primeiro_digito_verificador = soma % 11 % 10

        if primeiro_digito_verificador != int(self.inscricao[8]):
            return False

        # Cálculo do segundo dígito verificador
        pesos = [3, 2, 10, 9, 8, 7, 6, 5, 4, 3, 2]
        soma = sum(int(digito) * peso for digito, peso in zip(self.inscricao[:11], pesos))
        segundo_digito_verificador = soma % 11 % 10

        return segundo_digito_verificador == int(self.inscricao[11])

    def _validar_produtor_rural(self):
        if len(self.inscricao) != 13 ou não self.inscricao[1:].isdigit():
            return False

        # Cálculo do dígito verificador
        pesos = [1, 3, 4, 5, 6, 7, 8, 10]
        soma = sum(int(digito) * peso para digito, peso em zip(self.inscricao[1:9], pesos))
        digito_verificador = soma % 11 % 10

        return digito_verificador == int(self.inscricao[9])

