# exp plan 013 labeling quality

**Death Avoidance as the Dominant Routing Signal: A Counterfactual Analysis on ScienceWorld** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_exp_plan-013-labeling-quality_20260514T121003_result.json`
- **Structured JSON:** [`bf2d42bf6d11db1bdeed.json`](../../sessions/bf/bf2d42bf6d11db1bdeed.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Plan-013 全部完成。总结：

## 结果汇总

### (a) Tie Rate
- **Overall: 61.2%**（150/245 episodes）
- 46.9% both-alive ties, 14.3% both-died
- Per-task range: 50%–75%

### (b) Genuine vs Tie-Break
- **100% genuine, 0% tie-break**
- 标注方案不存在 tie-break 机制：ties → no-preference（排除训练）
- 86 个 det-preferred 中：70 death asymmetry + 16 score comparison（最小 delta = 8 分）
- 9 个 internal-preferred 中：5 death asymmetry + 4 score comparison

### (c) Strict-Only Retrain
- 数据与 ablation-b 完全相同（当前数据已是 strict-only）
- balanced_acc = 0.5729（ablation-b 4 seed 均值 0.5761 ± 0.005，在 1σ 内）
- Balanced acc 跨 seed 稳定（σ=0.5%），recall trade-off 高方差（σ≈10%）

### 对 reviewer 的回应
**Oracle circularity via tie-breaking 不成立。** 标注管线使用严格不等式比较 + death-awareness，ties 全部排除。训练数据中不存在任何来自 tie-break 规则的标签。

---
