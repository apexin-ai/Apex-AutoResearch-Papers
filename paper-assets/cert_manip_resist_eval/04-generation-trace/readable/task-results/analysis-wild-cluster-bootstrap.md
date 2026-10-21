# analysis wild cluster bootstrap

**The Weakest Link Across Panel Sizes: Predictor Relevance Patterns in Multi-Judge LLM Evaluation under Adversarial Manipulation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_wild-cluster-bootstrap_20260522T194342_result.json`
- **Structured JSON:** [`edcafc662319da6ac990.json`](../../sessions/ed/edcafc662319da6ac990.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

B=9999 完成。结果：

| Method | η\_max FDR sig | K\_eff FDR sig |
|---|---|---|
| Canonical OLS | 11/12 | 8/12 |
| Clustered SE | 8/12 | 0/12 |
| Mixed Effects | 7/12 | 3/12 |
| **Wild Bootstrap** | **10/12** | **9/12** |

K\_eff 在 wild cluster bootstrap 下 **9/12 显著**（全部正向），比 OLS 的 8/12 还多 1 个。3 个不显著的 condition：
- `mmluxverbosity_bias` (p=0.1465)
- `mmluxauthority_bias` (p=0.1375)  
- `arc_challengexsycophancy` (p=0.0593, 接近边缘)

η\_max 10/12 显著，2 个不显著：`arc_challengexscore_manipulation`、`arc_challengexauthority_bias`。

核心发现：wild cluster bootstrap（13 clusters, Rademacher weights）确认 K\_eff 效应是 robust 的——clustered SE 给出 0/12 是过度保守（15 clusters 远低于渐近理论要求的 ≥30），bootstrap 在小 cluster 数下给出更可靠的推断。

输出已保存到 `/root/cert_manip_resist_eval/artifacts/results/plan001/wild_cluster_bootstrap.json`。

---
