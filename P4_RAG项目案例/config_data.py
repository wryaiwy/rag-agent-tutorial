
md5_path = "./md5.text" # md5记录文件


# Chroma
collection_name = "rag" # 数据库的表名
persist_directory = "./chroma_db" # 数据库本地存储文件夹


# spliter
chunk_size = 1000       # 分块大小
chunk_overlap = 100     # 分块重叠
separators = ["\n\n", "\n", ".", "!", "?", "。", "！", "？", " ", ""]  # 文本分割的符号
max_split_char_number = 1000        # 文本分割的阈值

#
similarity_threshold = 1            # 检索返回匹配的文档数量

embedding_model_name = "text-embedding-v4"
chat_model_name = "qwen3.5-flash"

session_config = {
        "configurable": {
            "session_id": "user_001",
        }
    }
