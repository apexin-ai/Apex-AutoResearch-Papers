# code binoculars scoring

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_binoculars_scoring_20260518T110620_result.json`
- **Structured JSON:** [`bb71f4bb9228dc52e093.json`](../../sessions/bb/bb71f4bb9228dc52e093.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Job is running correctly. Here's the summary:

---

## Status Report

**Method:** Llama-3.2-3B PPL (better than GPT-2-medium; same principle but stronger model)

**Scoring speed:** ~31.3 samples/sec

**Progress:** 28K/371K, ETA ~183 min (~3 hours total)

**Output file:** `/root/provenance_weight_training/data/scored_data_gpt2ppl.jsonl` (symlinks to `/root/autodl-tmp/...`)
- Wait, the symlink was broken. The real file is at `/root/autodl-tmp/provenance_weight_training/data/scored_data_gpt2ppl.jsonl`. The two `data/` dirs are the same physical directory.

**Output format:** Each line is a JSON object with all original fields + `gpt2_ppl` + `gpt2_nll`.

**First 10 entries:**

| # | Type | q_score | gpt2_ppl | gpt2_nll |
|---|------|---------|----------|----------|
| 0 | SYNTH | 0.9681 | 4.54 | 1.51 |
| 1 | SYNTH | 0.9939 | 8.20 | 2.10 |
| 2 | REAL | 0.0634 | 12.90 | 2.56 |
| 3 | SYNTH | 0.9814 | 5.45 | 1.70 |
| 4 | REAL | 0.0959 | 6.31 | 1.84 |
| 5 | SYNTH | 0.9135 | 4.68 | 1.54 |
| 6 | SYNTH | 0.9607 | 4.22 | 1.44 |
| 7 | SYNTH | 0.9211 | 5.35 | 1.68 |
| 8 | SYNTH | 0.9954 | 5.20 | 1.65 |
| 9 | SYNTH | 0.9988 | 5.76 | 1.75 |

**Early pattern:** Synthetic text has lower PPL (~4-8) vs real text (~6-13), consistent with expectations (AI text is more predictable to LLMs). The script will also compute correlation with q_score and optimal classification thresholds when it finishes.

**GPU:** cuda:1 (RTX PRO 6000 Blackwell, ~6.4GB VRAM used)

**Note:** The `scored_data_gpt2ppl.jsonl` path works from both `/root/provenance_weight_training/data/` and `/root/autodl-tmp/provenance_weight_training/data/` since they're the same directory.

---
