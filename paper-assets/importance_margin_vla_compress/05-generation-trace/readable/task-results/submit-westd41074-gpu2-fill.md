# submit westd41074 gpu2 fill

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_submit_westd41074_gpu2_fill_20260525T001207_result.json`
- **Structured JSON:** [`c4f1070348100b8f581a.json`](../../sessions/c4/c4f1070348100b8f581a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两个优先级实验都已完成：
- `pi05_l2norm_k0.85_libero_10_seed43` → **78.6%**（500 eps，完整）
- `pi05_l2norm_k0.30_libero_10_seed42` → **36.6%**（500 eps，完整）

**GPU2 当前空闲，但任务列表中的两个实验都已有结果。**

汇报：
| 实验 | 状态 | 结果 |
|------|------|------|
| eval_pi05_l2norm_k085_long_seed43 | ✅ 已完成 | 78.6%（seed42=78.4%，跨seed稳定） |
| eval_pi05_l2norm_k03_long_seed42 | ✅ 已完成 | 36.6% |

GPU2 空闲可用。需要你指定下一个要提交的实验。

---
