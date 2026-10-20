# ssh w1 rerun k11

**Death Avoidance as the Dominant Routing Signal: A Counterfactual Analysis on ScienceWorld** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_w1-rerun-k11_20260518T080439_result.json`
- **Structured JSON:** [`b602910a88b3d28cd8bc.json`](../../sessions/b6/b602910a88b3d28cd8bc.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。已有结果仅含 pairs cluster bootstrap，缺少 3 种方法，因此用正确数据源（K=11, 245 episodes）重跑了完整的 4 方法分析。

核心结论：**四种方法一致显著**，DAF 极其稳健。

| 方法 | p-value | 关键指标 |
|------|---------|---------|
| Wild Cluster Bootstrap (Webb 2023) | < 0.001 | CI [0.73, 1.00] |
| Exact Permutation Test | 0.002 | 4/2048 extreme |
| Cluster-Robust T-Test | 0.000002 | t=10.0, df=10 |
| Cohen's d | — | d=3.02 (极大) |

10/11 task types 的 per-cluster DAF=1.0，唯一 DAF=0 的是 find-non-living-thing。结果已写入服务器和本地 `artifacts/w1_cluster_bootstrap_k11.md`，JSON 已更新至 `guided_router/cluster_bootstrap_results.json`。

---
