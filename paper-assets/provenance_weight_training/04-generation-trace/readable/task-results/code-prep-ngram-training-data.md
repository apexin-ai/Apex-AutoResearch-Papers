# code prep ngram training data

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_prep_ngram_training_data_20260518T140852_result.json`
- **Structured JSON:** [`43790395a596e28a43d2.json`](../../sessions/43/43790395a596e28a43d2.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。

### 产出报告

**输出文件**
- `/root/provenance_weight_training/data/scored_data_ngram_qscore.jsonl`
- `/root/autodl-tmp/provenance_weight_training/data/scored_data_ngram_qscore.jsonl`
- 行数：371,499（与源文件一致）

**转换方法**: percentile-based，`q_score = 1 - percentile_rank(ngram_ppl)`（scipy rankdata，ties 用 average）

**ngram_ppl 原始分布**
| 统计量 | 值 |
|---|---|
| min | 1.6474 |
| max | 614,383.5008 |
| mean | 1,586.5525 |
| median | 740.3377 |

**q_score 分布**
| 统计量 | 值 |
|---|---|
| min | 0.0000 |
| max | 1.0000 |
| mean | 0.5000 |
| median | 0.5000 |

**Real vs Synthetic 对比**
| 类别 | n | mean q_score | mean ngram_ppl |
|---|---|---|---|
| Synthetic (depth=1) | 206,610 | **0.6026** | 1,642.77 |
| Real (depth=0) | 164,889 | **0.3714** | 1,516.11 |

Synthetic 的 q_score 高于 Real（0.6026 > 0.3714），符合预期：synthetic 文本 ngram_ppl 更低 → 反转后 q_score 更高 → pretrain_weighted.py 会给更大的降权。`q_score` 字段已覆盖原有值，`ngram_ppl` 字段保留。

---
