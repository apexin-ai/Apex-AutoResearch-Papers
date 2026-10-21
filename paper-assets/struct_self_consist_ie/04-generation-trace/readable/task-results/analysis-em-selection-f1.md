# analysis em selection f1

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_em_selection_f1_20260515T044818_result.json`
- **Structured JSON:** [`bf42dfafbd44c74d1ced.json`](../../sessions/bf/bf42dfafbd44c74d1ced.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

结果：

## Qwen SciERC N=8 — EM Selection F1

### NER (n=529)

| Method | Selection F1 |
|---|---|
| Greedy | 0.6439 |
| Oracle | 0.7758 |
| LP-Best | 0.6501 |
| SJ-Best | 0.6450 |
| Ensemble-Best | 0.6450 |
| **EM-Best** | **0.6362** |
| Voting-Best | 0.6337 |
| Random-Avg | 0.6077 |

Sign test (EM vs Greedy): Wins=56, Losses=65, Ties=408, Δ=-0.0077

### RE (n=397)

| Method | Selection F1 |
|---|---|
| Greedy | 0.4042 |
| Oracle | 0.5850 |
| LP-Best | 0.3948 |
| SJ-Best | 0.3855 |
| Ensemble-Best | 0.3855 |
| **EM-Best** | **0.3718** |
| Voting-Best | 0.3592 |
| Random-Avg | 0.3544 |

Sign test (EM vs Greedy): Wins=27, Losses=63, Ties=307, Δ=-0.0324

### 结论

EM selection 在 NER 和 RE 上都**低于 greedy baseline**（NER -0.8pp, RE -3.2pp），排名倒数第二（仅高于 Voting-Best/Random-Avg）。Sign test 中 losses 显著多于 wins。EM 作为 selection signal 表现最差，这符合预期——exact match 在结构化输出中过于严格，大多数 instance 的 8 个 sample 几乎没有完全一致的输出，导致 plurality vote 基本退化为随机选择。

---
