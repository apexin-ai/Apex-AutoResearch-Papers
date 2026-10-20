# infra restart oft baseline cuda2

**afford invar** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_infra_restart-oft-baseline-cuda2_20260520T001057_result.json`
- **Structured JSON:** [`e23f4fc29f36f94a2ac7.json`](../../sessions/e2/e23f4fc29f36f94a2ac7.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

发现问题：**之前的 OFT baseline 训练（PID 123110）还在 GPU 2 上运行**，已运行 5 分 29 秒，输出目录是 `/root/afford_invar/runs`（根分区，非数据盘）。端口 29503 也被它占用。

有两个选择：
1. **杀掉旧进程**，用数据盘输出目录从头重启
2. **保留旧进程**（它正在训练中），只改输出目录到数据盘的问题后续处理

旧进程的 `--run_root_dir` 指向根分区 `/root/afford_invar/runs`，不是数据盘。要杀掉重启吗？

---
