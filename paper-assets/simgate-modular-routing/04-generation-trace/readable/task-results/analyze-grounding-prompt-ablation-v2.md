# analyze grounding prompt ablation v2

**Death Avoidance as the Dominant Routing Signal: A Counterfactual Analysis on ScienceWorld** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analyze_grounding-prompt-ablation-v2_20260518T220637_result.json`
- **Structured JSON:** [`e6d849917dfd5a7d8320.json`](../../sessions/e6/e6d849917dfd5a7d8320.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**实验仍在运行中，尚未退出。**

- 进程 PID 168847 处于活跃状态（CPU 16.8%）
- tmux session `grounding-prompt-ablation` 仍存在
- 启动时间：May 19 06:01
- 当前进度：chemistry-mix 的 13/20 episodes（第 1/10 个 task）
- 已完成的 13 个 episode 全部 death=false

`~/runs/simgate-modular-routing/grounding-prompt-ablation-v2.log` 中的 `EXIT_CODE=0` 是 registry sync 写入的，不是实验退出码。

**预估剩余时间**：每个 episode 约 25-30s，剩余 ~187 episodes，约 80-90 分钟完成。

**初步观察**（仅基于 chemistry-mix 前 13 episodes）：
- Death rate: 0/13 = 0%（baseline chemistry-mix 的 DR 需要对比）
- 但仅 1 个 task 的部分数据，不足以下结论

建议等实验完成后再分析。需要我设置定时检查吗？

---
