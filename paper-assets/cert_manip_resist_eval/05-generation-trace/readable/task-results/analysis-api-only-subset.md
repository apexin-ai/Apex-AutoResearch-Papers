# analysis api only subset

**The Weakest Link Across Panel Sizes: Predictor Relevance Patterns in Multi-Judge LLM Evaluation under Adversarial Manipulation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_api-only-subset_20260523T070411_result.json`
- **Structured JSON:** [`453f92e65fd6d4bbc620.json`](../../sessions/45/453f92e65fd6d4bbc620.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。结果摘要：

**API-Only K=3** (84 panels, 9 API models):
| 方法 | η_max FDR sig | K_eff FDR sig |
|------|--------------|--------------|
| OLS | 9/12 | 3/12 |
| Clustered SE | 8/12 | 2/12 |

**API-Only K=5** (126 panels):
| 方法 | η_max FDR sig | K_eff FDR sig |
|------|--------------|--------------|
| OLS | 8/12 | 6/12 |
| Clustered SE | 8/12 | 3/12 |

**对比 Full 15-model**:
- Full K=3 bootstrap: η_max 5/12, K_eff 1/12
- Full K=5 bootstrap: η_max 0/12, K_eff 7/12

**结论**: K=3 η_max dominant pattern 在 API-only 中保持且更强（8/12 vs full 5/12）。但 K=5 的 transition（K_eff 取代 η_max 成为主导）**未能复现** — API-only K=5 仍然 η_max dominant（8/12 vs K_eff 3/12）。

这暗示 K=5 transition 可能部分受 local model confounding 驱动，或者 9 个 API 模型的 K_eff 变异度不够（只有 9 clusters/position，clustered SE 也较保守）。OLS 层面 K=5 K_eff 已达 6/12，但 clustered SE 校正后降到 3/12。

输出保存在 `/root/cert_manip_resist_eval/artifacts/results/plan001/api_only_regression.json`。

---
