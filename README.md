# ads4b_mock_python

## Módulo de Aprovação de Crédito

O projeto implementa o módulo com injeção de dependência via `ServicoCredito` e decisão em `ProcessadorCredito` pelo método `analisar_proposta(cpf, valor_solicitado)`.

## Contexto acadêmico

- Matéria: ADS-MAT4B - 01/2026 - Testes Métricas e qualidade de software
- Professor: Marcelo Carboni
- Grupo:
  - Murilo Souza
  - João Paulo Nunes
  - Victor de Castro

### Regras de negócio

- Score menor que 200: `NEGADO`
- Score entre 200 e 599: `APROVADO` apenas quando `valor_solicitado < 1000`
- Score maior ou igual a 600: `APROVADO`
- Falha no serviço externo: `NEGADO` com registro de erro em log

### Casos de teste e resultados esperados

- CT01 — Score muito baixo: resultado esperado `NEGADO`
- CT02 — Score médio com valor alto: resultado esperado `NEGADO`
- CT03 — Score médio com valor baixo: resultado esperado `APROVADO`
- CT04 — Score alto: resultado esperado `APROVADO`
- CT05 — Serviço externo offline: resultado esperado `NEGADO`

### Executar testes

```bash
python -m unittest discover -s tests -v
```
