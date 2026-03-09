# langchain_community
from langchain_community.llms.tongyi import Tongyi

# 不用qwen3.5-flash，因为qwen3.5-flash是聊天模型，qwen-flash是大语言模型
model = Tongyi(model="qwen-flash")

# 调用invoke向模型提问
res = model.invoke(input="你是谁呀能做什么？")

print(res)