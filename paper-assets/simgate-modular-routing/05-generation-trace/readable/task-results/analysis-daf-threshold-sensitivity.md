# analysis daf threshold sensitivity

**Death Avoidance as the Dominant Routing Signal: A Counterfactual Analysis on ScienceWorld** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_daf-threshold-sensitivity_20260516T060023_result.json`
- **Structured JSON:** [`f264561c9422df9e249c.json`](../../sessions/f2/f264561c9422df9e249c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。结果摘要：

**验证通过**: T=-100 → DAF=90.4%, r=0.9698 ✓

**Method 1 (绝对阈值)**:
| T | avoidance | r |
|---|---|---|
| -100 | 90.4% | 0.9698 |
| -50, -20 | 90.4% | 0.9698 (无中间分数) |
| 0 | 100.0% | -0.13 |
| 10 | 100.0% | 0.02 |
| 20 | 88.5% | 0.20 |

**Method 2 (相对 drop)**:
| X% | avoidance | r |
|---|---|---|
| 50% | 87.4% | -0.52 |
| 75% | 87.4% | 0.26 |
| 90% | 100.0% | 0.08 |
| 100% (=death) | 90.4% | 0.9698 |

**Method 3 (Rank-based)**: Q1 阈值恰好是 -100 (42.9% episodes 死亡)，det-preferred 率 66.7% vs overall 35.1%（1.9x enrichment）。

**结论**: DAF robust — 所有阈值下 avoidance fraction 均 > 87%（远超 70% 标准）。failure avoidance 不依赖于 -100 这个特定 threshold 选择。关键 insight: 因为 ScienceWorld 分数是 bimodal 的（-100 或 ≥0），T ∈ {-100, -50, -20} 和 X=100% 给出完全相同的结果。

脚本: `/root/autodl-tmp/simgate-modular-routing/scripts/daf_threshold_sensitivity.py`
结果: `/root/autodl-tmp/simgate-modular-routing/artifacts/daf-sensitivity-extended/threshold_sensitivity.json`

---
