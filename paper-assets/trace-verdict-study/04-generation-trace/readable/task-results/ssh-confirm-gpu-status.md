# ssh confirm gpu status

**Trace Verbosity Degrades SFT Verdict Prediction: A Case Study in Information Density Effects** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_confirm_gpu_status_20260515T144614_result.json`
- **Structured JSON:** [`f59979d5576b63e9b534.json`](../../sessions/f5/f59979d5576b63e9b534.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 报告

### GPU 0 (cuda:0) — deepseek_full_trace_seed42

| 指标 | 值 |
|------|-----|
| 显存 | 93,958 MiB / 97,887 MiB (96%) |
| Utilization | 100% |
| 温度 | 73°C, 475W |

**问题：GPU 0 上有两个 full_trace 进程在跑，互相竞争资源：**

| PID | 运行时间 | 说明 |
|-----|---------|------|
| 111481 | 1h07m | **孤儿进程**，可能来自之前的提交 |
| 112299 | 59m | 当前 wrapper (PID 112289) 的子进程 |

两个进程各占 ~22GB 显存，写同一个 output_dir。训练进度：step 126/444 (28%)，~35s/step，预计还需 ~3h08m。

### GPU 1 (cuda:1) — deepseek_exception_only_seed42

| 指标 | 值 |
|------|-----|
| 显存 | 22,423 MiB / 97,887 MiB (23%) |
| Utilization | 100% |
| 温度 | 67°C, 469W |
| PID | 107198 (子进程 of wrapper 107188) |

训练进度：step 373/444 (84%)，~13.7s/step，**预计 ~16 分钟后完成训练**，之后会自动跑 eval。

### 需要处理

GPU 0 的孤儿进程 PID 111481 应该 kill 掉——它和当前 full_trace 任务写同一个 checkpoint 目录，会互相干扰，且白白占用 22GB 显存。是否 kill？

---
