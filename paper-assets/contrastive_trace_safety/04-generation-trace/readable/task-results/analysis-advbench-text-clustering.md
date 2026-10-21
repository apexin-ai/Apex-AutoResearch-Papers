# analysis advbench text clustering

**Layer Selection Sensitivity in Hidden-State Safety Probes for Reasoning Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_advbench_text_clustering_20260520T013745_result.json`
- **Structured JSON:** [`6346989a8bdf0091b1a8.json`](../../sessions/63/6346989a8bdf0091b1a8.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

分析完成。结果总结：

## AdvBench Text Embedding 聚类结果

### 聚类
| 方法 | Silhouette | 说明 |
|------|-----------|------|
| KMeans (k=3) | 0.0821 | 结构很弱，embedding 空间连续 |
| **HDBSCAN** | **0.2510** | 5 个 cluster + 309 noise (59.4%) |

HDBSCAN 优于 KMeans，但 59.4% noise 说明 text embedding 空间没有清晰的硬边界。HDBSCAN 识别出的 5 个 cluster 对应特定主题子群（金融犯罪、恶意软件、身份盗窃/黑客等）。

### ABC 分类统计
| 类型 | 数量 | 占比 |
|------|------|------|
| A: Refusal | 70 | 13.5% |
| B: Compliance | 387 | 74.4% |
| C: Educational | 63 | 12.1% |

### Jailbreak Yield
- **AdvBench: 86.5%** (B+C = 450/520)
- HarmThoughts: ~50% (209 traces)

AdvBench 的 jailbreak yield 显著高于 HarmThoughts（86.5% vs ~50%）。R1-8B 在 AdvBench 上几乎以 3:1 的比例 comply。

### t-SNE 观察
- 左图：HDBSCAN cluster 按主题聚集（金融犯罪、malware、暴力犯罪等）
- 右图：Refusal (A) 散布在整个空间中，不与特定主题强相关——拒绝行为更像随机触发而非主题驱动

### 注意事项
- ABC 分类基于关键词启发式，非人工标注。部分 C 类（含教育性 disclaimer 但仍提供实质内容的）可能被误判为 B
- 抽样验证显示分类大体合理：明确拒绝和明确配合都被正确识别

输出文件：
- `artifacts/advbench_preliminary/text_clustering_results.json`
- `artifacts/advbench_preliminary/tsne_clustering.png`

---
