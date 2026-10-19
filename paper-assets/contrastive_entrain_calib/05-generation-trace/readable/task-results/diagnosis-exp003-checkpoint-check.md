# diagnosis exp003 checkpoint check

**The Probe Reward Trap: Behavioral Death Before Distributional Collapse in Sycophancy Calibration** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnosis_exp003-checkpoint-check_20260520T042103_result.json`
- **Structured JSON:** [`a066669e53b7a77e5c5d.json`](../../sessions/a0/a066669e53b7a77e5c5d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全貌清楚了。实际上有**两个独立进程**在运行。汇报如下：

---

## exp-003 状态汇报

### 1. 两个进程在跑

| | 原始 run (PID 70649) | s2 run (PID 237437) |
|---|---|---|
| 脚本 | `run_exp003_r3only.py` | `run_exp003s2_r3only.py` |
| GPU | GPU 1 (38152 MiB) | GPU 0 (38040 MiB) |
| 运行时长 | 1天11小时30分 | 4小时5分 |
| 当前 step | 4000+（无法确认确切位置） | 316/8000 |

### 2. Checkpoint 列表（原始 run，`/root/autodl-tmp/checkpoints/exp003_r3only_seed1/`）

| checkpoint | 保存时间 |
|---|---|
| checkpoint-500 | May 19 04:49 |
| checkpoint-1000 | May 19 08:37 |
| checkpoint-1500 | May 19 12:38 |
| checkpoint-2000 | May 19 17:04 |
| checkpoint-2500 | May 19 20:44 |
| checkpoint-3000 | May 20 00:21 |
| checkpoint-3500 | May 20 03:58 |
| **checkpoint-4000** | **May 20 08:29** |

**checkpoint-4500 不存在。** 按之前每500步 ~4小时的节奏，4500 应该在 ~12:30 出现，但目前没有。

### 3. 日志状态

- **原始 run**：stdout 指向 pipe（tee 管道），用户之前看到的 step 3760 stale 日志就是因为**管道缓冲**——训练实际已到 4000+ 并保存了 checkpoint，但日志输出被 buffered。
- **s2 run**：`/root/runs/contrastive_entrain_calib/exp-003-s2.log` 最后修改 12:22:36（刚刚），step 316/8000，~31s/step，正在正常推进。
- **exp003_restart.log**：一次失败的重启尝试，OSError 加载不了 `deberta-v3-base` 就 crash 了。

### 4. GPU 利用率

两张卡此刻均为 **0%**（nvidia-smi 是快照）。GRPO 训练在 reward 计算阶段（NLI 模型推理等）是 CPU-bound 的，GPU 可能短暂空闲，不代表卡住。

### 5. 诊断结论

- **原始 run (PID 70649)**: 进程存活、状态 R (running)，但 checkpoint-4000 之后已 ~4 小时未出新 checkpoint（预期 ~4h 出一个）。**可能卡住了**——GPU 0% + 无新 checkpoint 是警示信号。建议手动检查它是否还在出 step（用 `strace -p 70649` 看系统调用，或等 30 分钟看 checkpoint-4500 是否出现）。
- **s2 run (PID 237437)**: 正常运行，step 316/8000，~31s/step，日志实时更新。按当前速度跑完约需 66 小时。
- 日志 stale 的原因是**管道缓冲**（stdout → pipe → tee），不是训练卡住（当时训练确实在推进）。

---
