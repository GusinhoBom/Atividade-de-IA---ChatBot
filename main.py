import google.generativeai as genai
import os 
from dotenv import load_dotenv, dotenv_values

load_dotenv()

genai.configure(api_key=os.getenv ("API_KEY"))

QUANTIDADE_PERGUNTAS = 3

def obter_resposta(pergunta, contexto):    
    # Obtém um modelo
    model = genai.GenerativeModel("gemini-2.0-flash")
    
    response = model.generate_content(f"Você é um especialista em {contexto}. Responda a pergunta: {pergunta}")
    
    return response.text if response else "Não foi possível gerar uma resposta."

def main():
    print("Bem-vindo ao ChatBot! Vamos começar?")
    contexto = input("Qual assunto você quer conversar? ")
    print(f"Legal, podemos falar sobre {contexto}. Você pode me fazer {QUANTIDADE_PERGUNTAS} perguntas.")

    perguntas = []
    respostas = []

    for i in range(QUANTIDADE_PERGUNTAS):
        pergunta = input(f"Qual é a sua pergunta {i + 1}? ")
        perguntas.append(pergunta)
        resposta = obter_resposta(pergunta, contexto)       
        respostas.append(resposta)
        print(f"Resposta: {resposta}\n")

    # Gera um resumo das perguntas e respostas
    model = genai.GenerativeModel("gemini-2.0-flash")
    resumo_prompt = "Resuma as seguintes perguntas e respostas:\n" + "\n".join(
        [f"Pergunta: {p}\nResposta: {r}" for p, r in zip(perguntas, respostas)]
    )

    resumo_response = model.generate_content(resumo_prompt)
    resumo = resumo_response.text if resumo_response else "Não foi possível gerar um resumo."

    print("\nResumo final do ChatBot:")
    print(resumo)

if __name__ == "__main__":
    main()