# diag wave1 progress check

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diag_wave1-progress-check_20260517T080506_result.json`
- **Structured JSON:** [`48e8aacca51730a7f034.json`](../../sessions/48/48e8aacca51730a7f034.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

| 实验 | 进度 | 状态 |
|------|------|------|
| **plan018-additive-random-b01-s45** | 435/500 (87%) | 训练中，prove_rate 波动 0.5-1.0 |
| **sweep-random-b005-s42** | 499/500 (99.8%) | 即将完成，还差 1 step |

**GPU 状态：**
- GPU 0: 90% util, 85493 MiB
- GPU 1: 90% util, 84583 MiB

两卡都在满负荷运行。sweep-random-b005-s42 马上结束（step 499/500），plan018-additive-random-b01-s45 预计还需约 13 分钟完成（按每 step ~20s 估算，剩余 65 步）。

---
