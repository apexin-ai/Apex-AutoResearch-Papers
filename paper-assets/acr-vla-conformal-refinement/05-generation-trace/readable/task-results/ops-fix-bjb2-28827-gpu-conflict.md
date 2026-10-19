# ops fix bjb2 28827 gpu conflict

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_fix-bjb2-28827-gpu-conflict_20260516T111949_result.json`
- **Structured JSON:** [`35e5c52741c67063b32c.json`](../../sessions/35/35e5c52741c67063b32c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。总结：

**已执行：**
- Kill PID 246301（GPU 2 上旧的 obs_only norm=0.3 seed45）— 成功

**当前状态：**
- GPU 2：仅 PID 248661（新进程），冲突已解决
- GPU 3：PID 242264 + PID 248932 并行，显存 11.3GB/24.6GB，余量充足，无需干预

**注意：** `eval_object_obs_only_norm03_seed45.json` 当前损坏/不完整。新进程 248860 仍在运行中，会从头写入结果覆盖该文件。如果该进程是追加写入模式（而非覆盖），可能需要删除旧文件后重启评估。

---
