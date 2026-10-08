# 🤖 Hip — Educador Financeiro com IA Generativa

Projeto do desafio **Agente Financeiro Inteligente** (DIO): um agente conversacional que ensina conceitos de finanças pessoais e investimentos, usando os dados do próprio cliente como exemplo — e que, por decisão de design, **nunca recomenda onde investir**.

## O Agente

**Hip** é um tutor financeiro, não um consultor. Ele explica como funcionam renda fixa, risco, liquidez e diversificação a partir da situação real do cliente (gastos, reserva de emergência, metas), mas se recusa a indicar produtos ou investimentos específicos — inclusive sob insistência ou em cenários hipotéticos. Essa é a regra central do projeto, não um detalhe de implementação.

📄 Documentação completa: [`docs/documentacao-agente.md`](./docs/documentacao-agente.md)

## Estrutura do Repositório

```
├── README.md
├── requirements.txt
│
├── data/                          # Dados mockados do cliente
│   ├── transacoes.csv             # Transações recentes
│   ├── historico_atendimento.csv  # Atendimentos anteriores
│   ├── perfil_investidor.json     # Perfil, objetivos e metas do cliente
│   └── produtos_financeiros.json  # Produtos disponíveis para consulta educacional
│
├── 📁 docs/                          # Documentação do projeto
│   ├── 01-documentacao-agente.md     # Caso de uso e arquitetura
│   ├── 02-base-conhecimento.md       # Estratégia de dados
│   ├── 03-prompts.md                 # Engenharia de prompts
│   ├── 04-metricas.md                # Avaliação e métricas
│   └── 05-pitch.md                   # Roteiro do pitch
│
├── 📁 src/                           # Código da aplicação
│   └── app.py                        # (exemplo de estrutura)
│
├── 📁 assets/                        # Imagens e diagramas
│   └── ...
│
└── 📁 examples/                      # Referências e exemplos
    └── README.md
```

---

## Dicas Finais

1. **Comece pelo prompt:** Um bom system prompt é a base de um agente eficaz
2. **Use os dados mockados:** Eles garantem consistência e evitam problemas com dados sensíveis
3. **Foque na segurança:** No setor financeiro, evitar alucinações é crítico
4. **Teste cenários reais:** Simule perguntas que um cliente faria de verdade
5. **Seja direto no pitch:** 3 minutos passam rápido, vá ao ponto
