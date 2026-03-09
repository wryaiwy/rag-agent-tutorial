from openai import OpenAI

# 1. 获取client对象，OpenAI类对象
client = OpenAI(
    # APIkey已经封装到环境变量中了
    base_url="https://dashscope.aliyuncs.com/compatible-mode/v1"
)

# 2. 调用模型
response = client.chat.completions.create(
    model="qwen3.5-flash",
    messages=[
        {"role": "system", "content": "你是一个音乐专家，并且不说废话简单回答"},
        {"role": "assistant", "content": "好的，我是音乐专家，并且话不多，你要问什么？"},
        {"role": "user", "content": "分析陈奕迅的《人来人往》"}
    ]
)

# 3. 处理结果
print(response.choices[0].message.content)
