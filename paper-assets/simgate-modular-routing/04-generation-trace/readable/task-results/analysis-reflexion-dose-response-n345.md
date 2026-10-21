# analysis reflexion dose response n345

**Death Avoidance as the Dominant Routing Signal: A Counterfactual Analysis on ScienceWorld** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_reflexion-dose-response-n345_20260518T182923_result.json`
- **Structured JSON:** [`7d437640c35043ba27c1.json`](../../sessions/7d/7d437640c35043ba27c1.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。核心结论：

**完整曲线：**

| N | Reflexion DR | Retry DR |
|---|---|---|
| 1 | 47.5% | 51.2% |
| 2 | 40.0% | -- |
| 3 | **34.0%** | 40.9% |
| 4 | **36.5%** | -- |
| 5 | **35.0%** | 43.5% |

**Plateau 确认成立：**
- Reflexion N=3..5 在 34.0%-36.5% 区间波动（spread=2.5pp），N=3 vs N=5 仅差 1.0pp
- 所有有意义的改善集中在 N=1->2 (-7.5pp) 和 N=2->3 (-6.0pp)，N>3 后无增益
- Reflexion plateau (~35.2%) 比 retry plateau (~42.2%) 低约 **7pp**，说明 reflexion 的自我纠错提供了 retry 无法达到的安全收益

报告已保存并注册为 artifact `art_20260518_bdd415`。

---
