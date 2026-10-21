# monitor comprehensive status check

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_monitor_comprehensive_status_check_20260521T142137_result.json`
- **Structured JSON:** [`04d018cf0a9df1c8d495.json`](../../sessions/04/04d018cf0a9df1c8d495.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 综合状态报告

### Seed 7 (westd GPU 0,1) — W&B: p6vwsrfk

| 项目 | 状态 |
|------|------|
| 进程 | **ALIVE** (PID 226699, uptime ~2h) |
| 当前 step | **Step 5** (已完成 step 4, 进度 27%, 4/15) |
| GPU 内存 | GPU 0: 97207/97887 MiB (99.3%), GPU 1: 97207/97887 MiB (99.3%) |
| Step 5 backward | **已通过** — checkpoint 已成功保存至 global_step_5 (22:09) |
| OOM 风险 | **低** — 虽然内存占用 99.3% 极高，但已稳定通过 5 个 step 的 backward+save，内存未持续增长 |
| Step 4 关键指标 | train success=1.0, pass@8=1.0, critic/score=6.95, entropy_loss=0.062 |
| 速度 | ~797s/step (~13.3 min), 预计剩余 ~2.2h 完成 |

### Seed 5 OOD eval (westd GPU 3) — W&B: u4zste0d

| 项目 | 状态 |
|------|------|
| 进程 | **ALIVE** (PID 383150, uptime ~19 min) |
| GPU 内存 | GPU 3: 90469/97887 MiB (92.4%) |
| W&B | state=running, **尚无指标** 写入 |
| 状态 | **进行中** — 模型已加载，W&B 已初始化，正在执行 134 episodes AlfworldSG_OOD 的 val rollouts |

还在跑，尚无结果。

### Seed 4 (bjb1 GPU 0,1) — W&B: fb1o765g

| 项目 | 状态 |
|------|------|
| 进程 | **ALIVE** (PID 302056, uptime ~5h40m) |
| 当前 step | **Step 10** (_step=10, 进度 67%, 10/15) |
| GPU 内存 | GPU 0: 20731/97887 MiB (21.2%), GPU 1: 同 |
| W&B 指标 | critic/score/mean=3.83, actor/kl_coef=0.01, entropy_loss=0.04 |
| Checkpoint | global_step_10 已保存 (21GB) |
| 磁盘 | 222/250GB (89%), **剩余 29GB** — 需关注，后续 checkpoint 可能不够 |

**磁盘风险提醒**: Seed 4 checkpoint 已占 21GB，剩余 29GB。max_actor_ckpt_to_keep=3 + max_critic_ckpt_to_keep=1，如果每个 checkpoint ~21GB，3 个 actor checkpoint 就 63GB，可能超限。但 save_freq=5，已有 step 10，下次保存 step 15（最终），旧 checkpoint 会被清理，勉强够用。

---
