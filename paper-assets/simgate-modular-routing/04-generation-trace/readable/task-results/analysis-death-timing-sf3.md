# analysis death timing sf3

**Death Avoidance as the Dominant Routing Signal: A Counterfactual Analysis on ScienceWorld** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_death-timing-sf3_20260515T161427_result.json`
- **Structured JSON:** [`7b06fc5c996fcca4d1b8.json`](../../sessions/7b/7b06fc5c996fcca4d1b8.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

分析完成。核心发现：

**Death Timing 分布**
- Internal mode: 105 次死亡，mean step=18.4，median=17，66% 集中在 steps 10–19（mid-episode）
- Deterministic mode: 40 次死亡，mean step=21.7，median=22，70% 在 step 20+（late-episode）
- Deterministic 比 internal 平均多存活 3.3 步

**Mixed Routing 结论：价值有限**

关键矛盾 — internal 的死亡集中在 mid-episode（step 16-17 峰值），恰好是 agent 完成初步探索、开始执行任务关键交互的阶段。要避免大部分死亡需要对前 20 步都用 deterministic，但这等于放弃了 67% 的探索机会，几乎就是纯 deterministic 模式。

SimGate 的 task-level routing 比 step-level mixed routing 更合理：直接为整个 episode 选模态，避免了"安全与探索"在时间维度上的冲突。

报告已注册为 artifact（`art_20260515_0338b4`），包含完整统计、histogram 数据点、per-task breakdown、论文讨论建议文本、以及可视化 spec。

---
