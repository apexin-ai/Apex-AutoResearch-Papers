# analysis nve threshold v2

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_nve_threshold_v2_20260525T201901_result.json`
- **Structured JSON:** [`db2e46c1f26581acbfab.json`](../../sessions/db/db2e46c1f26581acbfab.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

分析完成。报告已写入 `artifacts/plan_034_nve_threshold/analysis_v2.md` 并注册为 `art_20260525_828490`。

核心结论:

**Method A (step-matched NVE)** 仍是最佳分类器 (AUROC=0.989)。θ=1.5× 维持 100% recall，4 个 FP 均可解释 (frozen transient + eval-variance)。θ=2.0× 维持 100% precision (FP=0)。

**组合诊断标准** 在有轨迹数据的子集上能消除部分 FP (如 exp_082 被正确排除)，但 74% 实验缺少轨迹数据导致大量 A_only 回退，整体 F1 反而下降。建议作为二次确认而非独立分类器。

**Method B (raw ve_ratio_peak)** AUROC=0.970，在 θ=1.3× 达到 100% precision / F1=0.966 (N=35 子集)。不受 baseline 选择偏差影响，适合作为补充验证。

**Reviewer 关注点**: exp_084 NVE=0.37、exp_085 NVE=0.31，两种方法下均为 true negative。Reviewer 声称的 2.25/3.0 与 registry 数据不符，可能使用了不同的归一化方法。θ=2.0× 的 precision 仍为 100%。

---
