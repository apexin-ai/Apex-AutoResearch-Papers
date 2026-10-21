# analysis r6 1a kappa diversity

**The Weakest Link Across Panel Sizes: Predictor Relevance Patterns in Multi-Judge LLM Evaluation under Adversarial Manipulation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_r6-1a-kappa-diversity_20260525T064751_result.json`
- **Structured JSON:** [`dc74424e474b5321dea0.json`](../../sessions/dc/dc74424e474b5321dea0.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

任务完成。结果总结：

**κ-diversity vs K_eff 替代回归分析（R6 Batch 1A）**

| K | κ-div FDR sig | K_eff FDR sig | Mean ρ |
|---|---|---|---|
| 3 | **8/12** | 3/12 | 0.989 |
| 5 | 7/12 | 7/12 | 0.987 |
| 7 | 6/12 | **8/12** | 0.986 |

**核心发现**：两个预测变量 rank correlation ρ > 0.985，但 FDR 显著性模式**完全相反**：
- κ-diversity: 8 → 7 → 6（随 K 增大而**减少**）
- K_eff: 3 → 7 → 8（随 K 增大而**增加**）

**Rebuttal 意义**：K_eff 不是 "dressed up" 的 κ-diversity。尽管两者高度相关，K_eff 的 MI-based 公式在更大面板规模下越来越有优势。predictor shift 模式（少→多显著条件）是 K_eff **独有的**——κ-diversity 呈相反趋势。这证明 K_eff 捕捉了超越 pairwise agreement 的信息论结构。

**产出文件**：
- 脚本：`/root/cert_manip_resist_eval/scripts/run_kappa_diversity_regression.py`
- 结果 JSON：`/root/cert_manip_resist_eval/artifacts/results/plan001/kappa_diversity_regression.json`
- 本地报告：`artifacts/kappa_diversity_regression_R6_1A.txt`

---
