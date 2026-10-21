# exp mf1a rerun n1000

**Multi-Class Annotation Errors in Causal Inference: Topology-Dependent Bias, Sensitivity, and Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_exp_mf1a_rerun_n1000_20260523T175940_result.json`
- **Structured JSON:** [`734e9a8aaf2229d23a73.json`](../../sessions/73/734e9a8aaf2229d23a73.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

N=1000 重跑完成（135.8s）。核心数字对比：

| 指标 | N=100 | N=1000 | 变化 |
|------|-------|--------|------|
| total_curves | 54,611 | 545,945 | ×10 |
| non_monotone_fraction | 11.93% | 11.94% | 稳定 |
| max_eps_abs | 0.01637 | 0.01637 | 不变 |
| median_eps_abs | 0.0 | 0.0 | 不变 |
| mean_eps_abs | 0.000474 | — | — |
| p95_eps_abs | 0.00253 | — | — |
| p99_eps_abs | 0.00825 | — | — |
| safe_topo_max_eps | 0.01637 | 0.01637 | 不变 |
| fragile_topo_max_eps | 0.01318 | 0.01318 | 不变 |
| weak_iv_filtered | 2,089 | 21,055 | ×10 |

结论：10 倍采样量下所有关键指标高度稳定，max ε bound 未被突破，non-monotone fraction 收敛于 ~11.9%，bound 可信度得到增强。

---
