# Demo video script — under 3 minutes, leads with the best material

Record: screen (Fire TV UI + terminal) + voiceover, English, public YouTube/Vimeo. No third-party music/logos.

**0:00–0:20 — The problem**
"This is BeeBridge. One in three seniors leaves a doctor's appointment unsure what was actually said. BeeBridge remembers — so they don't have to."

**0:20–0:55 — Bee captures (show terminal + sample/live Bee data)**
- Show a Bee conversation arriving: run `python -m beebridge.demo` or the live app syncing.
- "This morning, Bee heard a call with Dr. Patel. BeeBridge extracted the medication, the health facts, and the next appointment — automatically. No typing, no app to learn."

**0:55–1:35 — Alexa+ answers (the money moment)**
- "Alexa, what did the doctor say about my next appointment?"
- Show the MCP call (`beebridge_ask`) and Alexa's answer: appointment Friday 10am, blood pressure improved, bring the blood-sugar log.
- "Alexa, what medication do I take?" → Metformin 500mg with breakfast, Vitamin D at night.

**1:35–2:10 — Ring completes the loop**
- Fire the Ring package-delivery event (simulator / `beebridge_ring_simulate`).
- "Mom said a package was coming. Ring just saw it arrive — and BeeBridge connects those two moments: 'Your package has arrived.' The to-do completes itself."
- Show the Fire TV screen updating with the alert.

**2:10–2:40 — Fire TV summary + stack**
- Pan the large-text Today screen: summary, to-dos, alerts, conversations.
- "Bee for memory, Alexa+ over MCP for voice, Ring for the front door, Amazon Bedrock on AWS for clear summaries. All open source, MIT."

**2:40–2:55 — Close**
"BeeBridge: a second memory, in the ear and in the home. Built for the Amazon Developer Hackathon."
