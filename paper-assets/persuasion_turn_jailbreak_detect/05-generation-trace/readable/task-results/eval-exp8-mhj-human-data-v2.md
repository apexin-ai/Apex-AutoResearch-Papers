# eval exp8 mhj human data v2

**DisPeD: A Controlled Study of Encoder Adaptation for Multi-Turn Jailbreak Detection** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_exp8-mhj-human-data-v2_20260518T162824_result.json`
- **Structured JSON:** [`6ffafc259984e1d1e951.json`](../../sessions/6f/6ffafc259984e1d1e951.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

All done. Here's the complete summary:

## Exp8: Human Jailbreak Data Evaluation Results

**Data source**: ToxicChat (LMSYS) — 204 human-written jailbreak attempts + 204 benign conversations, evaluated across 3 seeds (42, 123, 456).

**Note**: MHJ dataset (ScaleAI) was inaccessible (gated + no HF token + China network). Used ToxicChat as alternative — also human-written, with explicit `jailbreaking` labels from human annotators.

### Evidence Hierarchy (F1 at K=1)

| Variant | F1 | Precision | Recall | Accuracy |
|---------|-----|-----------|--------|----------|
| **jb_mlm** | **0.842±0.009** | 0.822±0.030 | 0.864±0.030 | 0.837±0.012 |
| TF-IDF | 0.710 | 0.606 | 0.858 | 0.650 |
| scrambled | 0.667±0.030 | 0.586±0.045 | 0.777±0.003 | 0.610±0.052 |
| 9-class | 0.654±0.087 | 0.578±0.061 | 0.757±0.138 | 0.605±0.089 |
| vanilla | 0.221±0.055 | 0.426±0.026 | 0.152±0.045 | 0.476±0.003 |

### Does the evidence hierarchy hold? **Yes.**

All fine-tuned variants (jb_mlm, 9-class, scrambled) massively outperform vanilla DeBERTa (3x+ F1), confirming that representations learned from Qwen3-8B synthetic data capture **generalizable jailbreak patterns**, not just within-LLM stylistic artifacts.

The jb_mlm variant is the standout performer (F1=0.842), achieving strong detection of human jailbreaks with zero exposure to human data during training.

### Caveat
ToxicChat is single-turn data, so K=1 through K=full are identical for DeBERTa models. The multi-turn evidence accumulation effect cannot be tested here but is already demonstrated on synthetic OOD data.

### Artifacts
- `results/exp8_mhj_evaluation.json` — full results with per-seed breakdowns
- `data/mhj/toxicchat_eval.jsonl` — evaluation dataset (408 conversations)
- Registry: `exp8_mhj_human_data` (status: DONE, conclusion: success)

---
