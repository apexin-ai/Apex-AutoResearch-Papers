# analysis nve step filter

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_nve_step_filter_20260525T211812_result.json`
- **Structured JSON:** [`ed110f5c11bd827aaae2.json`](../../sessions/ed/ed110f5c11bd827aaae2.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Section 8 已添加到 analysis_v2.md 并注册。

**核心结果**:

- Step filter (≥50K) 仅影响 **1 个实验**: exp_088 NVE_peak 1.82 → 0.55，消除该早期瞬态 FP
- 其余 5 个有 nve_traj 的实验 peak 均在 step ≥ 50K，无变化
- 57 个无 trajectory 数据的实验保留原始 NVE_peak

**θ=1.5× 验证目标**:
- F1 = **0.926 > 0.92** ✓
- FP = **4 > 3** ✗ (差 1，残余 FP 均为非早期 spike 类型，3 个无 trajectory 数据无法进一步过滤)
- AUROC = 0.9895 (+0.0032)

---
