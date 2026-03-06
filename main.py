from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from agent import get_support_response
from dotenv import load_dotenv
import os
import logging
from datetime import datetime

# Load environment variables
load_dotenv()

# Setup Logging (Production Standard)
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler("app.log"),  # Saves to file
        logging.StreamHandler()          # Prints to terminal
    ]
)
logger = logging.getLogger(__name__)

# Initialize the App
app = FastAPI(title="Support Agent API", version="1.0.0")

class QuestionRequest(BaseModel):
    question: str

@app.get("/health")
def health_check():
    logger.info("Health check requested")
    return {"status": "healthy", "service": "support-agent"}

@app.post("/ask")
def ask_agent(request: QuestionRequest):
    logger.info(f"Received question: {request.question}")
    
    if not os.getenv("OPENAI_API_KEY"):
        logger.error("API Key missing")
        raise HTTPException(status_code=500, detail="API Key missing")
    
    try:
        answer = get_support_response(request.question)
        logger.info("Successfully generated response")
        return {"question": request.question, "answer": answer}
    
    except Exception as e:
        logger.error(f"Error processing request: {str(e)}")
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    import uvicorn
    logger.info("Starting Server at http://127.0.0.1:8001")
    uvicorn.run(app, host="127.0.0.1", port=8001)