# code negative difficulty analysis

**StructFuse: Structure-Grounded Hard Negative Mining for Contrastive Code Context Retrieval** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_negative_difficulty_analysis_20260513T184724_result.json`
- **Structured JSON:** [`e64b8e9d309c9400f5c2.json`](../../sessions/e6/e64b8e9d309c9400f5c2.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

分析完成。关键发现：

## 结果摘要

| 策略 | Qwen mean sim | StarCoder mean sim | Delta |
|------|------|------|------|
| Random | 0.899 | 0.553 | -0.346 |
| Embedding Distance | 0.960 | 0.668 | -0.292 |
| Dataflow-Aware | 0.950 | 0.659 | -0.291 |

## 关键发现

**1. StarCoder pretrained embeddings 天然分辨力远强于 Qwen。** StarCoder 的 query-negative cosine similarity 整体低 0.29-0.35，说明 StarCoder pretrained 表征本身就能更好地区分 query 和 negative。

**2. Dataflow negatives 并非对 StarCoder "更容易"——恰恰相反。** 
- StarCoder: dataflow mean=0.659 vs random mean=0.553（dataflow 比 random **更难**区分，+0.106）
- Qwen: dataflow mean=0.950 vs random mean=0.899（同趋势，+0.051）

Dataflow negatives 在两个模型上都比 random 更难（更高 similarity），但这个差距在 StarCoder 上更大。

**3. 为什么 dataflow 对 StarCoder 没用的解释：** 不是因为 dataflow negatives 太简单。所有策略的负样本在 StarCoder 上都已经有较低的 cosine similarity（0.55-0.67），StarCoder pretrained 的表征空间本身就把不相关代码分得很开。**训练信号的边际收益小**——不管用什么策略，StarCoder 已经 "懂" 了。

**产出文件（服务器 bjb1-42106）：**
- 统计数据：`/root/autodl-tmp/structfuse/artifacts/negative_difficulty_stats.json`
- 图表：`negative_difficulty_{qwen,starcoder,comparison}.{pdf,png}`
- 脚本：`/root/structfuse/analysis/negative_difficulty.py`

---
