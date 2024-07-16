import httpx

with httpx.Client(timeout=None) as client:
    while True:
        resp = client.get("http://localhost:8000/hello/world")
        resp.raise_for_status()
