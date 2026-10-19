# ops path rename

**error diag dpo recovery** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_path-rename_20260513T152028_result.json`
- **Structured JSON:** [`3190721271b801b62501.json`](../../sessions/31/3190721271b801b62501.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**v9 仍在运行，路径规范化需等 v9 完成后再执行。**

## v9 进程状态

| PID | 运行时长 | GPU | 显存占用 | 任务 |
|-----|---------|-----|---------|------|
| 884787 | 7h03m | CUDA 0 | 16,306 MiB | collect_trajectories_icl part 0/3 |
| 885185 | 7h03m | CUDA 1 | 19,874 MiB | collect_trajectories_icl part 1/3 |
| 885703 | 7h03m | CUDA 4 | 14,590 MiB | collect_trajectories_icl part 2/3 |

3 个进程均在 tmux session 中运行（datagen_v9_icl_cuda0/1/4），timeout 设为 43200s（12h），已运行约 7 小时，剩余约 5 小时 timeout 余量。

另有 2 个 VLLM Worker（PID 17800/17803）各占 22,446 MiB，属于模型推理服务。

所有进程的工作目录和日志路径都硬编码了 `/root/autodl-tmp/rl-active-probe-fl`，此时重命名目录会导致进程崩溃。需等 v9 全部完成后再执行路径规范化。

---
