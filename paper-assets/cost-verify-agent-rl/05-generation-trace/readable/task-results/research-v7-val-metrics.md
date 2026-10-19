# research v7 val metrics

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_v7_val_metrics_20260519T184609_result.json`
- **Structured JSON:** [`da1522627df7bd900668.json`](../../sessions/da/da1522627df7bd900668.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## val_before_train 对比：v7 vs v9b

**v7 和 v9b 的 val_before_train 指标完全一致：**

| 指标 | v7 | v9b | 差异 |
|------|-----|------|------|
| success | 0.40625 | 0.40625 | 0 |
| action_is_valid | 0.9245 | 0.9245 | 0 |
| pass@1 | 0.40625 | 0.40625 | 0 |
| num_actions | 33.9375 | 33.9375 | 0 |
| response_length | 1465.0625 | 1465.0625 | 0 |
| action_is_effective | 0.999375 | 0.999375 | 0 |
| manager_invalid_action | 0.000625 | 0.000625 | 0 |

FSDP2 (v9b) 与原版 (v7) 在推理阶段数值完全一致，验证通过。

## v9b 训练进度

- **Training Progress: 0/30** — val_before_train 刚完成，训练刚开始（0%）
- GPU 内存（4x RTX PRO 6000 96GB）：

| GPU | 已用 | 总量 | 占比 |
|-----|------|------|------|
| 0 | 26.4 GB | 95.6 GB | 27% |
| 1 | 27.1 GB | 95.6 GB | 28% |
| 2 | 26.8 GB | 95.6 GB | 28% |
| 3 | 27.3 GB | 95.6 GB | 29% |

内存分布均匀，约 27-29%，FSDP2 分片正常。还有大量余量，backward 阶段内存增长应不会 OOM。

---
