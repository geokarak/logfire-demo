# logfire-demo

Instrumented FastAPI application using Pydantic Logfire.

## Quick Start

1. Install the required project dependencies: `make venv`
2. Create and start the PostgreSQL databse:
```bash
docker run --name postgres -p 5432:5432 -e POSTGRES_PASSWORD=postgres -d postgres
```
3. Start the FastAPI app: `python main.py`
4. Start the client: `python client.py`