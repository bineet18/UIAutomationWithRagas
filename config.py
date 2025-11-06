import os
from langchain_openai import ChatOpenAI, OpenAIEmbeddings
from ragas.llms import LangchainLLMWrapper
from ragas.embeddings import LangchainEmbeddingsWrapper

# Configuration
model_name = os.getenv("OPENAI_MODEL", "gpt-4")
embedding_model_name = os.getenv("EMBEDDING_MODEL", "text-embedding-ada-002")
api_key = os.getenv("OPENAI_API_KEY")

# Initialize LLM and embeddings
base_llm = ChatOpenAI(model=model_name, api_key=api_key)
evaluator_llm = LangchainLLMWrapper(base_llm)
embeddings = LangchainEmbeddingsWrapper(OpenAIEmbeddings(model=embedding_model_name, api_key=api_key))
