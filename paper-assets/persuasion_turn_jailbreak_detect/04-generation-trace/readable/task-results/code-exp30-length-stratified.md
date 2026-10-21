# code exp30 length stratified

**DisPeD: A Controlled Study of Encoder Adaptation for Multi-Turn Jailbreak Detection** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_exp30-length-stratified_20260520T152057_result.json`
- **Structured JSON:** [`52b775a806f71d735e7c.json`](../../sessions/52/52b775a806f71d735e7c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

exp30 完成。

## 结果

**结构性发现**：benign 和 jailbreak 对话长度无重叠，导致每个 bin 都是 single-class，无法计算 per-bin macro F1。
- Benign: 12-20 turns (mean 15.8)
- DD jailbreak: 6-10 turns (mean 8.1)
- AA jailbreak: 3-8 turns (mean 5.1)

**9-class DAPT Jailbreak Recall by Turn Bin**：

| Dataset | 1-3 | 4-6 | 7-10 | 10+ (bn specificity) |
|---------|-----|-----|------|------|
| DD OOD | — | 100.0±0.0 (N=20) | 99.4±0.8 (N=60) | 100.0±0.0 (N=38) |
| AA OOD | 93.3±6.2 (N=20) | 95.6±4.5 (N=38) | 100.0±0.0 (N=22) | 100.0±0.0 (N=38) |

**对比 JB_MLM**：

| Dataset | 1-3 | 4-6 | 7-10 |
|---------|-----|-----|------|
| DD OOD | — | 100.0±0.0 | 83.9±22.8 |
| AA OOD | 90.0±7.1 | 92.1±9.4 | 69.7±33.7 |

**结论**：9-class DAPT 在所有 turn bins 均保持 ≥93% recall，无系统性退化。JB_MLM 在较长对话（7-10 turns）显示明显不稳定（std 高达 0.337）。Vanilla 在所有 bins 的 recall 接近 0（OOD 迁移完全失败）。

---
