# gpu exp 002 merge and pilot

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_gpu_exp_002_merge_and_pilot_20260514T122323_result.json`
- **Structured JSON:** [`e5fe2754052155df9dfc.json`](../../sessions/e5/e5fe2754052155df9dfc.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

exp-002 全部完成。总结：

**exp-002: CoNLL-2003 Cross-Dataset Validation — SUCCESS**

| Signal | ρ (full) | AUROC |
|--------|----------|-------|
| **SJ** | **0.436** | **0.801** |
| FK | 0.400 | 0.774 |
| LogProb | 0.316 | 0.753 |
| EM | 0.451 | 0.816 |
| EV | 0.424 | 0.789 |

- **SJ vs LogProb: Δρ=+0.12, 95% CI [+0.088, +0.154], bootstrap显著** → Claim 1 validated
- EM略胜SJ（Δρ=+0.015），但两者都是structural signal，互不矛盾
- F1: greedy=0.912, voting=0.914, oracle=0.954
- Registry 已更新为 DONE/success，artifact 已注册

---
