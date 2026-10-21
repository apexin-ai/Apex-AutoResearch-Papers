# ssh ced score shard2

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_ced-score-shard2_20260515T044141_result.json`
- **Structured JSON:** [`b154e72d5f16ea3dd3e9.json`](../../sessions/b1/b154e72d5f16ea3dd3e9.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

shard_2 CED scoring 完成，耗时约 28 分钟。结果汇总：

### 关键统计
| 指标 | 值 |
|------|-----|
| 总 records | 5568 (696 unique docs) |
| f1 过滤丢弃 | 349 generations, 7 docs 完全丢弃 |
| 筛选后 | 689 samples (689/696 docs), 选择率 12.4% |

### 评分分布 (top_1 selected)
| 维度 | mean | median | range |
|------|------|--------|-------|
| format_reward | 1.000 | 1.000 | [0, 1] |
| f1_reward | 0.472 | 0.483 | [0, 1] |
| ced_reward | 0.501 | 0.521 | [0, 0.997] |
| combined_score | 0.589 | 0.601 | [0, 0.999] |

### 截断 vs 非截断 F1 对比
| 类别 | 数量 | mean F1 |
|------|------|---------|
| 截断 | 492 | 0.330 |
| 非截断 | 5076 | 0.486 |
| **gap** | — | **0.156** |

### 产出文件
- `rsft_scores.jsonl` — 全量评分 (17MB)
- `rsft_train.jsonl` — 训练数据 (2.1MB, 689 行)
- `rsft_report.json` — 统计报告

无错误或异常。cuda:2 已释放。

---
