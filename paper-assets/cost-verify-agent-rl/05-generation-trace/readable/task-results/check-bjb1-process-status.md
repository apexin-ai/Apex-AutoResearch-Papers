# check bjb1 process status

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_bjb1_process_status_20260519T131235_result.json`
- **Structured JSON:** [`f42f1bd1bfb0d0709f64.json`](../../sessions/f4/f42f1bd1bfb0d0709f64.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 报告

### 1. nvidia-smi

```
GPU 0: NVIDIA RTX PRO 6000 (96GB) — 0MiB 使用, 0% 利用率, 29°C
GPU 1: NVIDIA RTX PRO 6000 (96GB) — 0MiB 使用, 0% 利用率, 28°C
无 GPU 进程运行。
```

两张 GPU 完全空闲。

### 2. Python/训练相关进程

无训练或 eval 进程。仅有系统级后台服务：
- **TensorBoard** (PID 911) — 监听 0.0.0.0:6007，自 May 13 运行
- **JupyterLab** (PID 914) — 自 May 13 运行
- **HTTP server** (PID 96086) — `python -m http.server 18923`，在 `/root/autodl-tmp/expert_sft`，自今日 11:45 运行

### 3. per-task-type eval 进程

**未发现。** 没有任何 eval/per-task/breakdown 相关进程在运行。如果之前提交过，已经结束或被重启中断。

### 4. tmux sessions

无 tmux sessions。

### 5. 最近日志

最新活动在 `2026-05-19` 目录下。最新 wandb run (`run-20260519_195545-qtxhh5ak`) 的最后日志时间为 **19:58:13**（约 1 小时前），内容是 AlfworldSG validation generation 完成（耗时 145 秒）。该进程已结束，无遗留。

### 结论

服务器空闲，两张 GPU 可用，无训练/eval 进程运行，无 tmux session。8b_sft_clean_eval_v2 无遗留进程。per-task-type breakdown eval 未在运行。

---
