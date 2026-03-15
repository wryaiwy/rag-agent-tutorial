from langchain_chroma import Chroma
import config_data as config

# 向量存储服务


class VectorStoreService(object):
    def __init__(self, embedding):
        """
        :param embedding: 嵌入模型的传入
        """
        self.embedding = embedding

        self.vector_store = Chroma(
            collection_name=config.collection_name, # 集合名称
            embedding_function=self.embedding, # 嵌入模型
            persist_directory=config.persist_directory, # 持久化存储的文件夹,这里是去找
        )

    def get_retriever(self):
        """返回向量检索器，方便加入chain"""
        return self.vector_store.as_retriever(search_kwargs={"k": config.similarity_threshold})


if __name__ == '__main__':
    from langchain_community.embeddings import DashScopeEmbeddings
    retriever = VectorStoreService(DashScopeEmbeddings(model=config.embedding_model_name)).get_retriever()

    res = retriever.invoke("我的体重180斤，尺码推荐")
    print(res)

