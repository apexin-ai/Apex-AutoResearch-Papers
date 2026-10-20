# code dense n100 then ds8k

**Phase-Modulated Compound Sparsity Severity in 7B-Scale Mathematical Reasoning Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_dense_n100_then_ds8k_20260515T215355_result.json`
- **Structured JSON:** [`b420f6fc4e30e67b3610.json`](../../sessions/b4/b420f6fc4e30e67b3610.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。汇总：

### QW Dense n=100 结果（Priority 1）

| Batch | Correct | Total | Acc |
|-------|---------|-------|-----|
| batch1 (1-50) | 16 | 50 | 32% |
| batch2 (51-100) | 24 | 50 | 48% |
| **Combined** | **40** | **100** | **40%** |

batch2 显著高于 batch1（48% vs 32%），可能有题目难度分布差异。

### GPU 状态

| GPU | 任务 | 状态 |
|-----|------|------|
| GPU 0 | 其他任务 | 78% util |
| GPU 1 | 其他任务 | 69% util |
| GPU 2 | **acc_ds_s020_8k_v2** | 刚提交 (PID 280638) |
| GPU 3 | acc_qw_s030_n100 | 仍在运行 (72% util)，s030 输出文件尚未生成 |

DS s025 8k 需等 GPU 3 上的 s030_n100 完成后再提交，后续 Worker 处理。

---
