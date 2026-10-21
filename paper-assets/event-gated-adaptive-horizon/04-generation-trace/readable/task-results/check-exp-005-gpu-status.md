# check exp 005 gpu status

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_exp_005_gpu_status_20260513T173757_result.json`
- **Structured JSON:** [`083a41dc3086bc21a9f6.json`](../../sessions/08/083a41dc3086bc21a9f6.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 结果

### exp_005 (event-gated v5, cuda:1)
- **进程**: PID 51721 存活，运行 1h30m
- **当前 step**: **40000**（35 分钟前是 ~16K，增长了 24K 步）
- **eval_return@35K**: **290.8**（15K 时 153.9 → 35K 时 290.8，几乎翻倍）
- **train_return@40K**: 226~360 区间（均值 ~299）
- **FPS**: 7.3
- **GPU 1**: 利用率 13%，显存 4173/97887 MiB，温度 43°C

### exp_001 (baseline, cuda:0)
- **进程**: PID 9409 存活，运行 15h34m，CPU 1131%
- **GPU 0**: 利用率 41%，显存 4165/97887 MiB，温度 40°C

### 结论

exp_005 健康推进中，step 从 16K 大幅增长到 40K，reward 持续上升。GPU 利用率 13% 偏低但 FPS 7.3 稳定——这是 DreamerV3 的正常模式（环境交互 + 模型训练交替，GPU 不会持续满载）。baseline 的 41% 利用率也印证了这一点。**无异常。**

---
