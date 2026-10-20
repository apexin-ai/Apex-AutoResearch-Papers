# analysis acc qw b1 8k batch

**Phase-Modulated Compound Sparsity Severity in 7B-Scale Mathematical Reasoning Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_acc_qw_b1_8k_batch_20260516T010950_result.json`
- **Structured JSON:** [`bb6900a827b3430ccfa7.json`](../../sessions/bb/bb6900a827b3430ccfa7.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 已更新。两个实验的 status=DONE, conclusion=success, metrics 已写入。

## 对比表

| condition | old_b1 (2048) | new_b1 (8192) | b2 (8192) | old_n100 | new_n100 |
|-----------|---------------|---------------|-----------|----------|----------|
| dense     | 0.32 (16/50)  | **0.44 (22/50)** | 0.48 (24/50) | 0.40 | **0.46** |
| s020      | 0.26 (13/50)  | **0.26 (13/50)** | 0.46 (23/50) | 0.36 | **0.36** |

**关键发现：**
- Dense 从 8k tokens 中显著受益：batch1 +12pp (0.32→0.44)，combined n100 +6pp (0.40→0.46)
- S020 完全没有受益：batch1 结果与 2048 tokens 完全一致（仍为 13/50），combined 不变
- 两者 truncation 都极低（1/50），说明绝大多数问题不需要 8k tokens
- Dense 的改善来自模型在更宽裕 token 预算下的推理质量提升，而非避免截断

---
