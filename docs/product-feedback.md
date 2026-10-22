# Product feedback (hackathon submission field)

## Bee (wearable AI) — primary track
- **Used for:** capturing real conversations (doctor call, family call, pharmacy visit) and exposing them to BeeBridge via the Bee CLI (`bee sync`, `bee today`), Bee sync exports, and Bee's MCP surface.
- **Worked well:** the CLI/export model is exactly right for developers — conversations arrive as portable markdown/JSON, so a downstream app can build memory features without a proprietary sync protocol. The physical consent switch is a genuine trust feature for senior users, and we say so in the product.
- **Needs work:** discovering the exact export layout and MCP endpoint from the docs took trial and error; a single "developer quickstart: get today's conversations in 5 lines" page would cut onboarding from hours to minutes. A streaming/webhook option (push a new conversation when it's processed) would remove polling via `bee sync`.
- **Onboarding:** moderate — Developer Mode is a sensible gate, but the path from "device paired" to "first CLI data" should be one guided flow.
- **Build again?** Yes — Bee is the only device in the lineup whose data model *is* memory, which makes it uniquely buildable for accessibility products.

## Alexa+ (MCP / Agent Skills)
- **Used for:** the conversational front door — seniors ask Alexa+ questions and BeeBridge's self-hosted MCP server (Streamable HTTP, protocol 2025-11-25) answers from Bee memory. Tools: `beebridge_ask`, `beebridge_today`, `beebridge_todos`, `beebridge_sync_bee`, `beebridge_ring_simulate`.
- **Worked well:** standardising on MCP means one server serves Alexa+, Bee tooling, and any MCP client. Tool descriptions carry the product semantics, so the agent picks the right tool without custom intent plumbing.
- **Needs work:** the Agent Skill registration flow and the MCP path are documented in different places; a single checklist ("register skill → point at MCP URL → test utterances") would help. Local testing against a tunnelled MCP server should be a first-class flow.
- **Build again?** Yes — MCP is the right abstraction for agent skills.

## Ring
- **Used for:** contextual safety alerts via Ring-style events (doorbell press, motion, person detected, package delivery) posted to `POST /api/ring/events`, matching Bee-captured expectations (e.g. a package a family member mentioned).
- **Worked well:** the event model is clean and simulator-friendly — no physical device needed to build a real integration.
- **Needs work:** a hosted, one-click simulator that fires signed events at a developer webhook would be better than hand-crafting payloads; event schema docs should be linked directly from the hackathon resources page.
- **Build again?** Yes, especially for caretaking use cases.

## AWS (AWS Builder mini challenge)
- **Used:** **Amazon Bedrock** (Converse API, `src/beebridge/aws/bedrock.py`) to rephrase memory summaries into short, clear, senior-friendly sentences with names/dates/doses preserved; **Lambda + API Gateway + DynamoDB** deployment defined in `infra/aws/template.yaml` (SAM).
- **Worked well:** Bedrock Converse is a single API across models, so swapping Nova/Claude is a config change. SAM made the whole hosted path a single file.
- **Needs work:** Bedrock model access approval is still a speed bump for first-time builders on a deadline.

## Fire TV
- **Used for:** the large-text daily summary UI (`web/index.html`, served at `/tv`) — designed to be readable from a sofa by an older adult.
- **Worked well:** a standards-based web UI runs in the Fire TV/Vega browser with zero porting.
- **Needs work:** clearer guidance on which browser surface is the recommended demo path vs. a native app for a 2-day build.
