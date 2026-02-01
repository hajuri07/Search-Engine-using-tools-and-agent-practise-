import streamlit as st

from langchain_groq import ChatGroq
from langchain_community.utilities import ArxivAPIWrapper, WikipediaAPIWrapper
from langchain_community.tools import ArxivQueryRun, WikipediaQueryRun, DuckDuckGoSearchResults
from langchain_community.callbacks import StreamlitCallbackHandler

from langchain_core.messages import HumanMessage, AIMessage
from langgraph.prebuilt import create_react_agent


# Tools
arxiv_wrapper = ArxivAPIWrapper(top_k_results=1, doc_content_chars_max=200)
arxiv = ArxivQueryRun(api_wrapper=arxiv_wrapper)

wiki_wrapper = WikipediaAPIWrapper(top_k_results=1, doc_content_chars_max=200)
wiki = WikipediaQueryRun(api_wrapper=wiki_wrapper)

search = DuckDuckGoSearchResults(name="Search")  # returns search snippets


st.title("LangChain Chat with search")
st.sidebar.title("Settings")
api_key = st.sidebar.text_input("Enter your Groq API key here:", type="password")

if "messages" not in st.session_state:
    st.session_state["messages"] = [
        {"role": "assistant", "content": "Hi, I am a chatbot who can search the web. How can I help you?"}
    ]

# render chat history
for msg in st.session_state.messages:
    st.chat_message(msg["role"]).write(msg["content"])

if prompt := st.chat_input(placeholder="What is Deep learning?"):
    st.session_state.messages.append({"role": "user", "content": prompt})
    st.chat_message("user").write(prompt)

    if not api_key:
        st.info("Please add your Groq API key to continue.")
        st.stop()

    # Groq LLM (LangChain docs: use GROQ_API_KEY env var, but passing key works too)
    llm = ChatGroq(
        groq_api=api_key,          # if this errors, change to groq_api_key=api_key
        model_name="llama3-8b-8192",
        streaming=True,
        temperature=0,
    )

    tools = [search, arxiv, wiki]

    # ✅ NEW: create a ReAct agent
    agent = create_react_agent(llm, tools)

    # convert Streamlit dict messages -> LangChain message objects
    lc_messages = []
    for m in st.session_state.messages:
        if m["role"] == "user":
            lc_messages.append(HumanMessage(content=m["content"]))
        else:
            lc_messages.append(AIMessage(content=m["content"]))

    with st.chat_message("assistant"):
        st_cb = StreamlitCallbackHandler(st.container(), expand_new_thoughts=False)

        result = agent.invoke(
            {"messages": lc_messages},
            config={"callbacks": [st_cb]},
        )

        # agent returns updated message list
        response = result["messages"][-1].content
        st.session_state.messages.append({"role": "assistant", "content": response})
        st.write(response)
