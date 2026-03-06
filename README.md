# 🤖 AI Customer Support Agent

A production-grade AI support agent built with FastAPI and LangChain. Designed to handle customer queries automatically with fallback logic for reliability.

## 🚀 Features
- **FastAPI Backend**: High-performance async API
- **AI Integration**: LangChain + OpenAI (with mock fallback for reliability)
- **Error Handling**: Graceful degradation when API quotas are exceeded
- **Logging**: Professional request tracking for debugging
- **Security**: Environment variables managed securely (.env ignored)

## 🛠️ Tech Stack
- Python 3.12
- FastAPI
- LangChain
- Uvicorn

## 🏃 How to Run

1. Clone the repo
2. Install dependencies:
   pip install -r requirements.txt

3. Create a .env file with your OPENAI_API_KEY
4. Run the server:
   python main.py

5. Visit http://127.0.0.1:8001/docs

## 📬 Contact
Built by Vignesh | Open to Remote Opportunities
