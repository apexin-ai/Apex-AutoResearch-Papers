# code exp 006 v2

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_exp_006_v2_20260514T152631_result.json`
- **Structured JSON:** [`bc31945ffbe7edca1edf.json`](../../sessions/bc/bc31945ffbe7edca1edf.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

exp-006 v2 完成。

## 结果总结

**没有任何信号在任何任务上显著超过 greedy（p<0.05）。**

### NER SciERC (N=16, 551 instances)
| Signal | seed42 F1 | seed123 F1 | Δ greedy |
|--------|-----------|------------|----------|
| greedy | 0.618 | 0.618 | — |
| FK | 0.621 | 0.621 | ~+0.003 (ns) |
| logprob | 0.621 | 0.618 | ~+0.001 (ns) |
| SJ | 0.620 | 0.617 | ~+0.001 (ns) |
| EM | 0.606 | 0.613 | -0.005~-0.012 |
| voting_conf | 0.585 | 0.584 | **-0.033** |
| oracle | 0.787 | 0.785 | **+0.168** |

### NER CoNLL (N=8, 3453 instances)
所有信号都 **显著低于** greedy（p<0.001）。Oracle gap 仅 0.032，说明 N=8 sample 间差异小。

### RE SciERC (N=16, 397 instances)
| Signal | F1 | Δ greedy | p |
|--------|------|----------|-----|
| logprob | 0.410 | +0.007 | 0.27 |
| voting_conf | 0.408 | +0.005 | 0.34 |
| greedy | 0.403 | — | — |
| oracle | 0.631 | **+0.228** | 0.00 |

RE logprob-best 方向一致（+0.007）但在 v2 数据上不显著。Oracle gap 巨大（0.228），说明选择信号的 headroom 存在但当前信号无法利用。

### 输出
- 脚本：`code/exp_006_v2_selection.py`
- 结果：`output/exp_006_v2/exp_006_v2_results.json`
- Registry：exp_006_v2, DONE, conclusion=negative

---
