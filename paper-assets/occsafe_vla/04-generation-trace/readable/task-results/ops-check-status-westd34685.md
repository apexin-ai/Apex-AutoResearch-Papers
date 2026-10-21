# ops check status westd34685

**Does Auxiliary Spatial Supervision Make Vision-Language-Action Models Safer? A Factorial Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_check_status_westd34685_20260523T221131_result.json`
- **Structured JSON:** [`c498c8138ca438684d91.json`](../../sessions/c4/c498c8138ca438684d91.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## westd-34685 状态汇总

### GPU 状态

| GPU | 利用率 | 显存占用 | 状态 |
|-----|--------|----------|------|
| cuda:0 | 50% | 63,013 / 97,887 MiB | **训练中** — cutoff_45k_s0 |
| cuda:1 | 96% | 63,037 / 97,887 MiB | **训练中** — cutoff_15k_s0 |
| cuda:2 | 0% | 0 MiB | **空闲** |
| cuda:3 | 0% | 0 MiB | **空闲** |

### 训练进度

| 任务 | 进度 | 已耗时 | 预计剩余 | 速度 |
|------|------|--------|----------|------|
| cutoff_45k_s0 (cuda:0) | **23%** — 11,614/50,005 | 3h36m | ~10h | 1.08 it/s |
| cutoff_15k_s0 (cuda:1) | **25%** — 12,521/50,005 | 4h03m | ~9h37m | 1.08 it/s |

最近 loss (cutoff_45k_s0 step 11600): `occ_loss=0.0103, action_loss=0.1406`
最近 loss (cutoff_15k_s0 step 12500): `occ_loss=0.0142, action_loss=0.1055`

### Eval 进程

两个 eval **正在运行中**（cuda:2 和 cuda:3）：

- **cutoff_25k_s0_eval**: Task 5/10 进行中（Task 4 完成: TSR=0.740, CAR=1.000），已跑 21m40s
- **reverse_cutoff_s0_eval**: Task 4/10 进行中（96% episodes），稍落后于 cutoff_25k

### Eval 结果文件

`/root/occsafe_vla/artifacts/` 下最新两个 eval 结果：
- `safelibero_libero_spatial_20260524_051323.json` (May 24 06:05, 236KB)
- `safelibero_libero_spatial_20260524_051327.json` (May 24 06:01, 236KB)

这两个应该是之前完成的 eval，当前跑的 reverse_cutoff 和 cutoff_25k 的结果尚未生成。

### tmux

tmux session 存在（`/tmp/tmux-0`），但 `tmux list-sessions` 被 read_only 拦截，无法列出具体 session 名称。

---
