# eval exp15c status check

**DisPeD: A Controlled Study of Encoder Adaptation for Multi-Turn Jailbreak Detection** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_exp15c-status-check_20260519T122132_result.json`
- **Structured JSON:** [`584177978c69b6ffbcc9.json`](../../sessions/58/584177978c69b6ffbcc9.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 已更新至 DONE (negative)。

## exp15c_roberta_large_mlm 结果

**结论：negative** — 假设被否定。

| 指标 | MLM (exp15c) | Vanilla (exp15) | 9class (exp15) |
|------|:-----------:|:---------------:|:--------------:|
| **DD OOD Full** | 0.884 | 0.927 | **0.987** |
| DD OOD K=1 | 0.876 | 0.878 | 0.965 |
| DD OOD K=3 | 0.902 | 0.915 | 0.960 |
| **AA Full** | 0.874 | **1.000** | 0.946 |
| AA K=1 | 0.876 | 0.977 | 0.718 |
| AA K=3 | 0.881 | 0.990 | 0.881 |

**关键发现：** MLM-only DAPT 在 AA 和 DD OOD 上都是三者最差。AA Full: MLM 0.874 < 9class 0.946 < vanilla 1.000。这排除了"classification fine-tuning 导致退化"的假设。是 continued pretraining 本身的表征偏移与 frozen-encoder GRU 评估框架冲突，而非 classification head 的干扰。

---
