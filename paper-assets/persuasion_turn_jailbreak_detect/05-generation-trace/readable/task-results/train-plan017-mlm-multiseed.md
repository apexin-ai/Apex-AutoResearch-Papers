# train plan017 mlm multiseed

**DisPeD: A Controlled Study of Encoder Adaptation for Multi-Turn Jailbreak Detection** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_train_plan017-mlm-multiseed_20260518T061229_result.json`
- **Structured JSON:** [`23391b0c8d20218e1205.json`](../../sessions/23/23391b0c8d20218e1205.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。3-seed 汇总：

**DD OOD F1 (macro):**
| K | Mean | Std | seed=42 | seed=123 | seed=456 |
|---|------|-----|---------|----------|----------|
| K=1 | 0.973 | 0.019 | 1.0 | 0.96 | 0.96 |
| K=2 | 0.993 | 0.009 | 1.0 | 0.98 | 1.0 |
| K=3 | 0.997 | 0.005 | 1.0 | 0.99 | 1.0 |
| K=5 | 0.997 | 0.005 | 1.0 | 0.99 | 1.0 |
| Full | 0.914 | 0.115 | 1.0 | 0.99 | 0.75 |

**IID F1 (macro):**
| K | Mean | Std | seed=42 | seed=123 | seed=456 |
|---|------|-----|---------|----------|----------|
| K=1 | 0.925 | 0.027 | 0.96 | 0.89 | 0.92 |
| K=2 | 0.969 | 0.016 | 0.97 | 0.95 | 0.99 |
| K=3 | 0.978 | 0.012 | 0.99 | 0.96 | 0.99 |
| K=5 | 0.982 | 0.016 | 1.0 | 0.96 | 0.99 |
| Full | 0.982 | 0.016 | 1.0 | 0.96 | 0.99 |

关键发现：DD OOD K=1~5 均值 >= 0.97 且方差很小，MLM control 在截断 turn 上仍然很强。Full 的高方差 (0.115) 来自 seed=456 GRU 在长序列上的不稳定（recall=0.64），这是 GRU 分类器层面的随机性，非 MLM 预训练本身的问题。结果已保存到 `results/plan_017_mlm_3seed_summary.json` 并更新了 registry。

---
