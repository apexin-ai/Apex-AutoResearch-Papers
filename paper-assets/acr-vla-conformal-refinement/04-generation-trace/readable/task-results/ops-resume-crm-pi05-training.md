# ops resume crm pi05 training

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_resume-crm-pi05-training_20260524T204106_result.json`
- **Structured JSON:** [`4ee234087de96df1593d.json`](../../sessions/4e/4ee234087de96df1593d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

任务前提不成立，**训练并未死亡**，正在 epoch 28/50 活跃训练中。无需 resume。

## 实际状态

**train-crm-pi05-unified-3suite-r2 仍在运行**：
- PID 326315 存活（被孤儿化到 init，PPID=1），CUDA_VISIBLE_DEVICES=0
- 日志 `/root/runs/acr-vla-conformal-refinement/train-crm-pi05-unified-3suite-r2.log` 04:41:57 仍在写入
- 当前进度：epoch 28/50, batch 400/684
- best val_loss 已刷到 **0.004690 (epoch 27)**，优于任务描述的 0.004790 (epoch 25)
- checkpoint 已存到 epoch 27

**误解来源**：日志里的 `bash: line 1: 326314 Killed timeout 43200 ...` 是 12 小时 timeout 杀掉了**外层 bash wrapper (PID 326314)**，但内层 Python 子进程 (PID 326315) 没被信号传播到，继续作为孤儿进程运行——所以训练实际上没中断。

**剩余时长估算**：epoch 26→27 用 ~22 分钟，剩 22 epoch ≈ 8 小时。

## GPU 占用
- GPU 0: 训练 (PID 326315) — 当前采样 8% util（在 val/save 间隙）
- GPU 1/2: 两个 eval 进程 (norm005 obj/goal)
- GPU 3: PID 114507 precompute pi05 long benchmark，9883 MiB / 24% util — **不是僵尸**，在工作

## 建议
**不要提交新 r3 训练**——会和正在跑的 r2 抢 GPU 0。让 r2 自然跑完到 epoch 50（约 8 小时后）。如果担心再次 timeout，可以做的是：进一步用 `disown` 或 systemd 脱离 session（但目前进程已经孤儿化，不会再被 session 关闭影响）。

需要我做什么？继续观察、注册 artifact、还是其他动作？

---
