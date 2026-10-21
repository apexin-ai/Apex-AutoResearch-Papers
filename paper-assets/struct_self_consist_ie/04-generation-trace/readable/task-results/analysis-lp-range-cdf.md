# analysis lp range cdf

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_lp_range_cdf_20260515T124301_result.json`
- **Structured JSON:** [`13bfe44d86aed7034f49.json`](../../sessions/13/13bfe44d86aed7034f49.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。汇总结果：

### LP Range CDF 分析结果

**551 个 SciERC NER instances, N=8 samples, Qwen3-8B**

#### LP Range 分布
| Percentile | LP Range (nats) |
|-----------|----------------|
| Median | 0.041 |
| 75th | 0.069 |
| 90th | 0.122 |
| 95th | 0.177 |
| Mean ± Std | 0.062 ± 0.069 |

#### 各 ε 阈值下的 "effectively tied" 比例
| ε | Fraction below |
|------|---------------|
| 0.01 | 2.0% |
| 0.02 | 14.2% |
| 0.03 | 31.8% |
| **0.05** | **59.7%** |
| 0.10 | 83.7% |
| 0.15 | 93.1% |
| 0.20 | 96.6% |

CDF 曲线是平滑的——不存在 ε=0.05 处的 cliff，59.7% 处于连续 CDF 的自然位置，而非 arbitrary cutoff 造成的跳变。

#### Within-instance LP-F1 Correlation（ε-free 指标）
- **Pooled Spearman ρ(LP, F1) = 0.248**（p < 1e-62, n=4408 pairs）——LP 对质量有弱正相关但解释力有限
- **Instance-level Spearman ρ(LP_range, F1_range) = 0.328**（p < 1e-14）——LP 分散度越大，F1 变异越大
- **Per-instance Spearman**: 435 个可计算，仅 21.6% 达到 p<0.05 显著，mean ρ=0.18——N=8 下 LP 对单 instance 质量排序能力弱

#### 产出文件
- 数据：`output/analysis_lp_range_cdf.json`
- 图表：`output/figures/lp_range_cdf.pdf` / `.png`
- 脚本：`code/analyze_lp_range_cdf.py`

---
