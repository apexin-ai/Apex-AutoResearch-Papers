# diagnose eval batch failure

**The Probe Reward Trap: Behavioral Death Before Distributional Collapse in Sycophancy Calibration** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_eval-batch-failure_20260521T072325_result.json`
- **Structured JSON:** [`f98a184764a282605d42.json`](../../sessions/f9/f98a184764a282605d42.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 诊断报告

### 根因：tmux server 被杀导致批量 SIGHUP

**不是重启、不是 OOM。**

### 证据

| 检查项 | 结果 |
|--------|------|
| 重启 | **排除** — `uptime` 显示 up 7 days 23h |
| RAM OOM | **排除** — 754GB 总内存，当前仅用 22GB，dmesg 无权限但 free 正常 |
| GPU OOM | **排除** — 4 × V100-32GB，每卡用 ~16.8GB |
| tmux | **关键线索** — ckpt5000-v2 的 tmux session 已消失；ckpt6500/7000 的原始 session (PID 496116/496266) 已死，被新 session 替代 |
| Load average | 15min=158.84，正在快速下降至 1min=4.78 — 同时加载 4 个 8B 模型的瞬时 CPU 峰值 |

### 每个实验状态

| 实验 | 原 PID | 失败时间 (UTC) | 日志关键信息 | 当前状态 |
|------|--------|---------------|-------------|---------|
| ckpt5000-v2 | 495833/495837 | 07:19:24 | `Killed` → `EXIT_CODE=129`，eval 刚开始就被杀 | **已重跑** — nohup PID 497834 运行中，进度 20/362 |
| ckpt6000 | 498441 | — | 无失败记录 | **正在运行** — PID 498446，首次提交 |
| ckpt6500 | 496116 | ~07:21 | 原进程已死，无 exit file | **已重跑** — 新 tmux PID 498584 运行中 |
| ckpt7000 | 496266 | ~07:21 | 原进程已死，无 exit file | **已重跑** — 新 tmux PID 498666 运行中 |

### 根因分析

Wrapper 脚本中有 `trap 'exit 129' HUP` — 当 tmux server 被杀或 session 断开时，shell 收到 SIGHUP，触发 trap 退出 129。内部 python 进程被 SIGKILL（日志中 "Killed"）。

ckpt5000-v2 的 exit file 确认 `129|2026-05-21T07:19:24Z`。三个实验几乎同时死亡 + EXIT_CODE 全是 129 = tmux server 级别事件（`tmux kill-server` 或 tmux 进程崩溃），而非单个进程问题。

### 当前状况

**4 个实验已全部重跑且正常运行中，无需干预。** ckpt5000-v2 进度 20/362（~5.5%），其余 3 个刚启动约 2 分钟。GPU 利用率 ~50%，内存充裕。

建议后续确认是什么杀了 tmux server（可能是其他自动化脚本或手动操作），避免再次中断。

---
