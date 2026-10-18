# ops verbosity nli rerun

**The Likert Blindspot: Measurement-Mode Divergence in LLM Judge Style Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_verbosity_nli_rerun_20260520T212813_result.json`
- **Structured JSON:** [`76386ed50b2f03e10d9f.json`](../../sessions/76/76386ed50b2f03e10d9f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完整结果如下：

---

## Direction-aware NLI v2 结果报告

### 整体
- **Overall pass rate: 3/100 (3.0%)** — 使用 BERTScore ≥ 0.92 + NLI ≥ 0.90

### Direction 分布
| Direction | N | Passed | NLI mean | BERTScore mean |
|-----------|---|--------|----------|----------------|
| forward (compression: verbose→concise) | 46 | 2/46 (4.3%) | 0.9476 | 0.8449 |
| backward (expansion: concise→verbose) | 54 | 1/54 (1.9%) | 0.8267 | 0.6732 |

### NLI direction-aware 效果（核心改进）
Direction-aware NLI 效果显著：
- **NLI ≥ 0.80: 86/100 (86.0%)** — 比之前 bidirectional 的 65% 大幅提升
- NLI ≥ 0.85: 86.0%
- NLI ≥ 0.90: 86.0%
- NLI ≥ 0.95: 83.0%

### 瓶颈：BERTScore
BERTScore 是主要瓶颈（verbosity 改变文本长度，BERTScore 天然对长度敏感）：
- BERTScore ≥ 0.80: 44/100 (44.0%)
- BERTScore ≥ 0.85: 27/100 (27.0%)
- BERTScore ≥ 0.90: 7/100 (7.0%)
- BERTScore ≥ 0.92: 3/100 (3.0%)

### Threshold Sweep（联合阈值）
| BERTScore ≥ | NLI ≥ 0.90 |
|-------------|------------|
| 0.70 | 63/100 (63.0%) |
| 0.75 | 57/100 (57.0%) |
| 0.80 | 43/100 (43.0%) |
| 0.85 | 26/100 (26.0%) |

---

### 判定：FAIL (3% << 80%)

**核心发现：Direction-aware NLI 成功解决了原来的问题（86% vs 65%），但 BERTScore 0.92 阈值对 verbosity 轴不适用。** Verbosity 改写本质上改变文本长度，BERTScore（基于 token-level 对齐）对长度变化极其敏感，尤其是 backward（expansion）方向 BERTScore 均值仅 0.6732。

**建议方案（需你决定）：**
1. 对 verbosity 轴降低 BERTScore 阈值到 0.70-0.75（可得 57-63% pass rate）
2. 对 verbosity 轴去掉 BERTScore 门控，仅用 direction-aware NLI（86% pass rate at 0.90）
3. 换用对长度不敏感的语义相似度指标

---
