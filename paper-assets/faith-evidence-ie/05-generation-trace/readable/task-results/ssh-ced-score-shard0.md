# ssh ced score shard0

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_ced-score-shard0_20260515T050122_result.json`
- **Structured JSON:** [`99071ab2608ec4912054.json`](../../sessions/99/99071ab2608ec4912054.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**Shard 0 CED scoring 完成。**

### 汇报

| 指标 | 值 |
|------|-----|
| 总 records | 5560 (695 docs) |
| 选中 | **687** (12.4%, 687/695 docs) |
| F1 阈值过滤丢弃 | 339 gens, 8 docs |

**分数统计 (selected)**:
| reward | mean | median | min | max |
|--------|------|--------|-----|-----|
| format | 1.000 | 1.000 | 1.0 | 1.0 |
| f1 | 0.618 | 0.636 | 0.103 | 1.0 |
| ced | 0.673 | 0.692 | 0.0 | 0.997 |
| combined | 0.716 | 0.717 | 0.4 | 0.999 |

**截断 vs 非截断 F1 对比**:
| 类型 | 数量 | mean F1 |
|------|------|---------|
| 截断 | 506 | 0.328 |
| 非截断 | 5054 | 0.496 |
| **gap** | — | **0.169** (显著) |

**输出文件**:
- `rsft_scores.jsonl`: 5560 条评分记录 (17.5MB)
- `rsft_train.jsonl`: **687** 条训练样本 (2.1MB)
- `rsft_report.json`: 完整统计报告

耗时 ~18 分钟 (13:01→13:19)。GPU 0 现已释放。

---
