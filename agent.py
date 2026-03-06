from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage, SystemMessage
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

def get_support_response(user_question):
    """
    Sends user question to OpenAI. 
    Falls back to mock response if API fails (for development).
    """
    try:
        # Initialize the AI Model
        llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0.7)
        
        # Define the personality
        system_message = SystemMessage(
            content="You are a helpful customer support agent for a tech startup. "
                    "Keep answers short, friendly, and professional. "
                    "If you don't know the answer, say 'Let me connect you with a human.'"
        )
        
        human_message = HumanMessage(content=user_question)
        
        # Get response from AI
        response = llm.invoke([system_message, human_message])
        
        return response.content
    
    except Exception as e:
        # PRODUCTION TIP: Log the actual error internally, show user a friendly message
        print(f"⚠️ API Error (Switching to Mock Mode): {str(e)}")
        
        # Mock Response (So development continues)
        if "password" in user_question.lower():
            return "🤖 [MOCK] To reset your password, go to Settings > Security > Reset."
        elif "invoice" in user_question.lower() or "billing" in user_question.lower():
            return "🤖 [MOCK] You can find your invoices in Settings > Billing > Invoices."
        else:
            return "🤖 [MOCK] Thanks for asking! Our team will help you shortly. (API Quota Exceeded)"