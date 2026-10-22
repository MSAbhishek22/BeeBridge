import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from fastapi.testclient import TestClient

from beebridge.core.extractor import extract
from beebridge.core.models import Conversation
from beebridge.core.service import BeeBridgeService
from beebridge.core.store import MemoryStore
from beebridge.ring.simulator import RingEvent, RingEventKind, handle_ring_event


def make_service():
    svc = BeeBridgeService(store=MemoryStore(":memory:"))
    svc.sync_from_bee()
    return svc


def test_bee_sample_ingest_extracts_todos_and_facts():
    svc = make_service()
    counts = svc.store.counts()
    assert counts["conversations"] >= 3
    kinds = {t.kind.value for t in svc.store.list_todos(include_done=True)}
    assert "medication" in kinds
    assert "delivery" in kinds


def test_extractor_medication():
    conv = Conversation(id="c1", title="t", transcript="Please take Metformin 500mg every morning.")
    facts, todos = extract(conv)
    assert any(t.kind.value == "medication" for t in todos)


def test_ask_doctor():
    svc = make_service()
    ans = svc.ask("What did the doctor say about my next appointment?")
    assert "Friday" in ans["answer"] or "appointment" in ans["answer"].lower()
    assert ans["sources"]


def test_ask_medication():
    svc = make_service()
    ans = svc.ask("What medication do I need to take?")
    assert "Metformin" in ans["answer"]


def test_ask_today():
    svc = make_service()
    ans = svc.ask("What do I need to do today?")
    assert ans["answer"]


def test_ring_package_completes_delivery_todo():
    svc = make_service()
    before = [t for t in svc.store.list_todos() if t.kind.value == "delivery"]
    assert before
    alert = handle_ring_event(svc.store, RingEvent(kind=RingEventKind.PACKAGE_DELIVERY))
    assert "package has arrived" in alert.text.lower()
    after = [t for t in svc.store.list_todos() if t.kind.value == "delivery"]
    assert not after


def test_mcp_initialize_and_tools():
    from beebridge.main import app
    client = TestClient(app)
    r = client.post("/mcp", json={"jsonrpc": "2.0", "id": 1, "method": "initialize",
                                  "params": {"protocolVersion": "2025-11-25"}})
    assert r.status_code == 200
    assert r.json()["result"]["protocolVersion"] == "2025-11-25"
    r = client.post("/mcp", json={"jsonrpc": "2.0", "id": 2, "method": "tools/list", "params": {}})
    names = {t["name"] for t in r.json()["result"]["tools"]}
    assert "beebridge_ask" in names and "beebridge_today" in names
    r = client.post("/mcp", json={"jsonrpc": "2.0", "id": 3, "method": "tools/call",
                                  "params": {"name": "beebridge_ask",
                                             "arguments": {"question": "What medication do I take?"}}})
    body = r.json()["result"]["content"][0]["text"]
    assert "Metformin" in body


def test_api_endpoints():
    from beebridge.main import app
    client = TestClient(app)
    assert client.get("/health").json()["status"] == "ok"
    assert client.get("/api/today").status_code == 200
    r = client.post("/api/ring/events", json={"kind": "doorbell_press", "device_name": "Front Door"})
    assert "front door" in r.json()["text"].lower()
    assert client.get("/tv").status_code == 200
