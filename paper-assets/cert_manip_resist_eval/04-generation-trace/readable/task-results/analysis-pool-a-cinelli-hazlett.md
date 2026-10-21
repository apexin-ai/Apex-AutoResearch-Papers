# analysis pool a cinelli hazlett

**The Weakest Link Across Panel Sizes: Predictor Relevance Patterns in Multi-Judge LLM Evaluation under Adversarial Manipulation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_pool-a-cinelli-hazlett_20260523T120953_result.json`
- **Structured JSON:** [`2389a6a7c3724dac33a0.json`](../../sessions/23/2389a6a7c3724dac33a0.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。结果汇总：

### rv_exceeds_eta 计数

| Pool | K=3 | K=5 | K=7 | Total |
|------|-----|-----|-----|-------|
| **Full (15 models)** | 1/12 | 3/12 | 4/12 | 8/36 |
| **Pool A (9 models)** | 3/12 | 6/12 | — | 9/24 |

Pool A 比例 (37.5%) 显著高于 Full Pool (22.2%)。

### K=3 对比

Pool A 的 RV 普遍低于 Full Pool（因为 84 vs 455 panels，dof 减少导致 RV 下降），但 **eta benchmark 也同步下降更多**，因此 rv_exceeds 反而从 1/12 升到 3/12。exceeds 的三个 ARC conditions 是 authority_bias、prompt_injection、verbosity_bias。

### K=5 对比

Pool A K=5 是最突出的改善：6/12 exceeds vs Full Pool 3/12。ARC 侧 5/6 conditions 的 RV 均超过 eta benchmark，且 RV 绝对值普遍比 Full Pool 更高（如 verbosity_bias +0.30, score_manipulation +0.18）。这说明在低 collinearity 的 capability-matched pool 中，K_eff 的 robustness 确实更强。

### 关键发现
- Pool A 中 r(K_eff, η_max)=0.50 vs Full Pool 的 0.82，collinearity 大幅下降
- 低 collinearity → eta benchmark (eta_partial_r2_treatment) 变小 → RV 更容易超过 benchmark
- K=5 的 ARC 侧效果尤其显著，几乎全部 exceeds

产出文件：
- 服务器：`/root/cert_manip_resist_eval/artifacts/results/plan001/sensitivity_analysis_poolA.json`
- 本地：`docs/paper/data/sensitivity_analysis_poolA.json`

---
