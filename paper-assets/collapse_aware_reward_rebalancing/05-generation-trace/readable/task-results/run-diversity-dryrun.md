# run diversity dryrun

**Does Reward Curation Kill Diversity? Systematic Evidence of Surprising Resilience in Iterative Self-Training** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_run_diversity-dryrun_20260516T090727_result.json`
- **Structured JSON:** [`d56e784368c1a1abad10.json`](../../sessions/d5/d56e784368c1a1abad10.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Dry-run 完成（~28 分钟）。结果分析：

## Corpus-Level Diversity Scoring 结果

### 分布统计
| 指标 | 值 |
|------|-----|
| Mean | 0.2043 |
| Std | 0.0400 |
| Min | 0.1007 |
| Max | 0.4017 |
| Median | 0.2005 |
| IQR | 0.0557 |

### Within-Prompt 区分力
| 指标 | 值 |
|------|-----|
| Mean within-prompt std | 0.0164 |
| Mean within-prompt range | 0.0423 |
| 100% prompts range > 0.01 | ✓ |
| 30% prompts range > 0.05 | ✓ |

### Curation Impact（关键指标）
| 策略 | Mean Diversity |
|------|---------------|
| Always pick highest | 0.2277 |
| Random | 0.2043 |
| Always pick lowest | 0.1853 |
| **Discrimination gap** | **0.0423** |

### 结论

**W2-fixed corpus-level diversity scoring 具有足够的区分力：**

1. **方差合理**：std=0.04，IQR=0.056，分数不是挤在一起的（range 0.10-0.40，4倍差距）
2. **100% 的 prompt 内 4 个候选有 >0.01 的分差**，所以每个 prompt 都能区分候选
3. **Curation impact = 0.0423**：选最高 vs 最低 diversity 的候选，平均差 4.2 个百分点。在 reward-weighted curation 中，这个差距足以让 diversity signal 发挥 rebalancing 作用
4. **30% 的 prompt 有 >0.05 的 within-prompt range**，说明对部分 prompt 来说 diversity signal 特别强

总结：diversity scoring 通过验证，可以用于 CARR 的 reward rebalancing pipeline。

---
