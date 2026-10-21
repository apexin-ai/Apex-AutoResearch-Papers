# train plan003 scrambled ablation

**DisPeD: A Controlled Study of Encoder Adaptation for Multi-Turn Jailbreak Detection** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_train_plan003-scrambled-ablation_20260517T224408_result.json`
- **Structured JSON:** [`93aa85bf52fc601a1d64.json`](../../sessions/93/93aa85bf52fc601a1d64.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

All results obtained. Here's the **plan_003 Scrambled-Label Ablation** summary:

## Results

| K | Scrambled F1 | Proper Treatment F1 (phase_b) | Baseline F1 (phase_b) |
|---|---|---|---|
| 1 | 0.9744 | (not tested) | (not tested) |
| 2 | 1.0000 | 0.9867 | 0.8788 |
| 3 | 1.0000 | 0.9867 | 0.9276 |
| 5 | 1.0000 | 1.0000 | 0.9577 |
| full | 1.0000 | 1.0000 | 0.9867 |

## Stage 1 DeBERTa comparison

| Metric | Scrambled | Proper |
|---|---|---|
| Val Persuasion Acc | 0.6437 | 0.7963 |
| Val Intent Acc | 0.9674 | 0.9514 |
| Best Val Loss | 1.0147 | 0.6164 |

## Conclusion

**Ablation FAILS** — scrambling strategy labels does NOT hurt end-to-end detection performance. The scrambled model matches or slightly exceeds the proper treatment at every K.

Key interpretation:
1. Strategy labels are correctly learned as noisy (0.64 vs 0.80 persuasion acc), confirming the scramble worked
2. But the binary intent signal (jailbreak vs benign) is strong enough to carry detection performance alone
3. The DeBERTa embeddings capture sufficient textual differences between jailbreak and benign conversations regardless of strategy label quality
4. For this dataset and test difficulty level, the persuasion strategy signal is **redundant** for detection

Note: The phase_b results used a slightly different test split (N=72 vs 73). The definitive comparison will come from plan_002's results on the identical `data/final_v2/test.jsonl`. The conclusion is unlikely to change given near-perfect performance from both.

Results saved to `results/plan_003_scrambled_eval.json`.

---
