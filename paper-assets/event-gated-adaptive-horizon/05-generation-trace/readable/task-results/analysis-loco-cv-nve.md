# analysis loco cv nve

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_loco_cv_nve_20260525T142550_result.json`
- **Structured JSON:** [`3ff096f48243b08abfd6.json`](../../sessions/3f/3ff096f48243b08abfd6.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。产出汇总：

**LOCO-CV 结果（K=12, n=56）**
- 10/12 折选择 θ≈1.5 为最优（均值 1.61±0.23）
- CV accuracy at θ=1.5: **53/56 = 94.6%**，与 in-sample 完全一致
- Train AUROC: 0.988 ± 0.003
- 3 个 FP 与全样本分析完全相同（frozen_dt_emb 瞬态 ×2 + mitigation 瞬态 ×1）
- 所有折 FN=0

**文件**
1. `artifacts/plan_034_nve_threshold/loco_cv_analysis.py` — 分析脚本
2. `artifacts/plan_034_nve_threshold/loco_cv_results.md` — 完整结果
3. `docs/paper/sections/appendix.tex` — 在 LOEO 节后新增 `\subsection{Leave-One-Config-Out Cross-Validation}`（§nve_loco）
4. Artifact 已注册（art_20260525_eed111）

---
