# analyze eval perdof object norm003 seed43

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analyze_eval-perdof-object-norm003-seed43_20260519T032817_result.json`
- **Structured JSON:** [`4327cc0e170dc5c1442d.json`](../../sessions/43/4327cc0e170dc5c1442d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 已更新为 DONE/success。

## 分析结论

**Overall success rate: 13% (13/100)**

### Per-task 分布

| Task | seed43 |
|------|--------|
| alphabet_soup | 0% |
| cream_cheese | 0% |
| salad_dressing | 20% |
| bbq_sauce | 30% |
| ketchup | 0% |
| tomato_sauce | 10% |
| butter | 10% |
| milk | 10% |
| chocolate_pudding | 20% |
| orange_juice | 30% |

成功集中在 bbq_sauce、orange_juice (各 30%)、salad_dressing、chocolate_pudding (各 20%)，3 个任务完全失败。

### 与 seed42 对比

- seed42 = 14%, seed43 = 13%, 差 1 个百分点（1/100 rollouts），完全在噪声范围内。
- ε=0.03 两个 seed 均值 = **13.5%**。

### Conclusion: **success**

13% >= 10% 阈值，且与 seed42 (14%) 高度一致。这确认了 ε=0.03 的 cross-seed 稳定性，增强了 magnitude curve 低 ε 端的统计置信度。

### 更新后的 ε=0.03 数据点

ε=0.03: mean=13.5%, std=0.5%, n=2 (seed42=14%, seed43=13%)。与 ε=0.05 的 mean=12% (n=3) 相比略高，符合"低 ε 表现更好"的趋势。

---
