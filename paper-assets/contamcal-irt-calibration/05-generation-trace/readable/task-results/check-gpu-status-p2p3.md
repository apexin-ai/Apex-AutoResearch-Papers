# check gpu status p2p3

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_gpu_status_p2p3_20260516T143219_result.json`
- **Structured JSON:** [`2a1271bdf000e1404bc6.json`](../../sessions/2a/2a1271bdf000e1404bc6.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 状态汇总

### P2: D108 v4 — MMLU domain gamma N=24 (PID 789935, CPU)

**已完成 6/8 个域：**

| Domain | 完成时间 |
|--------|---------|
| STEM_Math | 19:41 |
| STEM_Science | 19:57 |
| STEM_CS_Eng | 20:01 |
| Medical | 20:20 |
| Humanities | 22:12 |
| Social_Sciences | 22:31 |

**当前正在跑：Business_Law** — MCMC 4 chains 刚启动，warmup 5% (100/2000)，~1.5 it/s。

**剩余：** Business_Law（进行中）+ Other。按每域 ~19 分钟估算，**预计 ~35-40 分钟完成全部 8 域**。

---

### P3: cuda:4 — Llama-3.2-3B d000 s42 eval (PID 785955)

- **GPU:** 8313MiB / 24564MiB，86% 利用率
- **运行时间:** 1h14m
- **日志异常：** `/tmp/llama3b_d000_eval.log` 显示 GSM8K 评估在 57/1319 处出现 `Terminated`，但进程仍在运行且 GPU 利用率正常。可能是日志缓冲问题——tqdm 输出未刷新到文件。进程本身（`evaluate.py --benchmarks mmlu gsm8k arc_challenge humaneval`）活跃。

### P3: cuda:5 — Qwen2.5-1.5B-Instruct eval (PID 786898)

- **GPU:** 3659MiB / 24564MiB，55% 利用率
- **运行时间:** 1h08m
- **进度：** GSM8K 1251/1319 (95%)，~2.5s/it
- MMLU 已完成。GSM8K **预计 ~3 分钟完成**，之后还需跑 arc_challenge 和 humaneval。

---
