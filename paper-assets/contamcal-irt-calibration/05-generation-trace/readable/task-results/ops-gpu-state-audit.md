# ops gpu state audit

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_gpu-state-audit_20260515T133236_result.json`
- **Structured JSON:** [`3725b2923b9d25da1890.json`](../../sessions/37/3725b2923b9d25da1890.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

审计完成。结果：

**cuda:2 冲突已确认** — 两个进程共享 GPU 2：
- PID 553256 (exp_008 eval, 3612 MiB) 先启动
- PID 555936 (exp_001 SFT 3B d005, 19316 MiB) 后启动 27 分钟
- 合计 22928 / 24564 MiB，GPU 100% 利用率，两者在抢算力

**2 个进程已死：**
- PID 549858 (exp_001_sft_15B_d005_s123_v2) → cuda:1 空闲
- PID 549516 (exp_001_sft_15B_d025_s123_v2) → cuda:0 空闲

**仍在运行：**
- cuda:3: PID 551219 (3B d000 eval), 2h20m
- cuda:4: PID 556016 (3B d025 SFT), 1h34m
- cuda:5: PID 551290 (3B d005 eval), 2h20m
- CPU: PID 528993 (extreme gamma sim), 4h57m

**空闲 GPU：cuda:0, cuda:1**

报告已保存至 `artifacts/gpu_audit_20260515T1330.md`。

---
