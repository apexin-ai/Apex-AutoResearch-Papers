# infra mvp llama phase a

**English-Chinese Knowledge Conflict Signals Are Consistent With General Cross-Lingual Asymmetries** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_infra_mvp_llama_phase_a_20260521T133704_result.json`
- **Structured JSON:** [`3ae8f43428dc9e237911.json`](../../sessions/3a/3ae8f43428dc9e237911.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Output format is correct — includes `qwen_parametric_answer`, `qwen_agrees_with`, and `original_label` fields.

**Llama-3.1-8B MVP Phase A — Complete. Results:**

| | Train | Test |
|---|---|---|
| **Input entries** | 800 | 200 |
| **Unique questions** | 395 | 100 |
| **Kept** | 266 (33.2%) | 70 (35.0%) |
| **Discarded** (neither) | 534 (66.8%) | 130 (65.0%) |
| **Flipped** | 54 (20.3% of kept) | 14 (20.0% of kept) |
| **Unchanged** | 212 | 56 |

**Key observations:**
- ~65% discard rate — Llama-3.1-8B's parametric answers matched neither ground truth nor ChatGPT's memory for most questions, much higher ambiguity than typical
- ~20% label flip rate among kept samples — consistent across train/test
- Both splits below 300 samples (WARNING triggered) — may need supplementary sampling
- Output files: `data/llama31/en_conflict_train_verified.jsonl` (266 lines), `data/llama31/en_conflict_test_verified.jsonl` (70 lines)

---
