# diagnose phase1 oft baseline

**afford invar** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_phase1_oft_baseline_20260520T003041_result.json`
- **Structured JSON:** [`41d91f1684c585645ab9.json`](../../sessions/41/41d91f1684c585645ab9.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 诊断结论

- **根因**: 进程被 SIGTERM (signal 15) 杀死。父 tmux session 收到 SIGHUP（EXIT_CODE=129=128+1），随后向子进程发送 SIGTERM。典型原因是 SSH 连接断开或 tmux session 被销毁。
  
- **训练进度**: 跑到了 step **4882/20000**（24%），速度 ~4.3 it/s，已训练约 21 分钟。

- **额外问题**: 日志开头显示第一次启动因 **port 29503 EADDRINUSE** 立即失败（端口被其他 torchrun 进程占用），之后才成功启动第二次。说明提交任务时端口有冲突。

- **是否产生了有用的 checkpoint**: **否**。运行目录 `/root/autodl-tmp/afford_invar/runs/openvla-7b+libero_goal_no_noops+b2+lr-0.0005+lora-r32+dropout-0.0--image_aug/` 仅有 `dataset_statistics.json`，无任何 checkpoint。尽管 `save_freq=500` 应在 step 500 时保存第一个 checkpoint，但4882 步无一保存——可能是 finetune.py 的 save 逻辑有延迟或条件未触发。

- **磁盘空间**: 数据盘 41% 使用（208GB 剩余），不是问题。

- **建议**: 
  1. 值得重试。需确保 tmux session 稳定不会被意外终止（检查是否有 cron job 在清理 tmux sessions）。
  2. 重试时换一个 `--master_port`（如 29504）避免端口冲突，或在启动前先 kill 占用端口的进程。
  3. 排查 checkpoint 未保存的问题——检查 finetune.py 中 save 逻辑是否需要额外参数（如 `--exp_name` 或 `--adapter_tmp_dir`），确认 save_freq 参数确实被正确传入。

---
