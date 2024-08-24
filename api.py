# from langchain import OpenAI
# from langchain.chains import QAChain

# model = OpenAI (api_key = " ")

# qa_chain = QAChain(model = model)

# question = "Qual a capital do Brasil?"
# response = qa_chain.run(question)

# print (response)



# from langchain.llms import OpenAI
# from langchain.chains import QAChain

# # Inicializar o modelo de linguagem
# model = OpenAI(api_key=" )

# # Criar uma cadeia de perguntas e respostas
# qa_chain = QAChain(model=model)

# # Fazer uma pergunta ao modelo
# question = "Qual é a capital da França?"
# response = qa_chain.run(question)

# print(response)  # Esperado: "Paris"




# from langchain import OpenAI
# from langchain.chains import RetrievalQA
# from langchain.prompts import PromptTemplate
# from langchain.vectorstores import SimpleVectorStore

# # Inicializar o modelo de linguagem
# model = OpenAI(api_key="")

# # Criar um prompt template (ajuste conforme necessário)
# prompt_template = PromptTemplate(template="Responda à pergunta com base no contexto: {question}")

# # Inicializar o vetor de armazenamento
# vector_store = SimpleVectorStore()

# # Criar uma cadeia de perguntas e respostas usando RetrievalQA
# qa_chain = RetrievalQA(llm=model, prompt_template=prompt_template, vector_store=vector_store)

# # Fazer uma pergunta ao modelo
# question = "Qual é a capital da França?"
# response = qa_chain.run(question)

# print(response)  # Esperado: "Paris"



from langchain import OpenAI
from langchain.chains import RetrievalQA
from langchain.vectorstores import Chroma
from langchain.prompts import PromptTemplate

# Inicializar o modelo de linguagem
model = OpenAI(api_key="###")

# Criar um prompt template (ajuste conforme necessário)
prompt_template = PromptTemplate(template="Responda à pergunta com base no contexto: {question}")

# Inicializar o armazenamento de vetores
vector_store = Chroma()

# Criar uma cadeia de perguntas e respostas usando RetrievalQA
qa_chain = RetrievalQA(llm=model, prompt_template=prompt_template, vector_store=vector_store)

# Fazer uma pergunta ao modelo
question = "Qual é a capital da França?"
response = qa_chain.run(question)

print(response)  # Esperado: "Paris"