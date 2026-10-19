# verify exp002v3 gpu

**The Probe Reward Trap: Behavioral Death Before Distributional Collapse in Sycophancy Calibration** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_verify_exp002v3-gpu_20260519T180346_result.json`
- **Structured JSON:** [`c8c39c515022861e572f.json`](../../sessions/c8/c8c39c515022861e572f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**exp-002v3 未在运行。** 具体情况：

| 检查项 | 结果 | 状态 |
|--------|------|------|
| GPU 0+3 占用 | GPU 0: 5MiB/0%, GPU 3: 4MiB/0% — **空闲** | FAIL |
| PID 149439 | **不存在** | FAIL |
| train.log | 有初始化日志（02:02:49-50），停在 DeepSpeed 编译阶段，无训练输出 | FAIL |
| tmux session | `tmux ls` 被 read_only 拦截，但 ps 输出中只看到 `exp-008v3` session | FAIL |

当前 GPU 实际占用情况：
- **GPU 1+2**：被 `exp-008v3`（`run_exp008v3_binary_probe_grpo.py`）占用，PID 104503/104504，~31GB/30GB 显存，利用率 76%/68%
- **GPU 0+3**：完全空闲

exp-002v3 看起来启动后在 DeepSpeed 初始化阶段就退出了，进程已不存在。需要检查完整日志定位失败原因。

---
