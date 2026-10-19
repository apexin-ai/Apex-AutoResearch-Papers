# check cqa1 32758 gpu status

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_cqa1-32758-gpu-status_20260525T082614_result.json`
- **Structured JSON:** [`54fc4f959e5f104eb839.json`](../../sessions/54/54fc4f959e5f104eb839.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## cqa1-32758 状态汇总

### GPU 状态（6 × ~24GB）
全部空闲：GPU 0-5 占用 0 MiB / 利用率 0%，无 compute 进程。

### 进程
无 `evaluate.py` / `train_crm` 进程在跑。只有系统服务（supervisord/sshd/jupyter-lab/tensorboard/autopanel）。tmux 工具被白名单屏蔽，但 `ps aux` 无 tmux 会话痕迹。

### Uptime / 重启
PID 1 (`boot.sh`) 已运行 4h03m → **容器约 4 小时前重启过**（约 12:08 之后）。`/proc/uptime` 显示 ~161 天是宿主机时钟，容器是新启的。

### 中断的实验（被重启杀掉）
`/root/autodl-tmp/logs/` 下 6 个日志在 12:02-12:08 时间窗内全部停止，**全部卡在同一位置**：第 5 个任务 `pick_up_the_black_bowl_in_the_top_drawer...` 的 rollout 15/20。说明 6 个并行任务被同步终止。

| 日志 | 已完成任务 | 进度（task 5） |
|---|---|---|
| eval-k2-adaptive-spatial-s42 | 4/10 (95/95/100/95) | rollout 15/20, 12/15 |
| eval-k2-adaptive-spatial-s43 | 4/10 (95/100/100/100) | rollout 15/20, 12/15 |
| eval-k2-adaptive-spatial-s44 | 4/10 (95/95/100/95) | rollout 15/20, 12/15 |
| eval-vla-only-spatial-cqa1-s42 | 4/10 (95/90/95/85) | rollout 15/20, 11/15 |
| eval-vla-only-spatial-cqa1-s43 | 4/10 (85/100/95/90) | rollout 15/20, 11/15 |
| eval-vla-only-spatial-cqa1-s44 | 4/10 (95/95/90/95) | rollout 15/20, 11/15 |

### JSON 收割
近 180 分钟内 `/root/autodl-tmp/logs/` **无新 JSON 输出**——6 个被中断的任务都没来得及写最终结果文件，需要重跑。`/root/acr-vla-conformal-refinement/logs/` 下的 JSON 都是 5/25 之前批次的旧产出。

### 结论
- 6 张 GPU 全部空闲，可立即下发新任务
- 12:08 左右的容器重启把 6 个 spatial eval（3 × k2-adaptive + 3 × vla-only，s42/43/44）打断在 task 5 rollout 15/20，需要重跑
- 没有需要收割的新 JSON

---
