# diagnose bf16 ds imp s010

**Phase-Modulated Compound Sparsity Severity in 7B-Scale Mathematical Reasoning Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_bf16_ds_imp_s010_20260514T093214_result.json`
- **Structured JSON:** [`0a9ddabe089f84b2343a.json`](../../sessions/0a/0a9ddabe089f84b2343a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Cron jobs not found (likely already cleaned up or from a different session). Both experiments are fully diagnosed and registry updated.

## 结果汇总

| 实验 | Verdict | Conclusion | 关键指标 |
|------|---------|------------|---------|
| **bf16_ds_imp_s010** (s=0.10) | **FAIL** | negative | II median 接近 0（high=+0.003, low=+0.015, mid=+0.006），mean 为负值，s=0.10 太低无法产生有意义的 importance 差异 |
| **bf16_ds_imp_s035** (s=0.35) | **PASS** | success | II median 显著正值（high=+0.11, low=+28.76, mid=+4.95），low_sparsity vs mid_sparsity CI 不重叠，支持 C2 单调递增 claim |

两个实验均已处理 50/50 problems，结果文件已保存，registry 已更新为 DONE。

---
