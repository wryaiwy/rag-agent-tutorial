from langchain_community.document_loaders import PyPDFLoader

# TODO 可快速加载PDF中的文字内容

loader = PyPDFLoader(
    file_path="./data/pdf2.pdf",
    mode="single",        # 默认是page模式，每个页面形成一个Document文档对象，
                        # single模式，不管有多少页，只返回1个Document对象
    password="itheima"
)

i = 0
for doc in loader.lazy_load():
    i += 1
    print(doc)
    print("="*20, i)
