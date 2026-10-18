# diagnose eval pi05 l2norm k07 long seed46 strict w38

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_eval_pi05_l2norm_k07_long_seed46_strict_w38_20260528T070539_result.json`
- **Structured JSON:** [`fb6a2f94bfe4ae5b8aca.json`](../../sessions/fb/fb6a2f94bfe4ae5b8aca.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 诊断结果

### OOM 类型：GPU OOM（GPU 1 同卡 3 进程）

**证据：**

| 指标 | 值 |
|---|---|
| 系统 RAM | 1.0 TiB 总量，86 GiB 已用，914 GiB 可用 — **排除 CPU OOM** |
| GPU 1 显存 | 97,887 MiB 总量，当前 21,639 MiB 已用（被杀进程已消失） |
| GPU 1 当前进程数 | **2 个**（被杀后剩余） |

**崩溃时 GPU 1 上有 3 个进程并行：**

| PID | 实验 | 启动时间 | 单进程显存 |
|---|---|---|---|
| 253691 | random k=0.9 seed46 | 14:27 | ~10,743 MiB |
| 261885 | attention k=0.5 seed46 | 14:34 | ~10,861 MiB |
| **267278** (killed) | **l2norm k=0.7 seed46** | **14:38** | **~10,700 MiB (估)** |

稳态总计 ~32 GiB / 97 GiB，看起来有余量，但进程在 **Task 0 完成 → Task 1 加载的过渡期**被杀（日志最后一行是 Task 0 汇总）。任务切换时环境重建 + MuJoCo 渲染缓冲区分配会产生显存峰值，3 进程峰值叠加导致 OOM。

### 完成进度

**50 / 500 episodes（10%）** — 仅完成 Task 0，成功率 74.0%（37/50）。

### 当前 GPU 分配

| GPU | 显存占用 | 进程数 |
|---|---|---|
| 0 | 10,364 MiB | 1 (random k=0.95 seed45) |
| 1 | 21,639 MiB | 2 (random k=0.9 + attention k=0.5) |
| 2 | 10,306 MiB | 1 (random k=0.7 seed45) |
| 3 | 10,586 MiB | 1 (attention k=0.85 seed46) |

### 建议

- **可以重试**，但 **不能再放到 GPU 1** — 已有 2 个进程
- GPU 0/2/3 各只有 1 个进程（~10 GiB / 97 GiB），任选其一可安全跑第二个实验
- 每张 97 GiB 卡最多同时跑 **2 个** π0.5 eval 进程较安全，3 个有 OOM 风险

---
