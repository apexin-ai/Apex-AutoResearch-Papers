# paper instruct nuance update

**Depth Profiling: Classifying Recursive Generation Depth in Base-Model LLM Text** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_instruct-nuance-update_20260515T181413_result.json`
- **Structured JSON:** [`ba35b778fbd9d3df29d6.json`](../../sessions/ba/ba35b778fbd9d3df29d6.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Done. Changes:

**discussion.tex** — `\paragraph{Instruct tuning degrades depth signal.}` replaced with expanded `\paragraph{Instruct tuning degrades depth signal through multiple mechanisms.}`:
- Surface features (TTR, hapax) confounded by length collapse (OLMo-Instruct ρ=−0.370, Qwen3 ρ=−0.583)
- Entropy features show genuine behavioral shifts surviving length control (OLMo-Instruct partial ρ=0.364, Qwen3 partial ρ=0.161)
- Concludes multi-faceted disruption, justifies base-model scope

**limitations.tex** — Instruct paragraph updated: replaces "length confounds dominating the residual signal" with nuanced length-controlled analysis distinguishing surface feature confounds from genuine entropy behavioral changes, with partial ρ values.

Both synced to `docs/paper/`.

---
