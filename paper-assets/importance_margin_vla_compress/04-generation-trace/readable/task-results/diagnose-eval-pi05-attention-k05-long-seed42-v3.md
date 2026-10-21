# diagnose eval pi05 attention k05 long seed42 v3

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_eval_pi05_attention_k05_long_seed42_v3_20260526T151912_result.json`
- **Structured JSON:** [`d08a99a8c633745992e0.json`](../../sessions/d0/d08a99a8c633745992e0.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

诊断完成。

**根因：EGL/MuJoCo 渲染驱动层静默崩溃**，非 OOM、非磁盘、非代码 bug。

核心证据：
- cgroup `oom_kill=0`，系统 RAM 940GB 可用，GPU 显存 10.5/24GB — 排除所有内存原因
- 同样的静默死亡（~30 行日志后无 traceback 消失）出现在 l2norm_k075、l2norm_k0925 等不同配置的实验中 — 非特定于 attention 剪枝
- 重试有时成功 — 间歇性故障，符合 EGL driver 在多进程并发下的已知不稳定性
- 4 个 GPU 全部同时运行 eval（均 `MUJOCO_GL=egl`），driver 资源争用

**可以重试**，但 cuda:2 当前被 PID 467731（random k0.7 eval）占用，需等其完成。建议降低并发到 2-3 个以减少崩溃频率。

报告已写入 `artifacts/diag_eval_pi05_attention_k05_long_seed42_v3.md`。

---
