# ops c2 qw n500 recovery

**Phase-Modulated Compound Sparsity Severity in 7B-Scale Mathematical Reasoning Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_c2_qw_n500_recovery_20260514T192347_result.json`
- **Structured JSON:** [`bc0a185d5381b62a6479.json`](../../sessions/bc/bc0a185d5381b62a6479.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 诊断结果

**cron 误判确认**：所有 4 个进程均健康运行，cron 在 s015→s020 条件切换时误判。

### 4 GPU 当前状态

| GPU | PID | 任务 | 进度 | GPU Util |
|-----|-----|------|------|----------|
| 0 | 156554 | DS imp_s020 | **109/500** | 98% |
| 1 | 154305 | DS rand_s020 | **154/500** | 80% |
| 2 | 159269 | **QW imp_s020** | **52/500** | 96% |
| 3 | 159794 | **QW rand_s020** | **29/500** | 76% |

### c2_qw_n500 Condition 完成情况（GPU2/GPU3）

每条 GPU 线路顺序执行 4 个 sparsity level：s015 → s020 → s025 → s030

**GPU2 (importance)**:
- `qw_imp_s015` — **已完成** (profiling_results.json 18.7MB, 03:02 UTC)
- `qw_imp_s020` — **运行中** (52/500, PID 159269)
- `qw_imp_s025` — 未开始
- `qw_imp_s030` — 未开始

**GPU3 (random)**:
- `qw_rand_s015` — **已完成** (profiling_results.json 18.7MB, 03:11 UTC)
- `qw_rand_s020` — **运行中** (29/500, PID 159794)
- `qw_rand_s025` — 未开始
- `qw_rand_s030` — 未开始

### 进程管理方式

脚本通过 `run_c2_qw_n500_gpu2.sh` / `run_c2_qw_n500_gpu3.sh` 顺序执行（`set -e`），不是 screen/tmux 管理（ssh_read_only 无法执行 `screen -ls` 验证，但从 /proc/cmdline 看是直接 python 进程，由 shell 脚本串联驱动）。

### 结论

进程正常，无需重启。cron 监控需要适配"条件切换间隙"场景——旧 PID 退出到新 PID 启动之间有短暂空窗期，不应判定为 failed。

---
