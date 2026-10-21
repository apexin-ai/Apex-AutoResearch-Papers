# urgent re selection recompute

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_urgent_re_selection_recompute_20260515T034814_result.json`
- **Structured JSON:** [`0b9b3b1fdf92b36cc3af.json`](../../sessions/0b/0b9b3b1fdf92b36cc3af.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

计算完成。以下是诊断结论：

---

## RE Selection F1 重新计算结果

### Q1: 全集 greedy F1 是多少？
**Macro F1 = 0.4042**, Micro F1 = 0.4436。论文中的 0.404 和 0.395 都不完全准确——或者说 0.404 是正确的 macro greedy F1。0.395 可能来自某个旧版 selection 值（logprob selection = 0.3948，非常接近 0.395）。

### Q2: 哪个 signal 最高？
全集上 **logprob** 的 selection F1 最高 = **0.3948**，其次是 voting_conf = 0.3944。但**所有 5 个信号的 selection F1 都低于 greedy**（0.4042），无一例外。

### Q3: 全集 vs 条件集差异
- 全集 greedy = 0.404, 条件集 greedy = 0.674（差 0.27）
- 全集有 **40.1%（159/397）的实例 greedy F1 = 0**，这些零值严重拉低了均值
- 条件集（n=238）排除了这些零后，所有数值大幅上升
- **0.395 vs 0.410 的矛盾根因**：0.395 ≈ logprob selection F1 在全集上的值（0.3948），0.410 可能来自某个带不同过滤条件或不同数据子集的旧计算。两个数字对应不同集合/不同指标，并非同一计算的不同结果。

### Q4: Macro vs Micro？
Macro = 0.4042, Micro = 0.4436，差距 0.039。论文若混用了两种平均方式，也可能产生部分数值差异。

### Q5: Greedy F1 分布（全集 n=397）
| 区间 | 数量 | 占比 |
|------|------|------|
| 0 | 159 | 40.1% |
| (0, 0.2] | 6 | 1.5% |
| (0.2, 0.4] | 52 | 13.1% |
| (0.4, 0.6] | 53 | 13.4% |
| (0.6, 0.8] | 38 | 9.6% |
| (0.8, 1.0] | 89 | 22.4% |

### 结论
**RE 上所有 5 个 selection signal 均输 greedy，定性结论确认：selection 在 RE 上无效。** 论文主表应报告 greedy=0.404, logprob-best=0.395（实际 0.3948），Δ=−0.009。appendix 中 0.410 的数字需要追溯来源——它不是来自这个数据集/配置的任何合理计算。

JSON 已保存至 `/root/autodl-tmp/struct_self_consist_ie/output/review_round2/re_selection_recompute.json`。

---
