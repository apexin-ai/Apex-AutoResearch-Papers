# analysis tier clustering

**Trace Verbosity Degrades SFT Verdict Prediction: A Case Study in Information Density Effects** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_tier_clustering_20260522T071852_result.json`
- **Structured JSON:** [`4485f1a1816afeb0566f.json`](../../sessions/44/4485f1a1816afeb0566f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部文件已生成。结果汇总：

---

### 1. 每个模型的最优 k

| 模型 | Gap statistic 最优 k | Silhouette (k=2) |
|------|---------------------|-------------------|
| **Qwen-7B** | **2** | 0.747 |
| **Qwen-1.5B** | **2** | 0.888 |
| **DeepSeek-6.7B** | **1** | 0.784 |
| **CodeLlama-13B** | **2** | 0.967 |
| **Pooled** | **2** | 0.800 |

DeepSeek gap statistic 选 k=1（数据分布较连续），但强制 k=2 时 silhouette 仍高达 0.78。其余 3 个模型和 pooled 分析均选 k=2。

### 2. k=2 cluster 分配 vs 论文

| 模型 | 匹配论文 Tier 划分？ | 差异 |
|------|---------------------|------|
| Qwen-7B | **完全匹配** | — |
| Qwen-1.5B | **完全匹配** | — |
| DeepSeek-6.7B | **不匹配** | vota (0.8445) 被聚到 Tier 2 而非论文的 Tier 1 |
| CodeLlama-13B | **完全匹配** | — |

### 3. CodeLlama loop_only 的归属

loop_only (0.7706) 和 no_trace (0.7650) 仅差 **0.56pp**，两者均被聚入 Tier 2。k=2 下它们不可分离——这实际上意味着 CodeLlama 上 loop_only trace 几乎没有比 no_trace baseline 提供更多信息。

### 4. 跨模型一致性

- **7/8 conditions 一致**：exception_only, ae_only, nomarker, loop_only, full_trace, label_only, no_trace 在所有出现的模型中聚类结果一致
- **vota 不一致**：3 个模型归 Tier 1，但 DeepSeek 归 Tier 2（0.8445 处于边界，距 Tier 1 中心 0.143，距 Tier 2 上边沿仅 0.032）

### 5. Pooled k=2 分界

Tier 1 (≥0.9563): exception_only, ae_only, vota (除 DeepSeek), nomarker
Tier 2 (≤0.8622): label_only, loop_only, full_trace, no_trace, DeepSeek:vota

**结论**：论文的 Two-Tier 划分在 3/4 模型上与 k-means 聚类完全吻合，pooled 分析也支持 k=2。唯一例外是 DeepSeek 的 vota (0.8445) 处于边界。建议论文中注明 vota 在 DeepSeek 上为 borderline case。

---
