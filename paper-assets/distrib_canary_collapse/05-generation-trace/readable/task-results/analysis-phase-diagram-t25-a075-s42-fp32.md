# analysis phase diagram t25 a075 s42 fp32

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_phase_diagram_t25_a075_s42_fp32_20260521T231853_result.json`
- **Structured JSON:** [`fef0d5a14ad1b4dc09e5.json`](../../sessions/fe/fef0d5a14ad1b4dc09e5.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

分析完成。

---

## 结果报告

### PermG 结果
| 指标 | 值 |
|------|-----|
| **PermG fwd (FDR)** | **8/8** |
| PermG rev (FDR) | 0/8 |
| Diff XCorr fwd | 8/8 |
| Threshold onset | 0/8 |
| TY Granger fwd | 2/8 |
| Robust pairs (≥3/5) | 4/8 |

### 与理论预测和历史对比
| T | α=0.75 PermG | 备注 |
|---|---|---|
| 5 | 0/8 | 信号不足 |
| 10 | 6/8 | mauve pair 失败 |
| 15 | 6/8 | mauve pair 失败 |
| 20 | 6/8 | mauve pair 失败 |
| **25** | **8/8** | downstreams=distinct+perplexity |

### Conclusion: **SUCCESS**

α=0.75 >> α_c(25)≈0.232，PermG 8/8 确认高污染下的强健检测。不对称性完美（fwd=8, rev=0）。

**注意**：T=25 的 downstreams 为 `[distinct_1, distinct_2, distinct_3, perplexity]`，而 T=10/15/20 使用的是 `[distinct_1, distinct_2, distinct_3, mauve]`。8/8 vs 6/8 的差异部分由 perplexity 替换 mauve 引起（mauve 是已知的 bottleneck）。直接跨 T 对比需标注此差异。

### Phase Diagram T=25 行进度
| α=0.45 | α=0.50 | α=0.60 | α=0.75 |
|--------|--------|--------|--------|
| RUNNING | RUNNING | RUNNING | **DONE ✓ (8/8)** |

---
