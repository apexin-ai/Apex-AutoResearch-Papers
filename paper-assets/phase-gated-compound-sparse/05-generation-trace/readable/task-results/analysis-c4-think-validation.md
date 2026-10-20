# analysis c4 think validation

**Phase-Modulated Compound Sparsity Severity in 7B-Scale Mathematical Reasoning Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_c4_think_validation_20260516T023355_result.json`
- **Structured JSON:** [`a226f0494f8368d844c9.json`](../../sessions/a2/a226f0494f8368d844c9.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

验证完成。结果摘要：

**核心指标** — 目标 κ ≥ 0.80 已达成:
- **Adaptive κ = 0.8804**（per-problem 均值 0.8466，中位数 0.8782）
- **Per-problem AUC-ROC = 0.9808**（中位数 0.9854），表明 sparsity 排序几乎完美区分 thinking/execution tokens
- 75% 的 problems κ ≥ 0.80，100% κ ≥ 0.60
- Token-level accuracy = 94.2%

**物理图像**: `&lt;think>` 阶段 sparsity 显著更低（0.656 vs 0.763，Cohen's d = -0.80），因为推理时注意力更密集。PACS "execution" phase（低 sparsity）对应 DeepSeek 的 thinking phase — 命名不同但现象一致。

**固定阈值 κ = 0.52** 较低，原因是 think fraction 跨 problem 变异大（0.46 ± 0.21），单一全局阈值无法适配。PACS 使用 per-sequence 自适应分位数，因此 adaptive κ 是正确的比较基准。

分析脚本在 `scripts/think_phase_kappa_v3.py`，数据在 `artifacts/think_phase_kappa_v3.json`，报告已注册为 `art_20260516_ea194d`。

---
