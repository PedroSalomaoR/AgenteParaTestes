import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain.prompts import ChatPromptTemplate

#carrega variáveis do arquivo .env
load_dotenv()

#chave da Groq
api_key = os.getenv("GROQ_API_KEY")
#inicia o modelo da Groq
chat = ChatGroq(
    api_key=api_key,
    model="llama-3.3-70b-versatile"
)

#prompt para gerar testes unitários
prompt = ChatPromptTemplate.from_messages([
    ("system", """Você é um agente que gera arquivos de teste em Python.
Cada arquivo de teste deve começar com 'import pytest'.
Crie funções test_* para casos de sucesso e falha.
Siga as normas de programação em Python, se for comentar no código use #, e não use ``` e nem comece com python o arquivo."""),
    ("user", "Gere um teste para o seguinte código:\n\n{codigo}")
])

chain = prompt | chat
def gerar_testes(arquivo_codigo: str):
    """Lê o código de um arquivo Python e gera um arquivo de testes pytest"""
    
    #nome para salvar o arquivo de teste
    nome_base = os.path.splitext(os.path.basename(arquivo_codigo))[0]
    nome_teste = f"test_{nome_base}.py"

    #verifica o conteúdo do arquivo Python
    with open(arquivo_codigo, "r", encoding="utf-8") as f:
        codigo = f.read()

    #invoca o modelo
    resposta = chain.invoke({"codigo": codigo})

    #salva o resultado no arquivo de teste
    with open(nome_teste, "w", encoding="utf-8") as f:
        f.write(resposta.content)

    return nome_teste

#exemplo de uso
if __name__ == "__main__":
    #pergunta qual arquivo o usuário quer usar
    arquivo = input("Digite o caminho do arquivo Python para gerar os testes: ").strip()
    
    if not os.path.exists(arquivo):
        print("Arquivo não encontrado!")
    else:
        arquivo_teste = gerar_testes(arquivo)
        print(f"Arquivo de teste gerado: {arquivo_teste}")
        print(f"Agora rode: pytest {arquivo_teste}")
