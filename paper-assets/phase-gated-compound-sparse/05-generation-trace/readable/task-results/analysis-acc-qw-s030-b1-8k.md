# analysis acc qw s030 b1 8k

**Phase-Modulated Compound Sparsity Severity in 7B-Scale Mathematical Reasoning Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_acc_qw_s030_b1_8k_20260516T013129_result.json`
- **Structured JSON:** [`cfc4a8d437dfef264031.json`](../../sessions/cf/cfc4a8d437dfef264031.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 已更新。摘要：

## acc_qw_s030_b1_8k 结果

| 指标 | 8k (本次) | 2048 (旧 batch1) | 变化 |
|------|-----------|-------------------|------|
| **accuracy** | 0.14 (7/50) | 0.14 (7/50) | **无变化** |
| truncation_rate | 0.04 (2/50) | — | — |
| avg_tokens | 863.3 | — | — |

**结论: negative** — 将 max_new_tokens 从 2048 提升到 8192 未带来任何 accuracy 提升，batch1 仍为 7/50。仅 2 个问题触发了 8k 截断（4%），说明绝大多数问题在 2048 以内就已完成生成，token 预算不是 batch1 低准确率的瓶颈。

---
