# Hip — Educador Financeiro

Chatbot educacional sobre finanças pessoais e investimentos, rodando localmente via Ollama + Streamlit. O Hip explica conceitos financeiros usando os dados do cliente como exemplo — nunca recomenda produtos ou investimentos específicos.

## Requisitos

- Python 3.9+
- [Ollama](https://ollama.com) instalado e rodando localmente
- Modelo `mistral` baixado no Ollama:
  ```bash
  ollama pull mistral
  ```
- Dependências Python:
  ```bash
  pip install streamlit pandas requests
  ```

## Estrutura de dados

O app espera os seguintes arquivos em `./data/`:

| Arquivo | Formato | Conteúdo |
|---|---|---|
| `transacoes.csv` | CSV | Transações recentes do cliente |
| `historico_atendimento.csv` | CSV | Histórico de atendimentos anteriores |
| `perfil_investidor.json` | JSON | Dados do cliente (nome, idade, perfil, objetivo, patrimônio, reserva) |
| `produtos_financeiros.json` | JSON | Lista de produtos financeiros disponíveis para consulta educacional |

## Como rodar

1. Garanta que o Ollama está rodando (`ollama serve`, se não estiver como serviço) e que o modelo `mistral` já foi baixado.
2. A partir da pasta do projeto, suba o app:
   ```bash
   streamlit run app.py
   ```
3. Acesse o endereço local que o Streamlit abrir no navegador (geralmente `http://localhost:8501`).

## Como funciona

- Os dados de `./data/` são carregados uma vez, no início da execução, e montados em um bloco de **contexto** (cliente, transações, atendimentos, produtos).
- Esse contexto é injetado, junto com o **system prompt**, em todo prompt enviado ao modelo.
- Cada pergunta do usuário é enviada para o Ollama local (`/api/generate`, modelo `mistral`), e a resposta é exibida na interface de chat do Streamlit.
- O system prompt define as regras de comportamento do Hip — em especial, a proibição de recomendar investimentos ou produtos específicos, mesmo sob insistência ou cenários hipotéticos.

## Configuração

- **Modelo**: trocável via a constante `MODELO` no topo do script (atualmente `mistral`).
- **URL do Ollama**: constante `OLLAMA_URL`, aponta para `http://127.0.0.1:11434/api/generate` por padrão (Ollama local).

## Limitações conhecidas

- Todo o conteúdo de `./data/` é recarregado para memória a cada execução do script — sem cache entre sessões.
- Sem tratamento de erro caso o Ollama não esteja rodando ou o modelo não esteja baixado — a chamada em `perguntar()` falhará nesse caso.
- Dados de exemplo (mock); uso com dados reais de clientes requer revisão de segurança e privacidade antes de produção.
