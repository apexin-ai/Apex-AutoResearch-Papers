# experiment mvp p2a linear

**StructFuse: Structure-Grounded Hard Negative Mining for Contrastive Code Context Retrieval** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_experiment_mvp_p2a_linear_20260512T113250_result.json`
- **Structured JSON:** [`955298496e3d88627453.json`](../../sessions/95/955298496e3d88627453.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## Phase 2a 结果：PASS

| Model | Acc | Prec | Rec | F1 | AUC | MRR |
|---|---|---|---|---|---|---|
| Random | 0.505 | 0.010 | 0.333 | 0.019 | 0.410 | 0.034 |
| BM25-only LR | 0.297 | 0.020 | 1.000 | 0.039 | 0.476 | 0.115 |
| DataFlow-only LR | 0.981 | 0.333 | 0.333 | 0.333 | 0.691 | 0.393 |
| **DataFlow+BM25 LR** | **0.887** | **0.080** | **0.667** | **0.143** | **0.780** | **0.556** |

**Gold file 排名提升（最关键指标）：**

| Repo | BM25-only | DataFlow+BM25 |
|---|---|---|
| flask | 16/53 | **3/53** |
| requests | 4/27 | **1/27** |
| pytest | 31/132 | **3/132** |

**DataFlow+BM25 在所有指标上超过纯 BM25**：F1 +0.104, AUC +0.304, MRR +0.441。

**特征重要性**：`is_connected`（+2.82）是最强信号，`min_hop`（-1.81）和 `df_path_count`（+1.70）也有显著贡献。有趣的是 `log_bm25` 系数为负（-1.80），说明在这些 repo 中 BM25 相似性反而有误导性。

**注意**：仅 3 个 repo、3 个正样本，为方向性证据。pytest 的提升最大（31→3），说明 data-flow 在大 repo 中优势更明显。

---
