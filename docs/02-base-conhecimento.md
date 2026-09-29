# Base de Conhecimento

## Dados Utilizados

Descreva se usou os arquivos da pasta `data`, por exemplo:

| Arquivo | Formato | Utilização no Hip |
|---------|---------|---------------------|
| `historico_atendimento.csv` | CSV | Contextualizar interações anteriores, evitando repetir explicações já dadas ao usuário |
| `transacoes.csv` | CSV | Identificar padrões de gastos para gerar exemplos didáticos personalizados (ex: explicar reserva de emergência usando os próprios números do usuário) |
| `perfil_investidor.json` | JSON | Adaptar o nível e o foco das explicações ao perfil e aos objetivos declarados do usuário (ex: priorizar conceitos de renda fixa e reserva de emergência para quem tem perfil conservador e essa meta) |
| `produtos_financeiros.json` | JSON | Explicar como cada categoria de produto funciona (risco, rentabilidade, liquidez) quando o usuário perguntar sobre ela — nunca para sugerir qual produto ele deveria escolher |

---

## Adaptações nos Dados

> Você modificou ou expandiu os dados mockados? Descreva aqui.

O perfil_investidor.json foi usado como veio, mas o transacoes.csv foi agregado por categoria de gasto (não usado transação a transação) para gerar exemplos e identificar padrões, sem expor o histórico bruto no prompt. O produtos_financeiros.json teve o campo indicado_para mantido apenas como contexto explicativo do produto — não como critério de match com o perfil do usuário.

---

## Estratégia de Integração

### Como os dados são carregados?
> Descreva como seu agente acessa a base de conhecimento.

perfil_investidor.json e o resumo agregado de transacoes.csv são carregados no início da sessão e incluídos no contexto (dados relativamente estáveis por sessão). produtos_financeiros.json e historico_atendimento.csv são consultados dinamicamente, sob demanda, apenas quando o tema da conversa exige (ex: usuário pergunta sobre um tipo de produto específico).

```python
import pandas as pd
import json

historico = pd.read_csv('../data/historico_atendimento.csv')
transacoes = pd.read_csv('../data/transacoes.csv')

with open('../data/perfil_investidor.json', 'r', encoding='utf-8') as arq:
    perfil = json.load(arq)

with open('../data/produtos_financeiros.json', 'r', encoding='utf-8') as arq:
    prod = json.load(arq)
```

### Como os dados são usados no prompt?
> Os dados vão no system prompt? São consultados dinamicamente?

O perfil do usuário vai fixo no system prompt, para calibrar tom e prioridade de explicações durante toda a sessão. Os produtos financeiros NÃO vão no system prompt como lista completa — são inseridos no contexto apenas quando o usuário pergunta sobre um produto específico, e sempre acompanhados da instrução de uso educacional (explicar, não recomendar).

---

## Exemplo de Contexto Montado

> Mostre um exemplo de como os dados são formatados para o agente.


## Exemplo de Contexto Montado

> Exemplo de como os dados são formatados e injetados no contexto do Hip para uma sessão de atendimento.

```
DADOS DO CLIENTE:
- Nome: João Silva
- Perfil: Moderado
- Objetivo principal: Construir reserva de emergência
- Reserva atual: R$ 10.000 (meta: R$ 15.000, prazo: 06/2026)
- Meta adicional: Entrada do apartamento — R$ 50.000 (prazo: 12/2027)

RESUMO DE GASTOS:
- Moradia: R$ 1.380
- Alimentação: R$ 570
- Transporte: R$ 295
- Saúde: R$ 188
- Lazer: R$ 55,90
- Total de saídas: R$ 2.488,90

PRODUTOS DISPONÍVEIS PARA CONSULTA (uso educacional apenas, não recomendar):
- Tesouro Selic (risco baixo)
- CDB Liquidez Diária (risco baixo)
- LCI/LCA (risco baixo)
- Fundo Multimercado (risco médio)
- Fundo de Ações (risco alto)
```

### Observações

- O bloco de produtos foi rotulado explicitamente como **"uso educacional apenas, não recomendar"** diretamente no dado injetado no contexto, não só nas instruções do system prompt. Essa camada extra reduz o risco do modelo "perder" a restrição em respostas mais longas.
- As duas metas do cliente (reserva de emergência e entrada do apartamento) foram incluídas, já que o contexto é montado por sessão inteira, o Hip precisa conseguir responder bem independentemente de qual meta o usuário perguntar.
- O resumo de gastos é agregado por categoria (não transação a transação), conforme decidido na seção de Adaptações nos Dados.
