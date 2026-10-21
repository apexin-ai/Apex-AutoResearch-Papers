# ssh diversity probe

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_diversity-probe_20260514T232333_result.json`
- **Structured JSON:** [`90f573c0a47b54920ae7.json`](../../sessions/90/90f573c0a47b54920ae7.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Diversity probe is nearly complete. Sample 3 T=1.0 is finishing (gen 3/8, ~5 min remaining) but it's all truncated outputs — won't change the conclusions.

**Summary of findings:**

| | T=0.7 | T=1.0 |
|---|---|---|
| Unique triple-sets | 7.0/8 avg | 8.0/8 avg |
| Jaccard similarity | 0.170 | 0.051 |
| Format OK rate | 50.0% | 43.8% |
| F1 | 0.000 | 0.000 |

**Conclusions in `artifacts/diversity_probe_results.md`:**
1. **Diversity is sufficient** — RSFT is viable. 6-8 unique outputs per 8 generations.
2. **Format compliance (~50%) is the main risk** — field name instability (`head` vs `head_entity`, `evidence` vs `sentence_ids`).
3. **F1=0 is a measurement artifact** — relation name mismatch (e.g. "founded" vs "inception"). CED reward must be used instead.
4. **Recommended RSFT config**: T=0.7, N=8, max_new_tokens=2048, CED reward + format gating.

---
