from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv

load_dotenv()

# Crear chain simple
llm = ChatOpenAI(model="gpt-3.5-turbo")
prompt = ChatPromptTemplate.from_template("Cuéntame un chiste sobre {tema}")
chain = prompt | llm | StrOutputParser()

# Ejecutar
resultado = chain.invoke({"tema": "programación"})
print(resultado)
