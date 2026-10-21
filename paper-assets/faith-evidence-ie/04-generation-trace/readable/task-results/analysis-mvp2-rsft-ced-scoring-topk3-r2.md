# analysis mvp2 rsft ced scoring topk3 r2

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_mvp2_rsft_ced_scoring_topk3_r2_20260515T132052_result.json`
- **Structured JSON:** [`026cede9049211edc5d2.json`](../../sessions/02/026cede9049211edc5d2.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## CED Scoring top_k=3 结果

**状态**: 成功完成 (EXIT_CODE=0)，耗时约 65 分钟 (20:13 → 21:18)

### top_k=3 vs top_k=1 对比

| 指标 | top_k=1 | top_k=3 | 变化 |
|------|---------|---------|------|
| 选择样本数 | 2,718 | **8,037** | +196% (2.96x) |
| 选择率 | 12.4% | **37.0%** | +24.6pp |
| 覆盖文档数 | — | 2,691/2,716 | 98.8% 覆盖 |
| mean_f1 (selected) | 0.6157 | **0.5761** | -0.040 |
| mean_ced (selected) | 0.6683 | **0.6205** | -0.048 |
| mean_combined (selected) | — | 0.6787 | — |

### 质量分布 (selected samples)

- **f1_reward**: mean=0.576, median=0.588, p25=0.444, p75=0.717
- **ced_reward**: mean=0.621, median=0.635, p25=0.487, p75=0.774
- **format_reward**: 100% = 1.0（全部格式合规）

### 过滤细节

- 总输入: 21,728 条（去重后，原始 43,936）
- f1 阈值(≥0.1) 过滤掉 1,299 条，25 个文档被完全移除
- 截断样本 1,924 条 (8.9%)，截断 vs 非截断 F1 差距 0.161 (显著)

### 输出文件

| 文件 | 大小 |
|------|------|
| `/root/autodl-tmp/rsft_filtered_topk3/rsft_train.jsonl` | 24.8 MB |
| `/root/autodl-tmp/rsft_filtered_topk3/rsft_scores.jsonl` | 67.6 MB |
| `/root/autodl-tmp/rsft_filtered_topk3/rsft_report.json` | 4.5 KB |

### 结论

top_k=3 如预期产生约 3 倍数据 (8037 vs 2718)，质量下降可控——F1 降 0.04，CED 降 0.048。这是一个典型的数据量-质量 tradeoff：更多样本但每个样本平均质量略低。数据可用于下一步 RSFT 训练，看更大数据量能否补偿单样本质量下降。

---
