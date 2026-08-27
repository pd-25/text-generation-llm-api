from typing import Optional

from pydantic import BaseModel


class LLMResponse(BaseModel):
    response: str

class InputRequest(BaseModel):
    client_api_key: Optional[str] = None
    query_text: str