# Text Generation LLM API

A FastAPI-based service that streams text responses from an OpenRouter-powered LLM. The app is lightweight, easy to run locally, and exposes interactive API docs through Swagger UI.

Live demo:
- Swagger UI: https://text-generation-llm-api.onrender.com/docs#/
- Base URL: https://text-generation-llm-api.onrender.com

## Features

- FastAPI backend
- Streaming text generation responses
- OpenRouter integration via the OpenAI SDK
- Health check endpoint
- Swagger/OpenAPI documentation
- Simple request model for passing text prompts

## Tech Stack

- Python 3.13+
- FastAPI
- Uvicorn
- OpenAI Python SDK
- python-dotenv

## Project Structure

- `main.py` — FastAPI app and route definitions
- `llm_call.py` — LLM request logic and streaming response generation
- `schema.py` — request/response models
- `.env` — local environment file with the OpenRouter API key
- `pyproject.toml` — project dependencies

## Local Setup

1. Clone the repository:

```bash
git clone <your-repo-url>
cd text-generation-llm-api
```

2. Install dependencies:

```bash
uv sync
```

If you are not using `uv`, create a virtual environment and install the project dependencies manually.

3. Create a `.env` file in the project root:

```env
OPENROUTER_API_KEY=your_openrouter_api_key_here
```

4. Run the app:

```bash
uv run uvicorn main:app --reload
```

5. Open the docs in a browser:

```text
http://127.0.0.1:8000/docs
```

## API Endpoints

### GET /health

Returns a basic health response with the current server time.

Example response:

```json
{
  "succes": true,
  "time": "2026-09-01T12:00:00"
}
```

### GET /query

Streams a generated response from the configured LLM.

Query parameters:
- `query_text` (required): The prompt or question to send to the model
- `client_api_key` (optional): Included for compatibility, but the server reads the API key from `.env`

Example:

```bash
curl "http://127.0.0.1:8000/query?query_text=Explain%20REST%20in%20one%20sentence"
```

## Notes

- The application currently loads the API key from the server environment (`.env`), not from the request body.
- The `/query` endpoint streams the model output as text, which is useful for long-form or incremental responses.
- The live deployment is available at the URL above and includes Swagger docs for testing the API.

## License

This project is for learning and personal use unless otherwise specified by the repository owner.
