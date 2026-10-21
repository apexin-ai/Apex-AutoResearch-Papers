# ops 19828 scan

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_19828-scan_20260523T022524_result.json`
- **Structured JSON:** [`77504829f0ec815b6beb.json`](../../sessions/77/77504829f0ec815b6beb.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两个实验状态汇总：

| 实验 | PID | GPU | 进度 | 目标 |
|------|-----|-----|------|------|
| **scale_14b_t15_a075_s42_fp32** | 793171 | cuda:0 (98%, 30.9G) | gen_0–gen_12 完成，正在跑 gen_13 | 需 gen_0–gen_14 |
| **scale_14b_t10_a050_s43_fp32** | 822048 | cuda:1 (98%, 27.7G) | gen_0–gen_5 完成，正在跑 gen_6 | 需 gen_0–gen_9 |

两个 PID 都 **ALIVE**，GPU 利用率 98%。

- t15_a075: **13/15 gen 完成**，还差 gen_13 + gen_14
- t10_a050_s43: **6/10 gen 完成**，还差 gen_6–gen_9

---
