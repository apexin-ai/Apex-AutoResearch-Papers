# ops gpu health check

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_gpu-health-check_20260515T124252_result.json`
- **Structured JSON:** [`ae3706e293aee4bf6cd0.json`](../../sessions/ae/ae3706e293aee4bf6cd0.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部 8 个进程存活，无异常。

**摘要：**
- **6 张 GPU 全部在用**，温度/功耗正常（最热 GPU4 71°C）
- **1.5B SFT** (cuda:0, cuda:1)：运行 1h38m，进度未从日志中单独提取（非指定任务）
- **3B d005 SFT** (cuda:2)：step 715/3177 (22.5%)，loss ~1.1，ETA ~2h35m
- **3B d025 SFT** (cuda:4)：step 893/3384 (26.4%)，loss ~1.15，ETA ~2h05m
- **0.5B base eval** (cuda:2)：MMLU 完成，GSM8K 52%，还剩 arc_challenge + humaneval，总计 ~2.5–3h
- **3B d000 eval** (cuda:3)：MMLU 完成，GSM8K 51%，~2.5–3h 剩余
- **3B d005 s42 eval** (cuda:5)：MMLU 完成，GSM8K 49%，~3h 剩余
- **gamma sweep** (CPU)：运行 4h07m，持续中

报告已写入 `artifacts/gpu_health_check_loop10.md`。

---
