"""BeeBridge app: REST API + Alexa+ MCP server + Fire TV web UI, one service.

Run:  uvicorn beebridge.main:app --app-dir src --port 8000
Or:   python -m beebridge.main
"""
from __future__ import annotations

import os
from pathlib import Path

from fastapi import FastAPI
from fastapi.responses import FileResponse
from pydantic import BaseModel

from .alexa.mcp_server import build_mcp_router
from .bee.client import BeeClient
from .core.models import Conversation
from .core.service import BeeBridgeService
from .core.store import MemoryStore
from .ring.simulator import RingEvent, handle_ring_event

DB_PATH = os.environ.get("BEEBRIDGE_DB", "beebridge.db")
store = MemoryStore(DB_PATH if DB_PATH != ":memory:" else ":memory:")
service = BeeBridgeService(store=store, bee=BeeClient())
# Ingest Bee exports on startup so the demo is alive immediately.
service.sync_from_bee()

app = FastAPI(title="BeeBridge", version="0.1.0",
              description="Memory companion for seniors: Bee -> Alexa+ MCP, Ring alerts, Fire TV summary.")
app.include_router(build_mcp_router(service))

WEB_DIR = Path(__file__).resolve().parents[2] / "web"


class AskRequest(BaseModel):
    question: str


class IngestRequest(BaseModel):
    conversation: Conversation


@app.get("/health")
def health():
    return {"status": "ok", "service": "beebridge", "counts": store.counts(),
            "bee_cli_available": service.bee.cli_available(),
            "bedrock_available": service.summarizer.available()}


@app.post("/api/sync")
def sync():
    return service.sync_from_bee()


@app.get("/api/today")
def today():
    return service.today_summary()


@app.post("/api/ask")
def ask(req: AskRequest):
    return service.ask(req.question)


@app.get("/api/todos")
def todos():
    return [t.model_dump(mode="json") for t in store.list_todos()]


@app.post("/api/todos/{todo_id}/done")
def todo_done(todo_id: str):
    todo = store.mark_todo_done(todo_id)
    return {"done": bool(todo), "todo": todo.model_dump(mode="json") if todo else None}


@app.get("/api/conversations")
def conversations():
    return [c.model_dump(mode="json") for c in store.list_conversations()]


@app.post("/api/conversations")
def ingest(req: IngestRequest):
    return service.ingest(req.conversation)


@app.get("/api/alerts")
def alerts():
    return [a.model_dump(mode="json") for a in store.list_alerts()]


@app.post("/api/ring/events")
def ring_event(event: RingEvent):
    """Ring API / simulator webhook."""
    return handle_ring_event(store, event).model_dump(mode="json")


@app.get("/tv")
def tv_ui():
    return FileResponse(WEB_DIR / "index.html")


def run():
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=int(os.environ.get("PORT", "8000")))


if __name__ == "__main__":
    run()
