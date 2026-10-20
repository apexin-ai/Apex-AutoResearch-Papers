# verify tau 06 nmin value

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_verify_tau_06_nmin_value_20260516T020422_result.json`
- **Structured JSON:** [`a92c44bb0bc810cde843.json`](../../sessions/a9/a92c44bb0bc810cde843.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

所有实验的训练日志都明确记录了参数值。

## 结论

| 实验 | n_min | 依据 |
|------|-------|------|
| tau_05_seed42 | **2** | 日志记录 `n_min: 2` |
| tau_06_seed42 | **2** | 日志记录 `n_min: 2` |
| tau_07_seed42 | **2** | 日志记录 `n_min: 2` |
| tau_09_seed42 | **2** | 日志记录 `n_min: 2` |
| tau_095_seed42 | **2** | 日志记录 `n_min: 2` |

**全部实验使用的是 n_min=2，不是 3。** 判断依据：每个实验的训练日志开头都打印了完整的超参数配置，其中明确显示 `n_min: 2`。Reviewer 的质疑不成立。

---
