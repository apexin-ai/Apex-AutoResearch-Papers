# ssh emergency diagnose

**prism collapse mixing** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_emergency-diagnose_20260515T221719_result.json`
- **Structured JSON:** [`455d50e4b7bea87a7244.json`](../../sessions/45/455d50e4b7bea87a7244.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**训练没有崩溃，正在正常运行。**

诊断结果：

- **进程存活**：PID 200889 (GPU 0) 和 200890 (GPU 1) 正在运行
- **显存占用**：每卡 8470MiB，符合预期
- **日志活跃**：正在执行 `per-example signals` 阶段
  - seed137：~74% (231/313)
  - seed42：~67% (210/313)
  - 处理速度 ~11-15s/item，持续推进中
- **GPU 0% utilization 是正常的**：signal 计算阶段做逐样本 forward pass，每次推理很短，`nvidia-smi` 瞬时采样容易采到间隙，显示 0%。显存占用 + 日志持续更新 = 进程正常工作。

不需要任何修复或重启。预计 signal 阶段还需 ~20-30 分钟完成，之后进入下一步。

---
