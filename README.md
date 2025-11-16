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

![](https://github.com/hakki17/AREP-Introduction-to-Creating-RAGs/blob/main/IMG/1.entorno-virtual.png)

3. Instalar dependencias:

```bash
pip install langchain langchain-openai python-dotenv
```

4. Crear archivo `.env`:

![](https://github.com/hakki17/AREP-Introduction-to-Creating-RAGs/blob/main/IMG/2.env.png)

5. Ejecutar:

```bash
python basic_chain.py
```

## Ejemplo de Output

![](https://github.com/hakki17/AREP-Introduction-to-Creating-RAGs/blob/main/IMG/3.pruebas.png)
