from fastapi import FastAPI, Request
from llm_handler import query_llm

app = FastAPI()

@app.post("/chat")
async def chat_endpoint(request: Request):
    data = await request.json()
    user_message = data.get("message")
    messages = [{"role": "user", "content": user_message}]
    reply = query_llm(messages)
    return {"reply": reply}
