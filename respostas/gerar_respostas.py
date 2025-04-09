from funcoes import consultar_banco, consultar_dados

import openai

def gerar_resposta(mensagem):
    if consultar_banco(mensagem):
        dado = consultar_dados(mensagem)
        prompt = f"Usuário perguntou: '{mensagem}'. Aqui está o dado do banco: {dado}. Gere uma resposta humanizada com base nisso"
    else:
        prompt = f"Responda a esta pergunta: {mensagem}"


    resposta = openai.ChatCompletion.create(model="gpt-4", messages=[{"role": "user",
                                                                       "content": prompt}])
    
    return resposta['choises'][0]['message']['content']