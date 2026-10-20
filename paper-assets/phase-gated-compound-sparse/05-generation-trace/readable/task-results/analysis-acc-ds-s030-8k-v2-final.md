# analysis acc ds s030 8k v2 final

**Phase-Modulated Compound Sparsity Severity in 7B-Scale Mathematical Reasoning Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_acc_ds_s030_8k_v2_final_20260516T013133_result.json`
- **Structured JSON:** [`68e5b0b7107891bd2b8b.json`](../../sessions/68/68e5b0b7107891bd2b8b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

log_path 已在 registry 中存在，无需重复更新。Registry 更新完成（status 自动变为 DONE）。

## 产出摘要

**exp_id**: `acc_ds_s030_8k_v2` | **conclusion**: negative

| 指标 | 值 |
|------|-----|
| accuracy | 0.04 (2/50) |
| truncation_rate | 0.78 (39/50) |
| non_truncated_accuracy | 0.182 (2/11) |
| avg_tokens | 6566.3 |
| total_time | 7095.1s (~1.97h) |
| max_new_tokens | 8192 |

### ⚠ 与 Director Reviewer-verified 值的差异

JSON 实际 `gen_length=8192` 计数为 **39**（非 38），导致：
- truncation_rate = **0.78** (Director: 0.76)
- non_truncated_total = **11** (Director: 12)
- non_truncated_accuracy = **2/11 = 0.182** (Director: 2/12 = 0.167)

可能原因：Reviewer 手工计数时漏计了一个 truncated sample。Registry 已按 JSON 实际数据录入。

---
