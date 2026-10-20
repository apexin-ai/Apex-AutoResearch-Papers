# eval plan002 b01 s44

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_plan002-b01-s44_20260514T093148_result.json`
- **Structured JSON:** [`6400c7ab3253c8b2da0b.json`](../../sessions/64/6400c7ab3253c8b2da0b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 已更新（metrics + conclusion=success 已存在）。notes 中已有详细对比分析。

总结 plan002-additive-b01-s44 的 eval_sta 结果：

- **PR=0.89, mean_ISR=0.803, tautological_collapse=False** — 实验成功
- 相比 s42（PR=0.81, ISR=0.337），s44 在 PR 和 ISR 上均显著更优
- 相比 exec-only s44（PR=0.98 但 94% tautology），ISR reward 成功阻止了 collapse，component_count_2_ratio 仅 2.2%
- 65% 样本达到 ISR=1.0，component 分布健康（4-comp 54个，5-comp 33个）
- seed 间方差较大（s42 ISR=0.337 vs s44 ISR=0.803），3-seed 统计需结合 s43

---
