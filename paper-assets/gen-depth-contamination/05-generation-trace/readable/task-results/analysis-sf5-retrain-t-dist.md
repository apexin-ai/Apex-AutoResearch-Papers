# analysis sf5 retrain t dist

**Generational Depth Estimation of Recursive Synthetic Text: Measuring the Discrimination Boundary** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_sf5_retrain_t_dist_20260520T042824_result.json`
- **Structured JSON:** [`37952892a383e9744691.json`](../../sessions/37/37952892a383e9744691.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

结果汇总：

### K\*=7 在 t-distribution CI 下仍然成立

两个模型的 6v7 pair 的 t-CI lower bound 均 > 0.60：

| Experiment | Pair | Mean | SE | Normal CI | t(df=4) CI | t_lower > 0.60 |
|---|---|---|---|---|---|---|
| **Pythia** | 6v7 | 0.6340 | 0.0037 | [0.6267, 0.6414] | [0.6237, 0.6444] | YES |
| **Qwen** | 6v7 | 0.6410 | 0.0019 | [0.6372, 0.6448] | [0.6357, 0.6464] | YES |

t-CI 确实比 normal-CI 更宽（t_crit=2.776 vs z_crit=1.96），但由于 fold 间方差很小（SE 仅 0.002~0.004），CI 的展宽不足以将 lower bound 拉到 0.60 以下。所有 pair（0v1 到 6v7）在 t-CI 下的 lower bound 均 > 0.60，K\*=7 判定不变。

结果已保存至：
- `/results/exp_pythia_retrain_depth7/pairwise_auc_t_dist.json`
- `/results/exp_qwen_retrain_chain_ext/pairwise_auc_t_dist.json`
- `/results/exp_008_retrain_chain/pairwise_auc_t_dist.json`

---
