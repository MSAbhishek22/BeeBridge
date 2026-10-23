# Devpost submission — copy/paste pack
Hackathon: **Build, Ship, Shape: Amazon Developer Hackathon** · Deadline: **Oct 24, 2026, 12:30am IST**
Devpost user: `msabhishekanni10` · GitHub user: `MSAbhishek22`

## Project name
BeeBridge: A Memory Companion for Seniors

## Tagline
Bee remembers the conversation. Alexa+ answers the question. Ring watches the door. BeeBridge connects all three into a second memory for seniors.

## Live demo (hosted)
https://msabhishek22.github.io/BeeBridge/ — interactive GitHub Pages demo (`docs/index.html`): tap-a-question answers from the real backend outputs, today's summary, Ring package simulation. Put this as the FIRST "Try it out" link on Devpost; repo second.

## Tracks / mini challenges to select
- **Primary track: Alexa+** — DECIDED 2026-10-22. The submission's centrepiece is a self-hosted MCP server (spec 2025-11-25, Streamable HTTP) + Agent Skill answering from Bee memory (`src/beebridge/alexa/`). Rationale: $25,000 first prize vs Bee's $12,000, and the MCP server is fully judge-runnable evidence (see placement strategy below).
- Data source, featured throughout: **Bee** (real Bee data via Bee CLI + Bee MCP + Bee sync exports — `src/beebridge/bee/`)
- Also demonstrates: **Ring** (simulator/API events) and a **Fire TV** summary UI
- **Mini challenge: AWS Builder** — Amazon Bedrock (Converse) for summaries; Lambda + API Gateway + DynamoDB SAM template (`infra/aws/template.yaml`)
- **Mini challenge: Open Source** — see fields below

## Text description (paste)
BeeBridge is a voice-driven memory assistant for seniors and caregivers. A Bee wearable captures everyday conversations — a doctor explaining medication, a daughter confirming Sunday lunch, a pharmacist handing over a refill — and BeeBridge converts them into structured memory: health facts, medication schedules, appointments, and to-dos.

Later, the senior simply asks: "Alexa, what did the doctor say about my next appointment?" BeeBridge's self-hosted MCP server (built for Alexa+, Streamable HTTP, protocol 2025-11-25) searches the Bee memory and answers in short, clear sentences — Amazon Bedrock rephrases summaries when AWS is configured. Ring adds the front door: when a package the family mentioned actually arrives, Ring's delivery event completes the matching Bee to-do and Alexa announces it; a doorbell press becomes a clear alert on the large-text Fire TV summary screen.

It was built during the hackathon window: the Bee ingestion (CLI/MCP/exports), the deterministic fact/to-do extractor, the MCP server, the Ring event matching, the Fire TV UI, the Bedrock integration, tests, and all documentation are new. The bundled sample Bee exports let anyone run the full pipeline without a device; with a Bee, the same code ingests real data by pointing `BEE_EXPORT_DIR` at a Bee sync folder or setting `BEE_MCP_URL`.

Privacy is a feature, not a footnote: Bee records only with consent, memory is stored locally by default, and nothing is shared with caregivers unless the user enables it.

## What to submit — checklist
- [ ] Text description (above)
- [x] GitHub repo: https://github.com/MSAbhishek22/BeeBridge — code pushed (commit `e2ab8a8`, 40 files, blob-verified). **Visibility DECIDED 2026-10-22: PUBLIC** (user's choice). With the MIT license included, this satisfies the hackathon's "public and open source" repo route — judges and the Amazon team can review it directly, no collaborator invites needed.
- [ ] Demo video < 3 min, public, English (script: `docs/demo-script.md`)
- [ ] Product feedback (paste `docs/product-feedback.md`)
- [ ] Friction log (paste `docs/friction-log.md`) — up to 10% judging bonus
- [ ] Tracks/mini challenges selected (above)
- [ ] "Built during the window" explanation (in description above)

## Repo sharing
**Not required anymore:** the repo is public (decided 2026-10-22), which is one of the two routes the hackathon accepts (public + open-source license included). The Amazon reviewers (`knmeiss`, `giolaq`, `anishamalde`, `mosesroth`, `emersonsklar`) and `testing@devpost.com` can review https://github.com/MSAbhishek22/BeeBridge directly. (The collaborator-invite route only applies to private repos; if the repo is ever flipped back to private, add those five collaborators at submission time — invitations expire after 7 days.)

## Open Source mini challenge — extra fields
- **Project:** Bee Memory MCP — a *separate, additional* open-source project (MIT), built during the window, so this entry is valid even though the main BeeBridge repo is private.
- **Repo URL:** https://github.com/MSAbhishek22/bee-memory-mcp (PUBLIC, live, commit `c879ff7`)
- **GitHub username:** `MSAbhishek22`
- **Contribution URL:** same as repo URL (new open-source project, MIT license file included)
- **Description:** Bee Memory MCP is a new open-source MCP server (MIT) that makes Bee wearable memory queryable by any MCP client (Alexa+, desktop agents, custom tools). It ingests Bee conversations via the Bee CLI / sync exports / Bee MCP, extracts facts, medication, appointments and to-dos, and serves them over MCP (Streamable HTTP, 2025-11-25), with optional Amazon Bedrock summaries. It matters because ambient memory help — for seniors, people with ADHD, or hearing loss — should be inspectable, self-hostable, and free of lock-in.

## Prize-money placement strategy (read before selecting tracks on Devpost)
Cash by track: Alexa+ 1st $25,000 / 2nd $15,000 / 3rd $4,000 · Fire TV $25k/$15k/$4k · Bee 1st $12,000 / 2nd $8,000 (no 3rd) · Ring $12k/$8k · Minis: $5,000 each (a project can win ONE track prize + ONE mini prize).
- As **Bee primary**: ceiling = $12,000 + $5,000 mini = **$17,000**. Risk: Bee judging requires the demo/code to show *live Bee device data* — without a physical Bee, the sample-export demo is our weakest evidence.
- As **Alexa+ primary**: ceiling = $25,000 + $5,000 mini = **$30,000**. Our Alexa+ evidence is the strongest we have: a real, spec-exact (2025-11-25), stress-tested MCP server that judges can run and curl themselves, with Bee as the data source featured throughout the description and video.
- Fire TV primary ($25k) is not recommended: our Fire TV piece is a web UI, not a native Fire OS/Vega app, and that demo must show a real device/simulator.
- **Recommendation: select Alexa+ as the primary track, enter both mini challenges (AWS Builder + Open Source via Bee Memory MCP).** Bee stays front-and-centre in the story, description, and video — it is the data source the Alexa+ experience is built on.

## AWS Builder mini challenge — extra fields
AWS services used: **Amazon Bedrock** (Converse API; senior-friendly summary rephrasing, model configurable, default `amazon.nova-micro-v1:0`), **AWS Lambda + API Gateway** (hosted MCP/REST path), **Amazon DynamoDB** (hosted memory store option). Documented in `README.md`, implemented in `src/beebridge/aws/bedrock.py`, deployable via `infra/aws/template.yaml`.

## Feature requests (optional field)
1. **Bee (important):** a push/webhook event when Bee finishes processing a conversation, plus a published, versioned sync-export schema + sample export in the docs.
2. **Alexa+ (important):** a single end-to-end MCP quickstart and a first-class local-tunnel testing flow for self-hosted MCP servers.
3. **Ring (nice-to-have):** a hosted one-click event simulator that fires signed events at a developer webhook.
