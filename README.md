
# ValidadorIE

sintegra-ie-validator é um pacote Python projetado para validar inscrições estaduais de diferentes estados brasileiros. Atualmente, suporta validações para os estados do Acre e Alagoas.

## Instalação

Instale o pacote via pip:

```bash
pip install ValidadorIE
```

## Uso

Para usar o sintegra-ie-validator, importe a classe de validação correspondente ao estado desejado. Por exemplo:

### Validando uma Inscrição Estadual do Acre

```python
from ValidadorIE.acre import InscricaoEstadualAC

validador_ac = InscricaoEstadualAC("inscricao_estadual_ac")
print(validador_ac.is_valid())
```

### Validando uma Inscrição Estadual de Alagoas

```python
from ValidadorIE.alagoas import InscricaoEstadualAL

validador_al = InscricaoEstadualAL("inscricao_estadual_al")
print(validador_al.is_valid())
```

## Contribuições

Contribuições são bem-vindas, especialmente para expandir a validação para outros estados. Sinta-se à vontade para fazer um fork do projeto, adicionar sua contribuição e criar um pull request.

## Licença

Este projeto está sob a licença MIT.
