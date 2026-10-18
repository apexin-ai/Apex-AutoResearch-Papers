# ssh d051 status check

**How Does Schema Complexity Predict Performance in Training-Free LLM Information Extraction?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_d051-status-check_20260517T033813_result.json`
- **Structured JSON:** [`47907e62ca8e698821b1.json`](../../sessions/47/47907e62ca8e698821b1.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

所有数据收集完毕。汇总如下：

## D051 Count Curves 实验状态

### FewRel（RE，7 levels: 4/8/16/32/40/64/80）

| Dataset × Seed | Status | Levels |
|---|---|---|
| **FewRel seed=42** | **complete** | 7/7 |
| **FewRel seed=123** | **complete** | 7/7 |
| **FewRel seed=456** | **complete** | 7/7 |

### Few-NERD（NER，6 levels: 2/6/12/22/44/66）

| Dataset × Seed | Status | Levels |
|---|---|---|
| **Few-NERD seed=42** | **complete** | 6/6 |
| **Few-NERD seed=123** | **complete** | 6/6 |
| **Few-NERD seed=456** | **running** | 2/6（完成 count_12, count_2；缺 count_6, count_22, count_44, count_66） |

---

### 当前运行进程

```
python3 scripts/run_d051_count_curves_25.py --dataset fewnerd --n_batches 25 --seed 456
```
在 tmux session `d051_batch2` 中运行，从 10:47 开始（已运行约 1 小时）。

---

### 完成结果明细

**FewRel seed=42** (accuracy):
| count | mean | std |
|---|---|---|
| 4 | 0.8700 | 0.0680 |
| 8 | 0.8050 | 0.0816 |
| 16 | 0.7188 | 0.0629 |
| 32 | 0.6518 | 0.0490 |
| 40 | 0.6058 | 0.0417 |
| 64 | 0.5393 | 0.0262 |
| 80 | 0.5041 | 0.0002 |

**FewRel seed=123** (accuracy):
| count | mean | std |
|---|---|---|
| 4 | 0.8475 | 0.1072 |
| 8 | 0.7988 | 0.0778 |
| 16 | 0.7454 | 0.0599 |
| 32 | 0.6379 | 0.0436 |
| 40 | 0.6092 | 0.0446 |
| 64 | 0.5357 | 0.0222 |
| 80 | 0.4958 | 0.0000 |

**FewRel seed=456** (accuracy):
| count | mean | std |
|---|---|---|
| 4 | 0.8508 | 0.0871 |
| 8 | 0.7858 | 0.0863 |
| 16 | 0.6915 | 0.0649 |
| 32 | 0.6549 | 0.0458 |
| 40 | 0.6091 | 0.0400 |
| 64 | 0.5352 | 0.0249 |
| 80 | 0.4865 | 0.0000 |

**Few-NERD seed=42** (recall):
| count | mean | std |
|---|---|---|
| 2 | 0.5267 | 0.1905 |
| 6 | 0.3899 | 0.1153 |
| 12 | 0.3057 | 0.1017 |
| 22 | 0.2684 | 0.1029 |
| 44 | 0.3007 | 0.1116 |
| 66 | 0.4071 | 0.0017 |

**Few-NERD seed=123** (recall):
| count | mean | std |
|---|---|---|
| 2 | 0.4460 | 0.1984 |
| 6 | 0.4217 | 0.1341 |
| 12 | 0.3568 | 0.1119 |
| 22 | 0.2768 | 0.0905 |
| 44 | 0.2724 | 0.1146 |
| 66 | 0.4067 | 0.0014 |

**Few-NERD seed=456** (recall, partial):
| count | mean | std |
|---|---|---|
| 2 | — | — |
| 6 | — | — |
| 12 | ✓ (file exists) | — |
| 22 | — | — |
| 44 | — | — |
| 66 | — | — |

注意：seed=456 目前只有 `results_count_12.jsonl`（13MB）和 `results_count_2.jsonl`（7MB），无 summary。脚本按 count 降序（或字母序）处理中，正在计算剩余 4 个 levels。按已完成 seeds 的用时估算，剩余约 2-3 小时完成。

---
