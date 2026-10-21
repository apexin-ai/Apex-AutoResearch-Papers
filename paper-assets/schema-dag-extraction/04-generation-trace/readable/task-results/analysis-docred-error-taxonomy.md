# analysis docred error taxonomy

**How Does Schema Complexity Predict Performance in Training-Free LLM Information Extraction?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_docred_error_taxonomy_20260519T173228_result.json`
- **Structured JSON:** [`ee8e6f775faccc1e2e14.json`](../../sessions/ee/ee8e6f775faccc1e2e14.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

分析完成。结果已保存到 `/root/schema-dag-extraction/analysis/docred_error_taxonomy.json`。

## DocRED Error Taxonomy 结果

### 按 BCS Bin 的错误分布

| Bin | BCS均值 | N批次 | 样本数 | Accuracy | IntraSub率 | Missed率 | IntraSub占错误比 |
|-----|---------|-------|--------|----------|-----------|---------|----------------|
| very_low | 0.385 | 15 | 1137 | 67.2% | 4.8% | 28.1% | 14.5% |
| low | 0.440 | 17 | 2497 | 57.7% | 13.5% | 28.8% | 31.9% |
| medium | 0.549 | 48 | 5721 | 55.1% | 22.4% | 22.6% | 49.8% |
| high | 0.678 | 19 | 2663 | 41.3% | 37.0% | 21.6% | 63.1% |
| very_high | 0.743 | 11 | 847 | 41.9% | 41.9% | 16.2% | 72.2% |

### Spearman 相关性（110 batches, 55 count_16 + 55 count_32）

| 指标 | ρ | p |
|------|---|---|
| **IntraSub率 vs BCS** | **0.843** | 8.1e-31 *** |
| IntraSub占错误比 vs BCS | 0.828 | 6.5e-29 *** |
| ExtraSub率 vs BCS | N/A (恒=0) | — |
| Missed率 vs BCS | -0.589 | 1.3e-11 *** |
| Accuracy vs BCS | -0.741 | 2.3e-20 *** |

Per config_key: count_16 ρ=0.847, count_32 ρ=0.800。

### 跨任务对比

| 任务 | IntraSub ρ(BCS) |
|------|-----------------|
| FewRel (sentence RE) | 0.954 |
| Few-NERD (NER) | 1.000 |
| **DocRED (document RE)** | **0.843** |

### 关键发现

- **IntraSub 与 BCS 强正相关复现成功**，ρ=0.843 (p<1e-30)
- ExtraSub 恒为 0 — DocRED 实验也是 forced-choice，模型从不预测 batch 外类型
- IntraSub 占总错误的比例从低 BCS 的 14.5% 单调递增到高 BCS 的 72.2%
- ρ 略低于 FewRel/Few-NERD，符合预期：document-level RE 有更长上下文带来的额外噪声源

---
