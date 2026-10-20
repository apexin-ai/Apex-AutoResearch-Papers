# analysis bf16 importance s020 s030

**Phase-Modulated Compound Sparsity Severity in 7B-Scale Mathematical Reasoning Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_bf16_importance_s020_s030_20260514T064103_result.json`
- **Structured JSON:** [`214324ad3fb0337f5077.json`](../../sessions/21/214324ad3fb0337f5077.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

数据全部提取完成。汇总如下：

---

## bf16_importance_s020 (sparsity=0.20)

### Interaction Index
| Phase | Mean | Median | CI | Winsorized Mean | Skewness |
|-------|------|--------|----|-----------------|----------|
| high | 0.1289 | 0.0145 | [-0.1975, 0.6647] | -0.0297 | 16.67 |
| mid | 1.2604 | 0.2027 | [0.7466, 1.8962] | 0.7660 | 7.05 |
| low | 6.0288 | 1.4963 | [4.4671, 7.9237] | 4.3426 | 6.01 |

### Per-Problem II Stats
| Phase | n | min | max | mean | median | std |
|-------|---|-----|-----|------|--------|-----|
| high | 49 | -0.1884 | 0.4196 | 0.0025 | 0.0036 | 0.0966 |
| mid | 40 | -0.0519 | 8.6969 | 0.6795 | 0.1977 | 1.4998 |
| low | 50 | -1.6151 | 22.6875 | 2.2301 | 1.1280 | 4.3758 |

### Other Metrics
- **gradient_paired_aggregate**: **5.90** (low 6.0288 - high 0.1289)
- **pass_fail**: ci_overlap=PASS, sign_reversal=FAIL, overall=**PASS**
- **n_problems**: 50
- **phase_stats**: high(21086 tokens, 387 seg), mid(13306 tokens, 191 seg), low(27748 tokens, 397 seg)

### Perplexity (s=0.20)
| Phase | dense | attn | kv | both |
|-------|-------|------|-----|------|
| high | 1.1689 | 1.5233 | 1.6191 | 2.1047 |
| mid | 1.2269 | 1.5375 | 3.5164 | 5.4246 |
| low | 1.2286 | 1.6486 | 15.7987 | **23.74** |

---

## bf16_importance_s030 (sparsity=0.30)

### Interaction Index
| Phase | Mean | Median | CI | Winsorized Mean | Skewness |
|-------|------|--------|----|-----------------|----------|
| high | 0.5547 | 0.0534 | [0.2773, 0.9198] | 0.3367 | 10.62 |
| mid | 11.3000 | 2.2833 | [6.8650, 17.2633] | 8.1752 | 9.19 |
| low | 57.7946 | 14.6395 | [41.4416, 77.0467] | 39.3143 | 8.31 |

### Per-Problem II Stats
| Phase | n | min | max | mean | median | std |
|-------|---|-----|-----|------|--------|-----|
| high | 49 | -0.5095 | 4.4457 | 0.1976 | 0.0343 | 0.6793 |
| mid | 40 | -0.1989 | 34.0258 | 5.2585 | 1.5173 | 7.9382 |
| low | 50 | -7.3027 | 126.7985 | 22.6601 | 9.9731 | 28.4096 |

### Other Metrics
- **gradient_paired_aggregate**: **57.24** (low 57.7946 - high 0.5547)
- **pass_fail**: ci_overlap=PASS, sign_reversal=FAIL, overall=**PASS**
- **n_problems**: 50
- **phase_stats**: high(21086 tokens, 387 seg), mid(13306 tokens, 191 seg), low(27748 tokens, 397 seg)

### Perplexity (s=0.30)
| Phase | dense | attn | kv | both |
|-------|-------|------|-----|------|
| high | 1.1689 | 1.7123 | 2.0544 | 3.2372 |
| mid | 1.2269 | 1.7894 | 9.4821 | 24.2847 |
| low | 1.2286 | 1.9347 | 51.6485 | **122.61** |

---

## 趋势分析（4点序列：s015 → s020 → s025 → s030）

| Metric | s=0.15 | s=0.20 | s=0.25 | s=0.30 |
|--------|--------|--------|--------|--------|
| gradient | 69.24 | **5.90** | 222.35 | **57.24** |
| low_median | 0.40 | **1.50** | 7.20 | **14.64** |
| high_median | 0.006 | **0.015** | 0.03 | **0.053** |
| PPL low_both | 12.51 | **23.74** | 63.67 | **122.61** |

**low_median**: 单调递增 ✓ (0.40 → 1.50 → 7.20 → 14.64)，s020 完美填补 s015-s025 之间的空缺。

**high_median**: 单调递增 ✓ (0.006 → 0.015 → 0.03 → 0.053)。

**PPL low_both**: 单调递增 ✓ (12.51 → 23.74 → 63.67 → 122.61)，近似指数增长，符合预期。

**gradient**: **非单调** ✗ (69.24 → 5.90 → 222.35 → 57.24)。s020 和 s030 的 gradient 远低于其相邻点，呈锯齿形。这是因为 gradient = low_mean - high_mean，而 mean 受右偏分布中的极端值影响极大（skewness 6-17）。**median 基础的指标远比 mean-based gradient 更稳定可靠**，建议后续分析以 median 为主。

---
