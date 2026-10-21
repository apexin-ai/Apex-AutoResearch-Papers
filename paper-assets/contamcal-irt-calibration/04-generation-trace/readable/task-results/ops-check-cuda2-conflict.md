# ops check cuda2 conflict

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_check-cuda2-conflict_20260515T134036_result.json`
- **Structured JSON:** [`7804d840157c5f77f4f8.json`](../../sessions/78/7804d840157c5f77f4f8.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**exp_008 eval 状态：**

- **PID 553256 仍在运行**，已用时 2h10m
- 当前正在跑 **GSM8K：1200/1319 (91%)**，速度 ~7.5s/it
- **MMLU 已完成**（14042 items，约 ~78it/s 跑完）
- GSM8K 剩 119 items → **~15 min**
- 之后还有 **arc_challenge** + **humaneval** 未跑

**预估剩余时间：**
- GSM8K 收尾：~15 min
- arc_challenge（~1200 MC items，速度接近 MMLU）：~15 min
- humaneval（~164 items，生成式，速度接近 GSM8K）：~20 min
- **总计约 45-50 min**

**cuda:2 状态：** 22.9GB/24.6GB 使用中，GPU util 100%。两个进程共存：
- PID 553256 (exp_008 eval): 3.6GB
- PID 555936 (3B d005 SFT): 19.3GB

---
