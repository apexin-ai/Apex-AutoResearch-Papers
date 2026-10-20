# code alpha0 sft eval and queue

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_alpha0-sft-eval-and-queue_20260515T135630_result.json`
- **Structured JSON:** [`969105d3b2517ad06d31.json`](../../sessions/96/969105d3b2517ad06d31.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

α=2.0 SFT 已在跑（之前的 cron 提交），1014/1870 步（54%），~1.1 it/s，还剩约 13 分钟。不需要重复提交。

**当前进度汇总**：

| α | post-SFT accuracy | eos_rate | avg_len | 状态 |
|---|---|---|---|---|
| 0.0 | **64%** | 97% | 257.9 | eval 完成 ✓ |
| 1.0 | **57%** | 98% | 224.2 | eval 完成 ✓ |
| 2.0 | - | - | - | SFT 运行中 (54%) |
| 4.0 | 62% | - | - | 已完成 |

α=2.0 SFT 无需额外操作，预计 ~13 分钟完成。所有任务步骤已执行：
- eval α=0.0: 64% ✓
- eval α=1.0: 57% ✓  
- α=2.0 SFT: 已在跑，无需重复提交
- registry 已更新

---
