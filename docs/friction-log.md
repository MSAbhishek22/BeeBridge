# Friction log (judging-bonus field)

## 1. Bee export layout discovery
- **Task:** ingest real Bee conversations into BeeBridge.
- **Steps:** enabled Developer Mode, ran `bee sync`, inspected the export folder.
- **Expected vs actual:** expected one documented export schema; actual layout required inspecting files to infer fields.
- **Severity:** Medium.
- **Workaround:** BeeBridge's `BeeClient` accepts both JSON exports and markdown exports and normalises them into one `Conversation` model.
- **Suggestion:** publish a versioned export schema with a sample export in the developer docs.

## 2. Alexa+ — MCP vs. classic skill paths
- **Task:** register an Alexa+ experience that calls Bee memory.
- **Steps:** reviewed Agent Skill and MCP documentation, chose self-hosted MCP (2025-11-25, Streamable HTTP).
- **Expected vs actual:** expected one registration checklist; actual guidance is split across Alexa+ and MCP references.
- **Severity:** Medium.
- **Workaround:** shipped both: the MCP server (primary) and a classic skill package + Lambda handler (`alexa-skill/`, `src/beebridge/alexa/lambda_handler.py`) mapping the same intents to the same service.
- **Suggestion:** one end-to-end "Alexa+ MCP quickstart" with a reference server.

## 3. Ring events without a device
- **Task:** react to a package delivery.
- **Steps:** modelled Ring events and fired them at the BeeBridge webhook.
- **Expected vs actual:** expected a hosted simulator endpoint; crafted event payloads by hand instead.
- **Severity:** Low.
- **Workaround:** built the event model + `beebridge_ring_simulate` MCP tool so demos and tests fire realistic events.
- **Suggestion:** ship an official one-click Ring event simulator for developer webhooks.

## 4. Talking to seniors, not at them
- **Task:** make answers understandable for an 80-year-old with hearing loss.
- **Steps:** tested answer wording; shortened sentences; put the Fire TV summary in 24px+ text.
- **Expected vs actual:** default LLM phrasing was too dense.
- **Severity:** Low (product, not platform).
- **Workaround:** deterministic senior-friendly wording offline; Bedrock prompt explicitly instructs short, clear sentences with exact names/dates/doses.
- **Suggestion:** Alexa+ "brief / accessibility" personality presets are valuable — keep investing in them.
