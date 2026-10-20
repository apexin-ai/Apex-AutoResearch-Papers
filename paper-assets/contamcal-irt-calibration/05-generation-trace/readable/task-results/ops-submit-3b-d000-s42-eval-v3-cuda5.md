# ops submit 3B d000 s42 eval v3 cuda5

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_submit-3B-d000-s42-eval-v3-cuda5_20260515T055024_result.json`
- **Structured JSON:** [`59e6d614e943888afb09.json`](../../sessions/59/59e6d614e943888afb09.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

GPU 5 上有两个 `compute_signals.py` 进程（exp008 的 RL signal 计算），运行约 20 分钟，占用 ~21GB 显存。

根据约束 C001/C002，**不能在 GPU 5 提交新任务**。需要等这两个进程完成或由 Director 指定其他空闲 GPU。

要查一下哪些 GPU 当前空闲吗？

---
