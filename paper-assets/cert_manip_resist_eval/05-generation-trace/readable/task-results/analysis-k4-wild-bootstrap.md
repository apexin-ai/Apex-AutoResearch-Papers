# analysis k4 wild bootstrap

**The Weakest Link Across Panel Sizes: Predictor Relevance Patterns in Multi-Judge LLM Evaluation under Adversarial Manipulation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_k4-wild-bootstrap_20260523T063715_result.json`
- **Structured JSON:** [`2e2f642f6d85f6dd9edf.json`](../../sessions/2e/2e2f642f6d85f6dd9edf.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。

## K=4 Wild Cluster Bootstrap 结果

**Summary**: K_eff FDR sig: **2/12**, η_max FDR sig: **1/12**

K_eff 显著的 2 个 condition（均为正方向）：
- `mmlu×prompt_injection` (std_β=+0.408, fdr_p=0.014)
- `arc_challenge×position_bias` (std_β=+0.841, fdr_p=0.014)

η_max 显著的 1 个 condition：
- `mmlu×position_bias` (std_β=+0.560, fdr_p=0.019)

**Validation**: arc×sycophancy K_eff β = -0.068（负方向，与 K=3 的 -0.192 一致）

## Cross-K Comparison 更新

| K | Bootstrap η_max | Bootstrap K_eff |
|---|---|---|
| K=3 | **5/12** | 1/12 |
| K=4 | **1/12** | **2/12** |
| K=5 | 0/12 | **7/12** |
| K=7 | 0/12 | **5/12** |

K=4 确认了 transition 位置：η_max 从 K=3 的 5/12 骤降到 K=4 的 1/12，K_eff 从 1/12 升到 2/12。dominance crossover 发生在 K=3→K=4 之间，K=4 已经是 η_max 不再主导的状态，但 K_eff 尚未获得强显著性（要到 K=5 才出现 7/12 的集中爆发）。

---
