# harvest a1 baseline object s42

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_harvest_a1-baseline-object-s42_20260524T141937_result.json`
- **Structured JSON:** [`b2699eed941e180417dd.json`](../../sessions/b2/b2699eed941e180417dd.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 已更新。以下是完整结果汇报：

---

## A1 VLA Baseline LIBERO-Object 评估结果

**Overall SR: 56.5% (113/200)** — 远低于官方报告的 99.8%，差距 43.3pp。

### Per-task 分解

| Task | SR | Successes/20 |
|------|-----|-------------|
| tomato_sauce | **95%** | 19/20 |
| chocolate_pudding | **90%** | 18/20 |
| bbq_sauce | **80%** | 16/20 |
| alphabet_soup | 65% | 13/20 |
| ketchup | 65% | 13/20 |
| butter | 65% | 13/20 |
| cream_cheese | 35% | 7/20 |
| salad_dressing | 35% | 7/20 |
| orange_juice | 25% | 5/20 |
| milk | **10%** | 2/20 |

### 关键发现

1. **差距是系统性的**：不仅 Task 0 低，全部 10 个 task 都远低于官方 99.8%。最好的 tomato_sauce 也只有 95%。
2. **方差极大**：从 10% (milk) 到 95% (tomato_sauce)，说明评估框架对不同物体的处理存在系统性偏差。
3. **结论 = negative**：我们的评估框架无法复现 A1 官方性能，差距达 43.3pp。这意味着 cross-architecture baseline 对比需要排除评估框架差异的影响，否则论文中直接引用此数据会误导。

可能原因：评估环境配置（action space、observation preprocessing、episode length）与 A1 官方评估 setup 存在差异。

---
