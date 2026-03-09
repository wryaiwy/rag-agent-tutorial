from openai import OpenAI

# 1. 获取client对象，OpenAI类对象
client = OpenAI(
    base_url="https://dashscope.aliyuncs.com/compatible-mode/v1"
)

# 2. 调用模型
response = client.chat.completions.create(
    model="qwen3.5-flash",
    messages=[
        {"role": "system", "content": "你是AI助理，回答很简洁"},
        {"role": "user", "content": "小明有2条宠物狗"},
        {"role": "assistant", "content": "好的"},
        {"role": "user", "content": "小红有3只宠物猫"},
        {"role": "assistant", "content": "好的"},
        {"role": "user", "content": "总共有几个宠物？"}
    ],
    stream=True     # 开启了流式输出的功能
)

# 3. 处理结果
for chunk in response:
    # 获取当前片段的内容
    content = chunk.choices[0].delta.content

    # 只有当内容不为 None 时才打印
    if content is not None:
        print(
            content,
            end="",  # 流式输出通常不需要额外空格，直接拼接即可
            flush=True  # 立刻刷新缓冲区，保证丝滑感
        )