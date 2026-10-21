# analysis cinelli hazlett sensitivity

**The Weakest Link Across Panel Sizes: Predictor Relevance Patterns in Multi-Judge LLM Evaluation under Adversarial Manipulation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_cinelli-hazlett-sensitivity_20260523T080322_result.json`
- **Structured JSON:** [`f9f0493968a3d6977a33.json`](../../sessions/f9/f9f0493968a3d6977a33.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。结果汇总：

**Cinelli & Hazlett (2020) Sensitivity Analysis — 36 conditions**

| K | RV > eta benchmarks | 含义 |
|---|---|---|
| K=3 | 1/12 | 大多数 condition 下 eta_max 的解释力已超过 RV，K_eff 系数对混淆较敏感 |
| K=5 | 3/12 | 随 K 增大，K_eff 系数更稳健 |
| K=7 | 4/12 | K_eff 系数的 robustness 继续提升 |
| **合计** | **8/36** | |

关键发现（以 K=3, mmlu×prompt_injection 为例）：
- RV = 0.419：未观测混淆需要同时解释 41.9% 的 K_eff 和 ASR 方差才能归零 β
- 但 eta_max 的 partial R² with treatment = 0.587（已超过 RV），说明一个 eta_max 量级的混淆就足以影响结论
- 总体趋势：更大的 K 值使 K_eff 系数更 robust

**产出文件**：
- JSON: `/root/cert_manip_resist_eval/artifacts/results/plan001/sensitivity_analysis.json`
- 图: `artifacts/figures/sensitivity_contour_K{3,5,7}.png`（4×3 subplot grid，黑色等高线=β=0，绿色菱形=eta_max benchmark）

---
