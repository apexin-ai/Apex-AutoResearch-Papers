# analysis plan017 14b ced scoring

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_plan017_14b_ced_scoring_20260520T191152_result.json`
- **Structured JSON:** [`9dac7ff54c7fcabbe30c.json`](../../sessions/9d/9dac7ff54c7fcabbe30c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

分析完成。汇总如下：

## plan017_14b_ced_scoring 结果

**基本信息**
- 输入: 24216 candidates, 3027 unique docs
- 输出: `/root/autodl-tmp/rsft_scored_14b/rsft_train.jsonl` (3015 条, 9.1MB)
- 运行时间: ~1h (GPU 0)

**Selected (top_k=1) 指标**

| 指标 | 14B | 4B (d112) | Δ |
|------|-----|-----------|---|
| selected_count | 3015 | 3014 | +1 |
| selection_rate | 12.45% | 12.4% | ~same |
| mean_f1 | **0.730** | 0.676 | **+5.4pp** |
| mean_ced | **0.690** | 0.676 | **+1.4pp** |
| mean_combined | 0.768 | — | — |

**数据质量**
- f1=0 样本: 0 条（阈值过滤生效）
- ced=0 样本: 0 条
- truncated 样本: 0 条（在 selected 中）
- format_reward: 全部 1.0
- f1 filter 丢弃 497 gens / 12 docs

**截断分析（全量）**
- truncated: 1701/24216 (7.0%), mean_f1=0.487
- non-truncated: 22515, mean_f1=0.625, gap=0.139 (显著)

**结论**: 14B 候选质量显著优于 4B，F1 提升 5.4pp，CED 提升 1.4pp，验证了 model scaling 假设。RSFT 训练数据已就绪，可进入下一步 RSFT training。

---
