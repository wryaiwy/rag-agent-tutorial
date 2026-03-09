# langchain_ollama
from langchain_ollama import OllamaLLM

model = OllamaLLM(model="deepseek-r1:1.5b")

res = model.invoke(input="你是谁呀能做什么？")

print(res)
