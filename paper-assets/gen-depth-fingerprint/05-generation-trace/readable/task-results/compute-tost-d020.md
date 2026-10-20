# compute tost d020

**Depth Profiling: Classifying Recursive Generation Depth in Base-Model LLM Text** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_compute_tost-d020_20260518T123736_result.json`
- **Structured JSON:** [`9ea56083302f41afce6c.json`](../../sessions/9e/9ea56083302f41afce6c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 结果

### TOST 等价性检验摘要 (|d| < 0.20, α = 0.05)

| Feature | Group | Cohen's d | p_TOST | 等价? |
|---|---|---|---|---|
| entropy_mean | drifting | +1.0544 | 1.00 | NOT |
| entropy_std | intermediate | +0.4571 | 1.00 | NOT |
| **entropy_max** | near-stationary | +0.0622 | 7.97e-26 | **EQUIV** |
| **entropy_min** | intermediate | -0.0157 | 3.39e-60 | **EQUIV** |
| **tail_decay** | near-stationary | +0.0873 | 6.67e-18 | **EQUIV** |
| ttr | drifting | +0.8142 | 1.00 | NOT |
| hapax_ratio | drifting | +0.7346 | 1.00 | NOT |

**样本量:** gen-1 = 7,896; gen-2+ = 21,199

**关键发现:**
- 3/7 特征通过等价性检验 (entropy_max, entropy_min, tail_decay)，均为 near-stationary 或 intermediate 组，observed |d| < 0.09
- 4/7 特征拒绝等价 (entropy_mean, entropy_std, ttr, hapax_ratio)，均为 drifting 或 intermediate 组，observed |d| 在 0.46~1.05 之间，远超 0.20 阈值
- 与论文中 "drifting vs near-stationary" 分类高度一致：drifting 特征确实在代际间有大效应量差异，near-stationary 特征统计等价

**JSON 已保存:** `/root/gen-depth-fingerprint/results/tost_equivalence.json`

**tmux:** 已清理，无残留 session。

---
