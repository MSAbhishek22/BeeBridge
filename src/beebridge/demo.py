"""Two-minute demo, no hardware needed:  python -m beebridge.demo

Seeds BeeBridge from the bundled Bee exports, asks the questions a
senior would ask Alexa, then fires a Ring package-delivery event.
"""
from __future__ import annotations

from .core.service import BeeBridgeService
from .core.store import MemoryStore
from .ring.simulator import RingEvent, RingEventKind, handle_ring_event


def main() -> None:
    svc = BeeBridgeService(store=MemoryStore(":memory:"))
    print("== Bee sync ==")
    print(svc.sync_from_bee())
    print("\n== Alexa, what do I need to do today? ==")
    print(svc.ask("What do I need to do today?")["answer"])
    print("\n== Alexa, what did the doctor say? ==")
    print(svc.ask("What did the doctor say about my next appointment?")["answer"])
    print("\n== Alexa, what medication do I take? ==")
    print(svc.ask("What medication do I need to take?")["answer"])
    print("\n== Alexa, what did Mom say? ==")
    print(svc.ask("What did Mom talk about?")["answer"])
    print("\n== Ring: package delivered ==")
    alert = handle_ring_event(svc.store, RingEvent(kind=RingEventKind.PACKAGE_DELIVERY))
    print("Alexa announcement:", alert.text)
    print("\nOpen todos after delivery:", [t.text for t in svc.store.list_todos()])


if __name__ == "__main__":
    main()
