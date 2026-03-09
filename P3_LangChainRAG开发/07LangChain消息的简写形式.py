from langchain_community.chat_models.tongyi import ChatTongyi

# 得到模型对象, qwen3-max就是聊天模型
model = ChatTongyi(model="qwen-flash")

# 准备消息列表
# TODO 动态的，需要在运行时由LangChain内部机制转换为Message类对象
# TODO 好处：在运行时支持内部填充，动态注入
messages = [
    # (角色，内容)  角色：system/human/ai
    ("system", "你是一个边塞诗人。"),
    ("human", "写一首唐诗。"),
    ("ai", "锄禾日当午，汗滴禾下土，谁知盘中餐，粒粒皆辛苦。"),
    ("human", "按照你上一个回复的格式，在写一首唐诗。")
]

# 调用stream流式执行
res = model.stream(input=messages)

# for循环迭代打印输出，通过.content来获取到内容
for chunk in res:
    print(chunk.content, end="", flush=True)
