import os
import openai
from dotenv import load_dotenv
from langchain.chat_models import ChatOpenAI
from llama_index import GPTVectorStoreIndex, LLMPredictor, PromptHelper, SimpleDirectoryReader, StorageContext, \
    load_index_from_storage
import gradio

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")


def index_documents(folder):
    max_input_size = 4096
    num_outputs = 512
    max_chunk_overlap = 20
    chunk_size_limit = 600

    prompt_helper = PromptHelper(max_input_size,
                                 num_outputs,
                                 max_chunk_overlap=max_chunk_overlap,
                                 chunk_size_limit=chunk_size_limit)

    llm_predictor = LLMPredictor(
        llm=ChatOpenAI(temperature=0.7,
                       model_name="gpt-3.5-turbo",
                       max_tokens=num_outputs)
    )

    documents = SimpleDirectoryReader(folder).load_data()

    index = GPTVectorStoreIndex.from_documents(
        documents,
        llm_predictor=llm_predictor,
        prompt_helper=prompt_helper)

    index.storage_context.persist(persist_dir="data")


def chatbot(input_text):
    storage_context = StorageContext.from_defaults(persist_dir="data")
    index = load_index_from_storage(storage_context)

    query_engine = index.as_query_engine()
    response = query_engine.query(input_text)
    return response.response


index_documents("docs")

interface = gradio.Interface(fn=chatbot,
                             inputs=gradio.components.Textbox(lines=7, label="Nhập câu hỏi của bạn vào đây"),
                             outputs="text",
                             title="Anh trai nhân vật chính AI chatbot")
interface.launch(share=True)
