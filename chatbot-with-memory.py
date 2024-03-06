import gradio as gr
from langchain.chains.conversation.memory import ConversationBufferWindowMemory
from langchain_groq import ChatGroq

from langchain.chains import ConversationChain

client =  ChatGroq(
            groq_api_key="your-api-key-here", 
            model_name="mixtral-8x7b-32768"
    )
memory=ConversationBufferWindowMemory(k=10)
conversation = ConversationChain(
            llm=client,
            memory=memory
    )

def chat(message):

    bot_response = conversation(message)

    memory.save_context({'input':message},{'output':bot_response['response']})

    return bot_response['response']

demo = gr.Interface(
    fn=chat,
    inputs=["text"],
    outputs=["text"],
)

demo.launch()