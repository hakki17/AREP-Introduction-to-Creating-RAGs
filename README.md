# AREP-Introduction-to-Creating-RAGs

ESTE ES EL REPO DEL PRIMER TRABAJO LangChain LLM Chain, PARA EL OTRO REPO (RAG Project) ESTE ES EL LINK:
https://github.com/hakki17/AREP-RAGproject

## Descripción

Implementación básica de un chain LLM usando LangChain y OpenAI para generar respuestas dinámicas.

## Arquitectura

- **LLM**: ChatGPT (gpt-3.5-turbo)
- **Prompt Template**: Plantilla parametrizable
- **Output Parser**: Procesador de respuestas en texto

## Instalación

1. Clonar repositorio

2. Crear entorno virtual:

![]()

3. Instalar dependencias:

```bash
pip install langchain langchain-openai python-dotenv
```

4. Crear archivo `.env`:

```
OPENAI_API_KEY=tu-api-key
```

5. Ejecutar:

```bash
python basic_chain.py
```

## Ejemplo de Output

```
¿Por qué los programadores prefieren el café helado?
Porque les ayuda a mantener la calma cuando hay un bug en el código.
```
