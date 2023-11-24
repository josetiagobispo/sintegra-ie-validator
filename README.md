
# sintegra-ie-validator

sintegraIEValidator é um pacote Python projetado para validar inscrições estaduais de diferentes estados brasileiros. Atualmente, suporta validações para os estados do Acre , Goias, Alagoas, São Paulo, Minas Gerais, Pernanbuco. Em breve mais Estados e Funcionalidades



## Instalação

Instale o pacote via pip:

```bash
pip install sintegraIEValidator
```

## Uso

Para usar o sintegraIEValidator, importe a classe de validação correspondente ao estado desejado. Por exemplo:

### Validando uma Inscrição Estadual de São Paulo

```python
from sintegraIEValidator import InscricaoEstadualSP

validador_ac = InscricaoEstadualSP("652896367166")
print(validador_ac.is_valid())
```


### Validando uma Inscrição Estadual do Acre

```python
from sintegraIEValidator import InscricaoEstadualAC

validador_ac = InscricaoEstadualAC("0154899511703")
print(validador_ac.is_valid())
```

### Validando uma Inscrição Estadual de Alagoas

```python
from sintegraIEValidator import InscricaoEstadualAL

validador_al = InscricaoEstadualAL("248368818")
print(validador_al.is_valid())
```
## Disclaimer
Este pacote é fornecido "como está", sem garantias de qualquer tipo. Os desenvolvedores não são responsáveis por quaisquer bugs ou problemas.

## Contribuições

Contribuições são bem-vindas, especialmente para expandir a validação para outros estados. Sinta-se à vontade para fazer um fork do projeto, adicionar sua contribuição e criar um pull request.

## Licença

Este projeto está sob a licença MIT.

## Ajude o Projeto
Considere enviar um PIX para josetiagobsouza@gmail.com para um café , ficarei muito grato.
