# analysis seed42 adaptive diagnostic

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_seed42_adaptive_diagnostic_20260514T131507_result.json`
- **Structured JSON:** [`6a9b4e989889ae2f0e53.json`](../../sessions/6a/6a9b4e989889ae2f0e53.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 诊断结论

**adaptive_seed42 非 bug，而是信噪比问题。** weighting 机制工作正常（3 个 seed 的 b*/ESS/alpha_eff 统计完全一致）。

### 根因：三个结构性因素叠加

1. **n_min=3 + batch_size=4 过于保守** — 84.5% 的 micro-batch ESS 被钳制在 [3.0, 3.1]，weighting 强度远弱于 grid_b0.5（ESS=2.87，不受 n_min 约束）。这直接解释了为什么 grid_b0.5_seed42 有效而 adaptive_seed42 无效。

2. **per-batch b* 纯噪声** — b* 自相关≈0，intra-step CV=0.51。同一 optimizer step 内 4 个 micro-batch 的 weighting 策略完全不同，等价于向梯度注入额外噪声。Grid 的 CV=0（完美一致）。

3. **改善信号极弱（0.04 ppl, 0.23%）+ 仅 3 个 seed** — seed42 偏离均值仅 1.4σ，统计上不显著。seed42 的 late-phase loss 停滞而 seed123 仍在下降，说明 data ordering 导致了不同优化轨迹。

### 最优先修复

**降低 n_min 到 2**（甚至去掉约束）— 成本最低，直接释放 adaptive 的 weighting 力度，使其接近 grid_b0.5 的有效强度。

报告和图表已保存到 artifacts。

---
