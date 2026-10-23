# BeeBridge demo page — design system (v3)

Research basis (Oct 2026): 2026 award-site trend reports (glassmorphism → "liquid
glass", motion-with-meaning micro-animations, bold editorial typography, dark-hero
storytelling), senior-UX guidance (Nielsen Norman / Netguru / Toptal consensus:
≥16px type — we use 19px+, WCAG contrast ≥ 4.5:1, sans-serif body, labelled icons,
minimal information at once, plain language, no time pressure), and narrative
landing-page structure (vivid problem → a person → the turn → the outcome).

## The soul: "The Fading Note"

The page opens with the problem made physical: handwritten sticky notes — the way
seniors actually try to remember — that **blur and fade as a "time passing" slider
moves**. Beside each smearing note sits BeeBridge's crisp, permanent version.
Every later section is the resolution of that first image. Motion is never
decoration: blur = forgetting, sharpness = BeeBridge, a tick = the real world
confirming itself (Ring).

## Themes (switchable in the nav)

| Theme | Language | Palette | Display type |
|---|---|---|---|
| Midnight Honey | Warm dark, hearth-light | Espresso `#171208` · honey `#F5C542` · amber `#FF9E45` · cream `#FFF6E9` | Fraunces |
| Morning Paper | Minimal, editorial, calm | Paper `#F7F1E5` · ink `#241B10` · deep honey `#A86E0C` · terracotta `#C75B2B` | Newsreader |
| Glass Dusk | Glassmorphism + hologram | Deep violet `#171233` mesh · frosted glass `rgba(255,255,255,.07)` + 14px blur · iridescent gold/sky/rose | Sora |

Body text is Public Sans in all themes. Handwriting (the notes, annotations) is
Caveat. All themes keep body text ≥ 18.5px and contrast ≥ 4.5:1 against their
own backgrounds; glass panels sit on a dark enough base to hold that ratio.

## Motifs

- **Doodles:** hand-drawn SVG squiggle underlines, a circled word, a dashed bee
  flight-path that draws itself across the hero — the human, kitchen-table layer.
- **Holograms:** device cards carry an iridescent sheen that follows the pointer
  and a conic-gradient border on hover — strongest in Glass Dusk.
- **Memory artifacts:** the captured moments rendered as physical paper — a
  pharmacy slip, an appointment card, a delivery note with a DELIVERED stamp —
  taped, slightly rotated, real data only.
- **Depth with restraint:** 3D tilt stays on the hero stage and device cards
  (the two places touch/mouse exploration is invited), nowhere else.

## Rules we don't break

1. Every quote on the page is a verbatim output of the shipped software or a
   verbatim line from the bundled Bee sample data.
2. No animation blocks reading; `prefers-reduced-motion` disables tilt, draw
   and reveal.
3. Buttons ≥ 44px, focus always visible, one idea per section.
