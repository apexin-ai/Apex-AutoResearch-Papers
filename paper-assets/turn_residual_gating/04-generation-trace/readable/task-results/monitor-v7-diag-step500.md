# monitor v7 diag step500

**Exposure Bias Collapses Auxiliary Attention Losses in Multi-Turn Dialogue** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_monitor_v7_diag_step500_20260518T185120_result.json`
- **Structured JSON:** [`379771ed78b14e2f79c1.json`](../../sessions/37/379771ed78b14e2f79c1.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

等 ~4.5 分钟让训练到 micro-step ~800 出 [GATE] step=100 行。

先整理目前已有的关键发现：

**重大发现：日志 "Step" 是 micro-step，不是 global_step**
- `grad_accum=8`，所以 `global_step = micro_step / 8`
- 日志 "Step 500" = micro-step 500 = **global_step ≈ 62**
- Director 以为 global_step ~300，实际只有 ~87（当前 micro-step ~700）
- 到 global_step 500 还需 ~80 分钟

**L_GAR 最近出现积极变化：**

| micro-step | global_step | L_GAR | mean_GAR (推算) |
|---|---|---|---|
| 0 | 0 | 0.2342 | 0.016 |
| 50-550 | 6-68 | ~0.23 | ~0.02 |
| 600 | 75 | 0.2179 | 0.033 |
| 650 | 81 | 0.2106 | 0.041 |
| 700 | 87 | 0.1886 | **0.066** |

micro-step 700 时 mean_GAR ≈ 0.066，已超过 0.05 阈值。

---
