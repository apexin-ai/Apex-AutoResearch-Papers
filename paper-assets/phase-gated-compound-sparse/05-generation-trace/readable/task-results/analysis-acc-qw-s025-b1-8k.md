# analysis acc qw s025 b1 8k

**Phase-Modulated Compound Sparsity Severity in 7B-Scale Mathematical Reasoning Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_acc_qw_s025_b1_8k_20260516T013121_result.json`
- **Structured JSON:** [`be3f783afb439ff24f67.json`](../../sessions/be/be3f783afb439ff24f67.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 已更新。摘要：

| 指标 | 8k (本次) | 2048 (旧 batch1) | 变化 |
|------|-----------|-------------------|------|
| **accuracy** | 0.32 (16/50) | 0.32 (16/50) | **无变化** |
| truncation_rate | 4% (2/50) | — | — |
| avg_tokens | 797.3 | — | — |

**结论：negative。** 将 max_new_tokens 从 2048 扩展到 8192 对 importance_s025 batch1 无收益——平均生成长度仅 797 tokens，只有 2 个问题触及 8192 上限，且这 2 个问题均答错。truncation 不是 2048 配置下的瓶颈。

---
