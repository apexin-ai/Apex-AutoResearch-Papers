# analysis cohens d bf16

**Phase-Modulated Compound Sparsity Severity in 7B-Scale Mathematical Reasoning Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_cohens-d-bf16_20260514T075854_result.json`
- **Structured JSON:** [`c301afd2eae30522d202.json`](../../sessions/c3/c301afd2eae30522d202.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

计算完成。结果与之前声称的 0.60→1.12 **不符**：

| Sparsity | Cohen's d | 95% CI | Effect Size |
|----------|-----------|--------|-------------|
| s015 (15%) | **0.44** | [0.35, 0.78] | small |
| s020 (20%) | **0.52** | [0.43, 0.90] | medium |
| s025 (25%) | **0.68** | [0.56, 0.86] | medium |
| s030 (30%) | **0.80** | [0.67, 1.02] | large |

实际范围是 **0.44→0.80**（不是 0.60→1.12）。趋势方向一致——sparsity 越高 effect size 越大——但数值明显低于之前的 claim。s015 仅为 small effect，s030 刚达到 large effect 边界。

结果已保存到 `/root/autodl-tmp/pacs/analysis_output/cohens_d_bf16.json`。每个 sparsity level 49 个有效 problem（1 个因 null 跳过）。

---
