
class InscricaoEstadual:
    '''
    Classe base para verificação de inscrição estadual.
    '''
    def __init__(self, inscricao):
        self.inscricao = inscricao

    def is_valid(self):
        '''
        Método para verificar se a inscrição estadual é válida.
        Deve ser sobrescrito pelas subclasses.
        '''
        raise NotImplementedError("Subclasses devem implementar este método.")
