# analysis appendix v2 rerun

**The Weakest Link Across Panel Sizes: Predictor Relevance Patterns in Multi-Judge LLM Evaluation under Adversarial Manipulation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_appendix-v2-rerun_20260523T191113_result.json`
- **Structured JSON:** [`03f2938e497d75bb497e.json`](../../sessions/03/03f2938e497d75bb497e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

All three analyses complete. Here's the full comparison:

---

## V2 Correction 对比报告

### 1. Cross-benchmark IV

| 指标 | V1 | V2 | 变化 |
|------|----|----|------|
| ρ(K_eff) K3/K5/K7 | 0.784/0.762/0.763 | 0.785/0.762/0.763 | 无实质变化 |
| Cross η vs within η | 同 | 同 | 不变 |
| Reduced-form keff sig | 34/36 | **35/36** | K7 arc→mmlu 从 5/6 升至 6/6 |
| 2SLS F-stats | 820/4508/9232 | 820/4508/9232 | 不变 |
| Bootstrap K3 FDR sig | 4/6 sig | 4/6 sig | 不变 |
| 结论 | exclusion restriction violated | 同 | **结论不变** |

个别系数微调：K3 `arc_keff_on_mmlu_authority_bias` β 从 0.231→0.181（仍显著 p=2.3e-4）。

### 2. Cinelli-Hazlett Sensitivity (Pool A)

| 指标 | V1 | V2 |
|------|----|----|
| K3 RV > η | 3/12 | 2/12 |
| K5 RV > η | 6/12 | **10/12** |
| Total | 9/24 | **12/24** |
| 结论 | K_eff 对部分条件 robust | **K5 robustness 明显增强**，结论强化 |

### 3. K_eff Stability Split

| 稳定性 | V1 K3/K5 | V2 K3/K5 |
|--------|----------|----------|
| Stable (8 conditions) | 0/8, 4/8 | **4/8**, **6/8** |
| Moderate (2) | 1/2, 2/2 | 0/2, 2/2 |
| Unstable (2) | 0/2, 1/2 | 0/2, **2/2** |
| 结论 | 稳定性偏弱 | **稳定性显著增强**，结论强化 |

### 总结

V2 修正（过滤 API error samples）对三个 Appendix 分析的影响：
- **Cross-benchmark IV**：几乎无变化，所有关键结论保持不变
- **Sensitivity Analysis**：K5 robustness 从 6/12 升至 10/12，结论强化
- **K_eff Stability Split**：stable 条件下 sig 比例大幅提升，结论强化

**无需修改论文结论方向**。V2 修正消除了 error→tie 的噪声，使统计信号更清晰。

---
