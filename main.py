import os
from pathlib import Path

from dotenv import load_dotenv
from openai import OpenAI
from fastapi import Depends, FastAPI, status
from fastapi.responses import StreamingResponse

from llm_call import generate_response
from schema import InputRequest, LLMResponse

env_path = Path(__file__).resolve().parent / ".env"
load_dotenv(dotenv_path=env_path)

api_key = os.getenv("OPENROUTER_API_KEY")
if not api_key:
    raise RuntimeError("OPENROUTER_API_KEY is not set. Add it to your .env file.")

client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=api_key,
)

app = FastAPI(title="Text Generation from LLM api", version='0.1.0')


@app.get('/query', status_code=status.HTTP_200_OK, description="This endpoint takes key(optional), context then return the response")
def query(input_request: InputRequest = Depends()):
    return StreamingResponse(
        generate_response(client, input_request.query_text),
        media_type="text/event-stream"
    )
    


