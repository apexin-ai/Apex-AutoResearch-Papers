# analysis bootstrap significance

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_bootstrap-significance_20260516T081641_result.json`
- **Structured JSON:** [`12d8d500c277e653f3f8.json`](../../sessions/12/12d8d500c277e653f3f8.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。核心结论：

**ρ=0.4 (3-seed bootstrap, p<0.001)**:
- Adaptive (n_min=3) vs Uniform: **-0.055 PPL, 显著**
- Adaptive_fix (n_min=2) vs Uniform: **-0.043 PPL, 显著**
- Grid-best vs Uniform: **-0.051 PPL, 显著**
- Adaptive vs Grid-best: -0.004 PPL, **不显著** (p=0.30)
- ESS-only vs Uniform: **+0.029 PPL, 显著更差**

Cohen's d 极大（>10）是 N=3 的数学必然——3个观测值方向完全一致时 SD 极小，d 被放大。报告中已注明 N=3 限制。

**ρ=0.6**: 单 seed，仅有 point estimates，方向与 ρ=0.4 一致。

报告已注册为 `art_20260516_d1d9e7`。

---
