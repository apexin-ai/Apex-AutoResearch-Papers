# monitor westd progress check

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_monitor_westd-progress-check_20260515T171533_result.json`
- **Structured JSON:** [`8e4e9a3fef876109f03a.json`](../../sessions/8e/8e4e9a3fef876109f03a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 实验进度报告

### GPU 状态
| GPU | Util | VRAM | 任务 |
|-----|------|------|------|
| 0 | 0% | 0/32607 MiB | **空闲** (val-sweep 已死) |
| 1 | 98% | 27313/32607 MiB | cls-8b-s42-resume |
| 2 | 96% | 30733/32607 MiB | cwm-8b-conda-v4 |
| 3 | 89% | 22527/32607 MiB | cwm8b-ckpt400-test-eval |

### 进程状态
PID 388791 (val-sweep) 不在进程列表中，其余 3 个进程均存活 (CPU 100%)。

---

### 1. repo-level-cls-8b-s42-resume (PID 295794, cuda:1) — 正常
- **Step: 6262/6633 (94.4%)**，上次 4041 → 进展显著
- Loss: 0.0474 (step 6250), eval_loss: 0.4385 (step 6200)
- Speed: ~8.1s/step
- 剩余 371 steps × ~8.1s ≈ **50 min**
- **ETA: ~02:10 UTC May 16**
- Step 6200 刚完成 checkpoint 保存和 eval

### 2. repo-level-cwm-8b-conda-v4 (PID 266816, cuda:2) — 正常
- **Training step: ~5300+/6633 (~80%)**，上次 4013 → 进展显著
- 当前正在 eval (2909/9335, ~31%)，eval 触发于 step 5200+ 附近
- Loss: 0.0057 (step ~5300), eval_loss: 0.5038 (step 5200)
- Speed: ~12.2s/step training
- 剩余约 1200-1300 training steps + 若干次 eval（每次 ~20min）
- **ETA: ~05:00-06:00 UTC May 16**

### 3. cwm8b-ckpt400-test-eval (PID 381618, cuda:3) — 正常但慢
- **Progress: 1704/9784 (17.4%)**，new=1345 + resumed=359
- Running accuracy: **65.5%**
- Speed: ~8.5 samples/min (与预期一致)
- 剩余 8080 samples / 8.5 per min ≈ **15.8 hours**
- **ETA: ~17:10 UTC May 16** (比之前预估的 09:20 晚很多，原始 ETA 似乎有误)

### 4. cls8b-s42-resume-val-sweep (PID 388791, cuda:0) — 已死
- **进程被 Terminated**，GPU 0 完全空闲
- 仅完成 **1/21 checkpoints** (checkpoint-1800 done)
- checkpoint-2000 评估到 5120/9335 (54.9%, acc=82.7%) 时被杀
- **需要重启**，GPU 0 当前闲置可用

---

### 整体摘要
- 3/4 任务正常运行。cls-8b 即将完成（~50min），cwm-8b 还需约 4-5 小时。
- cwm8b-test-eval 速度正常但总量大，实际完成时间在 May 16 17:00 UTC 左右。
- **val-sweep 已挂，GPU 0 空闲，需要决定是否重启。**

---
