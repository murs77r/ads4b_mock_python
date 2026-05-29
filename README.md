# ads4b_mock_python

## Módulo de Aprovação de Crédito

O projeto implementa o módulo com injeção de dependência via `ServicoCredito` e decisão em `ProcessadorCredito` pelo método `analisar_proposta(cpf, valor_solicitado)`.

### Regras de negócio

- Score menor que 200: `NEGADO`
- Score entre 200 e 599: `APROVADO` apenas quando `valor_solicitado < 1000`
- Score maior ou igual a 600: `APROVADO`
- Falha no serviço externo: `NEGADO` com registro de erro em log

### Executar testes

```bash
python -m unittest discover -s tests -v
```

### Vantagem de usar Mock no CT05

No cenário de serviço externo offline, o mock permite simular a indisponibilidade de forma determinística e sem custo, validando rapidamente o comportamento de segurança (`NEGADO`) e o tratamento de erro sem depender de API real, rede ou instabilidade de terceiros.
