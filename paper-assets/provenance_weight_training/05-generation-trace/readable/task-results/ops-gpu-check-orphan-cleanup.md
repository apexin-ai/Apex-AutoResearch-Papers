# ops gpu check orphan cleanup

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_gpu_check_orphan_cleanup_20260515T220118_result.json`
- **Structured JSON:** [`2f6c8c70bfdf0895d9e1.json`](../../sessions/2f/2f6c8c70bfdf0895d9e1.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 结果

### 4 个合法进程 — 确认正常

| GPU | Job | Python PID | VRAM | Util |
|-----|-----|------------|------|------|
| 0 | contamination_60_seed42_r2 | 257982 | 46,514 MiB / 97,887 MiB | 82% |
| 1 | contamination_60_uniform_seed42 | 250079 | 46,514 MiB / 97,887 MiB | 99% |
| 2 | bs8_nmin2_seed42_r2 | 238719 | 81,696 MiB / 97,887 MiB | 100% |
| 3 | contamination_60_grid_b0_5_seed42 | 255786 | 46,514 MiB / 97,887 MiB | 99% |

全部在正确的 GPU 上。

### Orphan 进程处理

- **PID 258500** (grid_b_low_serial_seed42) — 已经不存在，之前因 CUDA OOM 自行崩溃
- **PID 257545** (grid_b_low_b0.1_seed42，父进程 257540，脚本 `run_grid_b_low_seed42.sh`) — **发现仍在 GPU 0 上运行**，占用 46,514 MiB → **已 kill，确认死亡**

GPU 0 显存从 93,042 MiB 降至 46,523 MiB，释放了 ~46.5 GiB。

### Tmux sessions

只有 `contamination_60_seed42_r2`（合法 job 的 session），无 grid_b_low 相关的 rogue session。

### grid_b_low 系列失败根因

**CUDA OOM**。orphan PID 257545 (`grid_b_low_b0.1_seed42`) 违规占用 GPU 0 约 45 GiB，导致后续在 GPU 0 上启动的 `grid_b_low_serial_seed42` (PID 258500) 没有足够显存，在 forward pass 中 OOM 崩溃：

> `torch.OutOfMemoryError: Tried to allocate 32.00 MiB. GPU 0 has a total capacity of 94.97 GiB of which 31.44 MiB is free. Process 257545 has 45.42 GiB memory in use. Process 257982 has 45.42 GiB memory in use.`

`grid_b_low_seed42_r3` 的日志显示它在 step 164/6103 时仍在运行（就是 orphan 257545 本身的进度）。

### 总结

问题已清理完毕。GPU 0 现在只有合法 job 在跑，4 卡各一个进程。grid_b_low 实验如需重跑，GPU 0 目前仍有 ~51 GiB 空余（但建议等某个 job 完成后独占一张卡）。

---
