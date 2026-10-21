# code exp cross benchmark analysis

**What Can IRT Person-Fit Statistics Reveal About SFT-Stage Benchmark Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_exp-cross-benchmark-analysis_20260520T113150_result.json`
- **Structured JSON:** [`3287f41247e721eb9847.json`](../../sessions/32/3287f41247e721eb9847.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

实验完成。关键发现：

- **57/60 cells flagged** (95%)，10/12 模型在全部 5 个 benchmark 上被 flag
- **93.3% positive lz***（over-consistent），仅 4 个 cell 为 negative
- **Gemini-1.5 独立成簇**：GSM8K、HellaSwag、HumanEval 上 lz* 为负（aberrant pattern），与其余 11 个模型的 over-consistent 模式截然不同
- **Benchmark 敏感度**：MMLU (mean |lz*|=26.1) > HellaSwag (18.9) > GSM8K (7.9) > ARC-C (3.3) > HumanEval (2.9)
- **ARC-C/HellaSwag/GSM8K/HumanEval 高度相关** (Spearman ρ>0.6)，MMLU 与其余 benchmark 相关性较弱
- **Negative lz* 集中在** Gemini-1.5（3 cells）和 Doubao-pro（MMLU 1 cell）

产出已写入 `artifacts/cross_benchmark_analysis/`，7 个 artifact 全部注册，registry 状态 → DONE。

---
