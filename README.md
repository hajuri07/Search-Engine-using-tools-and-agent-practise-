**# Search-Engine-using-tools-and-agent-practise-
Practice project: Streamlit chatbot using LangChain + Groq with search tools (Wiki, ArXiv, DuckDuckGo). Built in Colab and exposed via Cloudflare Tunnel to understand agents, tools, and deployment flow.
**# LangChain + Groq: AI Search Agent 🤖

A simple practice project to learn how to build a ** Agent** using LangChain and Groq. This chatbot doesn't just talk; it can search the web, Wikipedia, and Arxiv to provide up-to-date information.

## 🚀 Features
- **Real-time Web Search:** Uses DuckDuckGo to find current events.
- **Academic Research:** Pulls paper summaries from Arxiv.
- **General Knowledge:** Queries Wikipedia for quick facts.
- **Llama 3 Powered:** Fast inference using Groq's LPUs.
- **Thought Visualization:** Uses Streamlit Callback Handler to show the agent's "reasoning" process.

## 🛠️ Tech Stack
- **Framework:** [Streamlit](https://streamlit.io/)
- **Orchestration:** [LangChain](https://www.langchain.com/) & [LangGraph](https://langchain-ai.github.io/langgraph/)
- **LLM:** Meta Llama 3 (via Groq)
- **Tools:** Wikipedia API, Arxiv API, DuckDuckGo Search

## 📋 Prerequisites
Before running the app, you'll need a Groq API Key. You can get one for free at [console.groq.com](https://console.groq.com/).

## 💻 How to Run

1. **Clone the repo:**
   ```bash
   
2 .Install dependencies:

Bash
pip install -r requirements.txt

3. Run the app:

Bash
streamlit run your_filename.py
4. Usage:

Enter your Groq API key in the sidebar.

Ask a question like "What is the latest news in Quantum Computing?" or "Explain Deep Learning."

📝 Note
This project was built for practice purposes to understand agentic workflows and tool-calling in the LangChain ecosystem.


---

### A Quick Tip for your GitHub Repo
When you upload this to GitHub, make sure you **don't** hardcode your API key in the code. Using the `st.sidebar.text_input` method you already have is perfect because it keeps the key in memory without saving it to your public files.

Made by Hajuri
