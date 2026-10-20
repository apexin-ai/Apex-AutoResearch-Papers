# code sf1 cluster bootstrap v2

**Temporal Score Incomparability in LLM Benchmarks: A Large-Scale Psychometric Audit of 5,227 Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_sf1_cluster_bootstrap_v2_20260522T035327_result.json`
- **Structured JSON:** [`a832c347f0f39cb54eeb.json`](../../sessions/a8/a832c347f0f39cb54eeb.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。产出在 `artifacts/sf1_cluster_bootstrap/`：

**结果摘要**：

| | Cluster Bootstrap | Model Bootstrap |
|---|---|---|
| 95% CI | [26.73%, 53.17%] | [29.23%, 37.75%] |
| CI width | 26.44 pp | 8.52 pp |
| SD | 6.79% | 2.19% |

- **CI 宽度比**: 3.10× (cluster / model)
- 29 个 families (size ≥ 3), 1882 models
- Point estimate C% = 31.30%（与原始 5227 模型的 31.32% 一致）

**关键发现**：每个 family 100% 属于单一 cohort（无跨 cohort family），导致 cluster bootstrap 同时改变 ref/focal 比例，是 CI 大幅变宽的主因。即便如此，cluster CI 下界仍为 26.73%，C% 显著非零的结论稳健。

---
