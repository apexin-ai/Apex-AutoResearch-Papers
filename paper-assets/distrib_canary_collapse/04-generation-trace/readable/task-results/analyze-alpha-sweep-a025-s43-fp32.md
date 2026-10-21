# analyze alpha sweep a025 s43 fp32

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analyze_alpha_sweep_a025_s43_fp32_20260519T150138_result.json`
- **Structured JSON:** [`663e67cef0425246daf7.json`](../../sessions/66/663e67cef0425246daf7.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 分析完成

### alpha_sweep_a025_s43_fp32 结果

| Lead-lag 指标 | 值 |
|---|---|
| PermG_fwd | **0/8** |
| PermG_rev | 0/8 |
| K≥4 | **0/8** |
| MMCT | **0** |
| d1_drift | **-38.95%** |

### 3-Seed α=0.25 一致性

| | s42 | s43 | s44 | mean | σ |
|---|---|---|---|---|---|
| PermG | 0/8 | 0/8 | 0/8 | 0/8 | — |
| K≥4 | 0/8 | 0/8 | 0/8 | 0/8 | — |
| MMCT | 0 | 0 | 0 | 0 | — |
| d1_drift | -39.15% | -38.95% | -38.35% | **-38.82%** | **0.34%** |

### 统计结论

**α=0.25 确认在 blind zone 内。** 3/3 seed 一致 PermG=0/8、K≥4=0/8，d1_drift 方差极小（σ=0.34%），seed stability 完全通过。模型坍缩仍在发生（d1 下降~39%），但 canary → downstream 的 lead-lag 信号不可检测。

Registry 已更新：status=DONE, conclusion=success。

---
