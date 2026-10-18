# analysis api only power betastd

**The Weakest Link Across Panel Sizes: Predictor Relevance Patterns in Multi-Judge LLM Evaluation under Adversarial Manipulation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_api-only-power-betastd_20260524T190307_result.json`
- **Structured JSON:** [`567c96b7667302c4f592.json`](../../sessions/56/567c96b7667302c4f592.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

结果保存在 `/root/cert_manip_resist_eval/artifacts/results/plan001/api_only_power_betastd.json`。

**核心发现：power_issue，不是 effect_shrinkage。**

| 指标 | K=3 | K=5 |
|------|-----|-----|
| Full pool β_std(K_eff) | 0.349 | 0.437 |
| API-only β_std(K_eff) | 0.634 | 0.796 |
| Ratio (api/full) | 1.82 | 1.82 |
| Full pool OLS sig | 11/12 | 12/12 |
| API-only OLS sig | 11/12 | 10/12 |
| MDE@80% (WCB) | 0.897 | 不可达 |
| Power@β=0.5 (WCB) | 42% | 8.5% |

API-only β_std(K_eff) 反而比 full pool 更大（ratio ~1.82），说明 K_eff 效应在 API-only 子集中更强。OLS 下 11-12/12 条件显著。非显著性完全来自 WCB 的保守性——K=3 仅 7 clusters/position，K=5 仅 5 clusters/position，WCB 需要 β_std > 0.9 才能达到 80% power（K=3），K=5 即使 β_std=1.0 也只有 30% power。

---
