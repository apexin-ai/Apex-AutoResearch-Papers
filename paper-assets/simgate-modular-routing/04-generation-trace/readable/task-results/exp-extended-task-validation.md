# exp extended task validation

**Death Avoidance as the Dominant Routing Signal: A Counterfactual Analysis on ScienceWorld** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_exp_extended-task-validation_20260519T203302_result.json`
- **Structured JSON:** [`956092ad545375514d21.json`](../../sessions/95/956092ad545375514d21.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

任务已启动并运行：

- **GPU 0** (ext-val-gpu0): boil → melt → find-living-thing (3 tasks × 20 eps)
- **GPU 1** (ext-val-gpu1): use-thermometer → power-component (2 tasks × 20 eps)
- **模型**: Qwen2.5-7B-Instruct, vLLM v0.18.1
- **参数**: max_steps=30, seed=42, temperature=0.3

首批 episode 已开始（boil 内部策略 score=-100 → death，use-thermometer 同样 death）。预估总运行时间 5-8 小时。4.5 分钟后自动检查进度。

---
