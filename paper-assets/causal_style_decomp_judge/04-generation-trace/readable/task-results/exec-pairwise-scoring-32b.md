# exec pairwise scoring 32b

**The Likert Blindspot: Measurement-Mode Divergence in LLM Judge Style Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_exec_pairwise_scoring_32b_20260520T173534_result.json`
- **Structured JSON:** [`e6d631b14997e3b5fddf.json`](../../sessions/e6/e6d631b14997e3b5fddf.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。以下是完整结果：

---

## Pairwise Comparison 完整分析结果

### 1. 总体统计
| 指标 | 值 |
|------|-----|
| N (有效) | 99 (1条null) |
| Formal wins | 57 (57.6%) |
| Casual wins | 42 (42.4%) |
| Formal win rate | 0.5758 |
| **Binomial p-value (vs 0.50)** | **0.159070** (不显著) |

### 2. Position Bias 检查
| 位置 | 被选次数 | 比例 |
|------|---------|------|
| Chose A | 47/99 | 47.5% |
| Chose B | 52/99 | 52.5% |

位置偏差极小，随机化有效。

### 3. 方向分析
| 方向 | n | Formal wins | 比例 | p-value |
|------|---|------------|------|---------|
| formal→casual | 58 | 36 | 62.1% | 0.086949 |
| casual→formal | 41 | 21 | 51.2% | 1.000000 |

formal→casual 方向的 formal 偏好更强（边缘显著），casual→formal 方向基本无差异。

### 4. NLI 分层分析
| 子集 | n | Formal wins | 比例 | p-value |
|------|---|------------|------|---------|
| NLI≥0.90 | 87 | 52 | 59.8% | 0.085689 |
| All | 99 | 57 | 57.6% | 0.159070 |

高 NLI（语义保持好）子集中 formal 偏好更强，接近显著。

### 5. pairwise_summary.csv
```
n,formal_wins,casual_wins,formal_win_rate,binomial_p,position_a_rate
99,57,42,0.5757575757575758,0.1590696518812378,0.47474747474747475
```

### 关键发现
- 整体 formal win rate 57.6%，但 p=0.159 **未达 0.05 显著**
- NLI≥0.90 子集 p=0.086，formal→casual 方向 p=0.087，均为**边缘显著**
- Position bias 几乎不存在 (47.5% vs 52.5%)
- 方向不对称：当原始文本是 formal 时，judge 更偏好 formal (62.1%)；当原始文本是 casual 时，几乎无偏好 (51.2%)

---
