# check rsft diversity

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_rsft-diversity_20260515T010435_result.json`
- **Structured JSON:** [`10d5a8b468e9a083b252.json`](../../sessions/10/10d5a8b468e9a083b252.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 结果

### 整体统计
| 指标 | 值 |
|------|-----|
| 总文档数 | 208 |
| 总生成数 | 1664 (每文档恰好 8 个) |
| **平均 unique ratio** | **0.985** |
| 中位数 unique ratio | 1.000 |
| 100% unique 的文档 | 196/208 (94.2%) |
| 低多样性 (<50% unique) | 仅 2/208 |

### 采样细节
- AirAsia Zest: 8 gen → 5 unique (前 200 字符截断比较；完整输出大概率更不同)
- Niklas Bergqvist: 8 gen → 4 unique (同上)
- Pacific Fair: 8 gen → 7 unique

### 日志中 "0.9/8" 的含义
日志报告的 `mean_diversity: 0.9/8` 表示平均多样性比率约 0.9（即约 7.2/8 unique），与实际统计一致。

### 结论
**RSFT 数据多样性完全可行。** 94% 的文档 8 个生成全部不同，平均 unique 比率 98.5%。仅 2 个文档出现低多样性。T=0.7 的温度设置产生了足够差异化的输出，RSFT 方向没有多样性瓶颈。

---
