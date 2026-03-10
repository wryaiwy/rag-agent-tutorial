from langchain_community.document_loaders import CSVLoader

# TODO
# 文档加载器提供了一套标准接口，用于将不同来源（如 CSV、PDF 或 JSON等）的数据读取为 LangChain 的文档格式。
# 这确保了无论数据来源如何，都能对其进行一致性处理。
# 不同的文档加载器可能定义了不同的参数，但是其都实现了统一的接口（方法）。
# load()：一次性加载全部文档
# lazy_load()：延迟流式传输文档，对大型数据集很有用，避免内存溢出。


loader = CSVLoader(
    file_path="./data/stu.csv",
    csv_args={
        "delimiter": ",",       # 指定分隔符
        "quotechar": '"',       # 指定带有分隔符文本的引号包围是单引号还是双引号
        # 如果数据原本有表头，就不要下面的代码，如果没有可以使用
        "fieldnames": ['name', 'age', 'gender', '爱好']
    },
    encoding="utf-8"            # 指定编码为UTF-8
)

# 批量加载 .load()   ->  [Document, Document, ...]
# documents = loader.load()
#
# for document in documents:
#     print(type(document), document)

# 懒加载  .lazy_load()  迭代器[Document]
for document in loader.lazy_load():
    print(document)
