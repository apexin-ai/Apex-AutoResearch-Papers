# ops check xvla k01 seed42 and launch k08 seed42

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_check-xvla-k01-seed42-and-launch-k08-seed42_20260520T205503_result.json`
- **Structured JSON:** [`b2fe16642c90a147b035.json`](../../sessions/b2/b2fe16642c90a147b035.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两个任务均完成。

**任务 1 — X-VLA k=0.1 seed42 结果:**
- **overall_success_rate = 0.0%** (0/500)
- 所有 10 个 task 均为 0%，Wilson CI 95%: [0.0%, 0.8%]
- 符合预期（seed43=0%, seed44=0%）

**任务 2 — X-VLA k=0.8 seed42 启动状态:**
- tmux session `eval_xvla_k08_s42` 已创建
- GPU 0: PID 335130, 2296MiB 占用, 19% util（模型加载中）
- 4 张 GPU 全部在跑评估

---
