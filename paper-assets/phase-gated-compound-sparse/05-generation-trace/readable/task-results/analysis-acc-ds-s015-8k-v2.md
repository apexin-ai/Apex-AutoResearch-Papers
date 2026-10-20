# analysis acc ds s015 8k v2

**Phase-Modulated Compound Sparsity Severity in 7B-Scale Mathematical Reasoning Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_acc_ds_s015_8k_v2_20260516T002941_result.json`
- **Structured JSON:** [`9e678eaf2a103e701d9d.json`](../../sessions/9e/9e678eaf2a103e701d9d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

结果：

| 指标 | s015 (本次) | dense | s020 | s025 |
|------|------------|-------|------|------|
| accuracy | **0.48** | 0.74 | 0.30 | 0.08 |
| truncation_rate | **0.32** | 0.16 | 0.58 | 0.76 |
| avg_tokens | **3750.5** | — | — | — |

关键发现：
- **truncated_count=16**（32%），全部产生 null 预测
- 额外 1 个 null 预测来自非截断问题（algebra/2584, gen_length=5290，答案提取失败）
- heads_pruned=112 在所有问题上一致
- s015 的截断率是 dense 的 2 倍，但远好于 s020/s025，accuracy 也处于 dense 和 s020 之间的合理位置

产出已写入 `artifacts/acc_ds_s015_8k_v2_analysis.json` 并注册（`art_20260516_9f8bf8`）。

---
