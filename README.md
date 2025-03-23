# Atividade-de-IA---ChatBot
📜 Descrição

O chatbot permite ao usuário escolher um tema de conversa e fazer até três perguntas sobre esse tema. Ele utiliza o modelo gemini-2.0-flash da API do Google Gemini para gerar respostas e, ao final, cria um resumo das perguntas e respostas.

🚀 Funcionalidades

Configuração da API do Google Gemini usando variáveis de ambiente.

Recebe um contexto de conversa do usuário.

Permite fazer até 3 perguntas sobre o contexto escolhido.

Retorna respostas geradas pelo modelo de IA.

Gera um resumo final das perguntas e respostas.

🛠️ Configuração e Execução

1️⃣ Pré-requisitos

Python instalado (versão 3.7 ou superior).

Biblioteca google-generativeai instalada.

Biblioteca dotenv instalada para gerenciamento de variáveis de ambiente.

2️⃣ Instalação das Dependências

pip install google-generativeai python-dotenv

3️⃣ Configuração da API Key

Criei um arquivo .env no mesmo diretório do main.py e adicione a chave da API do Google Gemini:

API_KEY=your_google_gemini_api_key

4️⃣ Executando o ChatBot

python main.py

📂 Estrutura do Código

obter_resposta(pergunta, contexto): Gera uma resposta com base na pergunta e no contexto.

main(): Controla o fluxo do chatbot, recebendo entradas do usuário e gerando respostas.

📝 Observações

Certifique-se de que sua API Key está correta e ativa.

O modelo utilizado é o gemini-2.0-flash, que pode estar sujeito a alterações pela Google.

O número de perguntas pode ser ajustado modificando a variável QUANTIDADE_PERGUNTAS.

📌 Autor

Desenvolvido por Gustavo Pereira Vieira.

