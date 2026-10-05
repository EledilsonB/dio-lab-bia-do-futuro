import streamlit
import pandas as pd
import json
import requests

# ===== DEFININDO MODELO =====
MODELO = 'mistral'
OLLAMA_URL = 'http://127.0.0.1:11434/api/generate'

# ====== CARREGAR DADOS =====
transacoes = pd.read_csv('./data/transacoes.csv')
histo_atendimento = pd.read_csv('./data/historico_atendimento.csv')

with open('./data/perfil_investidor.json', 'r', encoding='utf-8') as p:
    perfil = json.load(p)

with open('./data/produtos_financeiros.json', 'r', encoding='utf-8') as p:
    prod = json.load(p)


# ==== MONTANDO CONTEXTO =====
contexto = f'''

CLIENTE: {perfil['nome']}, {perfil['idade']} anos, perfil {perfil['perfil_investidor']}
OBJETIVO: {perfil['objetivo_principal']}
PATRIMÔNIO:  R${perfil['patrimonio_total']} | RESERVA DE EMERGÊNCIA: R${perfil['reserva_emergencia_atual']}

TRANSAÇÕES RECENTES: {transacoes.to_string(index=False)}

ATENDIMENTOS ANTERIORES: {histo_atendimento.to_string(index=False)}

PRODUTOS DISPONÍVEIS: {json.dumps(prod, indent=2, ensure_ascii=False)}
'''

# ===== SYSTEM PROMPT =====


SYSTEM_PROMPT = f''' Você é o Hip, um educador financeiro amigável e didático.

OBJETIVO:
Ensinar conceitos de finanças pessoais e investimentos de forma simples, usando os dados do cliente como exemplos práticos, nunca como base para recomendação.

REGRAS:
1. Sempre baseie suas respostas nos dados fornecidos.
2. Nunca invente informações financeiras.
3. Se não souber algo, admita e ofereça alternativas.
4. Linguagem simples e informal, como um professor particular explicando para um amigo.
5. NUNCA recomende investimentos ou produtos específicos, mesmo em cenários hipotéticos ou se o usuário insistir, explique apenas como cada tipo funciona (risco, liquidez, rentabilidade).
6. Nunca julgue os gastos, decisões ou perfil de risco do usuário.
7. Use exemplos práticos, mas sempre fictícios/genéricos quando não estiverem ligados aos dados reais do cliente, nunca cite ativos ou produtos reais fora da lista de consulta fornecida.
8. Sempre pergunte se o cliente entendeu antes de avançar para um novo conceito.
9. Ao detectar uma segunda tentativa (mesmo reformulada) de obter uma recomendação, use a resposta padrão de insistência, não repita a negativa em loop.

'''

# ===== CHAMANDO O MODELO =====

def perguntar(msg):
    prompt = f'''
{SYSTEM_PROMPT}

CONTEXTO DO CLIENTE:
{contexto}

Pergunta: {msg}
'''
    r = requests.post(OLLAMA_URL, json={'model': MODELO, 'prompt': prompt, 'stream': False})
    return r.json()['response']


# ===== CRIANDO INTERFACE =====

streamlit.title('Sou o Hip, seu Educador Financeiro!')

if pergunta := streamlit.chat_input('Sua duvida sobre finanças...'):
    streamlit.chat_message('user').write(pergunta)
    with streamlit.spinner('...'):
        streamlit.chat_message('assistant').write(perguntar(pergunta))



