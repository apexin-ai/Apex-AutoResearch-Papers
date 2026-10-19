# analysis dataflow reposize confound

**StructFuse: Structure-Grounded Hard Negative Mining for Contrastive Code Context Retrieval** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_dataflow_reposize_confound_20260514T203328_result.json`
- **Structured JSON:** [`5eced147df334c879e52.json`](../../sessions/5e/5eced147df334c879e52.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

产出已全部写入 `/root/autodl-tmp/structfuse/artifacts/confound_analysis/`，三个文件都已生成。

---

## 关键发现

### 1. 交叉分布：rich-dataflow 确实集中在大 repo
| dataflow \ repo_size | small | medium | large | xlarge | total |
|---|---|---|---|---|---|
| sparse | 99 | 559 | 1485 | 956 | 3099 |
| moderate | 31 | 180 | 273 | 56 | 540 |
| **rich** | **0** | **5** | **318** | **362** | **685** |

- Rich-dataflow 的 **99.3%** 落在 large/xlarge repo（对比 moderate 的 60.9%）
- Rich-dataflow 在 small repo 中完全不存在

### 2. 控制 repo_size 后，反直觉模式**没有消失**

在 dataflow_aware 策略下，**每个** repo_size bin 内 rich < moderate 都成立：

| repo_size | rich R@1 | moderate R@1 |
|---|---|---|
| medium | 0.091 (n=99) | 0.331 (n=326) |
| large | 0.108 (n=1049) | 0.128 (n=444) |
| xlarge | 0.091 (n=871) | 0.108 (n=65) |

### 3. 真正的 confound 是 pool_size，不（仅）是 repo_size

- Pearson r(dataflow_edges, repo_size) = 0.089（弱）
- 但 rich instances 的平均 candidate pool 远大于 moderate（46-50 vs 17-37）
- 在 mock 模型中，R@1 ≈ 1 - exp(-5/pool)，pool_size 才是直接驱动 R@1 差异的因素
- Partial correlation (dataflow → R@1 | repo_size) 几乎没有被控制掉：raw = -0.064，partial = -0.061

### 结论

repo_size 和 dataflow_richness 有强分布偏斜（rich 几乎只在大 repo），但**控制 repo_size 不能消除反直觉模式**。在 dry-run mock 数据中，pool_size 是更直接的 confound——rich-dataflow 文件的候选池更大，导致随机/mock rank 天然更高。真实模型实验需要额外控制 pool_size 来确认 dataflow richness 的独立效应。

---
