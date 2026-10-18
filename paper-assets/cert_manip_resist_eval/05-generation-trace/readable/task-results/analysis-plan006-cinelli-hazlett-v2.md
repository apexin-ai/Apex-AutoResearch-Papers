# analysis plan006 cinelli hazlett v2

**The Weakest Link Across Panel Sizes: Predictor Relevance Patterns in Multi-Judge LLM Evaluation under Adversarial Manipulation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_plan006-cinelli-hazlett-v2_20260524T100043_result.json`
- **Structured JSON:** [`b8d6582907af99b5d17f.json`](../../sessions/b8/b8d6582907af99b5d17f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

结果已保存。汇总如下：

## V2 Cinelli-Hazlett Robustness Value 结果

| 指标 | V1 | V2 | 变化 |
|------|----|----|------|
| RV 范围 | 0.20–0.42 | 0.005–0.59 | 显著拓宽 |
| RV > η benchmark 总计 | 8/36 (22%) | **11/36 (31%)** | +3 |
| K=3 | 1/12 | **4/12** | +3 |
| K=5 | 3/12 | 3/12 | 不变 |
| K=7 | 4/12 | 4/12 | 不变 |

**主要变化在 K=3**，新增 3 个 exceeds 条件（ARC×prompt_injection, ARC×sycophancy, MMLU×authority_bias）。K=5/K=7 使用的 `k5_k7_panel_analysis.json` 本身已经是 V2 数据，所以结果没变。

**对论文的影响**：
- 原论文声称 "78% of conditions (28/36) RV ≤ η benchmark" → V2 变为 **69% (25/36)**
- 整体叙事方向不变（多数条件下 K_eff 不够 robust），但数字需要更新
- RV 范围从 0.20–0.42 改为 **0.005–0.59**（更大的离散度）

结果文件：`/root/cert_manip_resist_eval/artifacts/results/plan001/cinelli_hazlett_v2.json`

---
