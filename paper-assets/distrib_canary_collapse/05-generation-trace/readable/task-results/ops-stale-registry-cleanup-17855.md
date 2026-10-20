# ops stale registry cleanup 17855

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_stale_registry_cleanup_17855_20260520T085329_result.json`
- **Structured JSON:** [`a29f16fc1945e67b1bae.json`](../../sessions/a2/a29f16fc1945e67b1bae.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

All data collected. Here's the summary:

---

## 结果汇报

### 1. interv_pred_14b_s42_fp32 (PID 191999)
- **进程**: DEAD
- **结果**: **完整** — gen_0 到 gen_10 全部完成，all_metrics.json 存在，EXIT_CODE=0
- **Registry**: 已经是 `DONE/success`，无需更新

### 2. interv_pred_a075_s42_fp32 (PID unknown)
- **进程**: DEAD，无存活进程
- **结果**: **失败** — 仅完成 gen_0，EXIT_CODE=1（`CUDA error: device-side assert triggered`）
- **Registry**: 以 `interv_pred_a075_s42` 名称存在，已标记 `DONE/killed`，无需更新

### 3. alpha_sweep_a005_s42 (PID unknown)
- **进程**: DEAD，无存活进程
- **结果**: **失败** — 仅完成 gen_0 + gen_1，EXIT_CODE=1（`Eigenvalues did not converge`）
- **Registry**: 此 ID 不存在。已被 `alpha_sweep_a005_s42_v3`（DONE/success）取代，无需更新

### 4. alpha_sweep_a060_s42_fp32 (PID unknown)
- **进程**: DEAD，无存活进程
- **结果**: **失败** — 仅完成 gen_0 + gen_1，EXIT_CODE=1（`Eigenvalues did not converge`）
- **Registry**: 此 ID 不存在。已被 v3（DONE/success）和 v4（**当前 RUNNING，PID 295535 存活中**）取代，无需更新

---

**结论**: 4 个实验均非 stale RUNNING — 要么已标记 DONE，要么从未注册（被后续版本取代）。Registry 无需清理操作。

---
