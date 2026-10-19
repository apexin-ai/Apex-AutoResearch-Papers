# investigate bjb1 18228 gpu status

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_investigate_bjb1-18228-gpu-status_20260526T101320_result.json`
- **Structured JSON:** [`725a3ed8fe02271d7e3b.json`](../../sessions/72/725a3ed8fe02271d7e3b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## bjb1-18228 GPU 占用排查结果

当前时间 2026-05-26 18:13:55，4 块 GPU 全部被同一项目的 `src/evaluate.py` 评估进程占用，没有僵尸进程，**全部是正在跑的真实任务**。

| GPU | PID | 启动时间 | 运行时长 | 任务 | seed | 输出文件 | 来源 |
|-----|-----|----------|----------|------|------|----------|------|
| 0 | 2558 | 11:45:30 | ~6h28m | `pi05` + `crm_obs_only` K=2 norm=0.05 / **long** | 42 | `eval_long_crm_obs_only_norm0.05_seed42_pi05_K2.json` | tmux 手动 nohup |
| 1 | 2916 | 11:46:00 | ~6h27m | `pi05` + `crm_obs_only` K=2 norm=0.05 / **long** | 43 | `eval_long_crm_obs_only_norm0.05_seed43_pi05_K2.json` | tmux 手动 nohup |
| 2 | **42110** | 14:45:50 | ~3h28m | `pi05` + `adaptive_conformal_crm` K=2 norm=0.2 τ=0.25 / **goal** | 43 | `eval_goal_adaptive_pi05_seed43_bjb1.json` | **cron**: `pi05-adaptive-goal-s43-bjb1-18228` |
| 3 | 3764 | 11:48:12 | ~6h25m | `pi05` + `adaptive_conformal_crm` K=2 norm=0.2 τ=0.25 / **long** | 42 | `eval_long_adaptive_pi05_seed42.json` | tmux 手动 nohup |

### 关键发现

1. **PID 42110 = cron 实验 pi05-adaptive-goal-s43-bjb1-18228 已实际在运行**。父进程链清楚显示其由 cron wrapper 启动（包含 `/tmp/agent-ml-exit/...exit` 退出码 trap、日志写到 `~/runs/acr-vla-conformal-refinement/pi05-adaptive-goal-s43-bjb1-18228.log`）。  
   ➡️ **registry 状态 PREPARING 与现实不符，应同步为 RUNNING**。

2. **GPU 0/1/3 的三个进程是手动 tmux nohup 启动**，不在 cron 系统里。父进程 cmdline 显示完整命令为 `source conda ... && nohup bash -c "CUDA_VISIBLE_DEVICES=N python -u src/evaluate.py ..."`，父 bash 已 PPid=1（脱离 tmux 后被 init 收养）。这三个是 11:45 左右从同一个 tmux session（`/tmp/tmux-0/default`）批量启动的 pi05 long 评估，**registry 里没有对应 RUNNING 记录是因为它们不走 cron**。

3. 进程都健康：CPU/GPU 利用率 24%-65%，显存 10-11GB，最新日志在持续输出 rollout 结果（如 GPU 3 跑到 `KITCHEN_SCENE8`，GPU 0 跑到 `LIVING_ROOM_SCENE1`），无错误。

4. `tmux ls`/`ps`/`pgrep` 被 ssh_read_only 白名单拦截，本次结论全部基于 `/proc/&lt;PID>/cmdline` + `/proc/&lt;PID>/status` + stat 时间。

### 建议（不执行，仅汇报）
- 把 `pi05-adaptive-goal-s43-bjb1-18228` 的 registry 状态改为 RUNNING（PID 42110，启动 14:45:50）。
- GPU 0/1/3 上的三个手动评估任务建议补登记到 registry，否则后续 cron 调度可能在这台机器上重复占卡。

---
