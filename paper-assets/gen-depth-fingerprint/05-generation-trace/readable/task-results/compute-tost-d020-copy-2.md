# compute tost d020

**Depth Profiling: Classifying Recursive Generation Depth in Base-Model LLM Text** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_compute_tost-d020_20260518T123940_result.json`
- **Structured JSON:** [`417fe4fb29eefca8d9a6.json`](../../sessions/41/417fe4fb29eefca8d9a6.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

没有 d=0.10 备份，说明脚本上次可能就已经改成 0.20 了。当前结果已经是 d=0.20 的 TOST 检验，无需重跑。

**d=0.20 TOST 等价性检验结果：**

| Feature | Group | d_obs | p_TOST | Equivalent? |
|---|---|---|---|---|
| entropy_mean | drifting | +1.0544 | 1.0 | NOT |
| entropy_std | intermediate | +0.4571 | 1.0 | NOT |
| entropy_max | near-stationary | +0.0622 | 7.97e-26 | **EQUIV** |
| entropy_min | intermediate | -0.0157 | 3.39e-60 | **EQUIV** |
| tail_decay | near-stationary | +0.0873 | 6.67e-18 | **EQUIV** |
| ttr | drifting | +0.8142 | 1.0 | NOT |
| hapax_ratio | drifting | +0.7346 | 1.0 | NOT |

- **等价 (3/7):** entropy_max, entropy_min, tail_decay（observed |d| < 0.10，远在 0.20 bound 内）
- **不等价 (4/7):** entropy_mean, entropy_std, ttr, hapax_ratio（observed |d| 从 0.46 到 1.05，远超 bound）

即使放宽到 d=0.20，drifting 组和 entropy_std 的效应量太大，TOST 仍拒绝等价。

---
