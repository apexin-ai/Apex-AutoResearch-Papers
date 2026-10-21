# analysis r16 beam wikievents 70b

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_r16_beam_wikievents_70b_20260521T033801_result.json`
- **Structured JSON:** [`b3435c431c13ab164b3f.json`](../../sessions/b3/b3435c431c13ab164b3f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Results written to `artifacts/r16_verification/beam_wikievents_70b.json`.

### Sub-task 1: Beam 998-doc Progress

| | Qwen (westd-21461) | Llama (westd-16980) |
|---|---|---|
| Status | Running (7h18m) | Running (5h52m) |
| Progress | **799/998 (80.1%)** | **852/998 (85.4%)** |
| Rate | 1.82 docs/min | 2.42 docs/min |
| ETA | ~109 min (~1h50m) | ~60 min (~1h) |

Llama is faster per-doc and should finish first. Both have occasional FAIL docs (timeout at ~115s).

### Sub-task 2: WikiEvents Test Split

**20 docs is the full official test split.** WikiEvents (Li et al., 2021) splits: train=206, dev=20, test=20, total=246. Confirmed by `all.jsonl` = 246 lines on server. The `train.jsonl` (12 lines) is a curated SFT subset, not the full training set.

### Sub-task 3: 70B LoRA Feasibility

**Feasible, with large headroom.**

- GPU: NVIDIA RTX PRO 6000 Blackwell Server Edition, **96GB VRAM** per card (2 cards)
- 70B AWQ INT4 estimate: ~43GB total (38GB model + 1.5GB LoRA + 3GB KV cache + 0.5GB constraint)
- Headroom: **~33GB** on cuda:1
- Model already downloaded: `/root/autodl-tmp/models/LLM-Research/Meta-Llama-3___1-70B-Instruct-AWQ-INT4` (38G)
- No blockers

---
