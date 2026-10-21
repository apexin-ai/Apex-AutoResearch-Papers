# diagnose cqa1 full gpu check

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_cqa1_full_gpu_check_20260528T051855_result.json`
- **Structured JSON:** [`e51bf689a354a33f9046.json`](../../sessions/e5/e51bf689a354a33f9046.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## cqa1-33015 GPU 诊断汇总

| GPU | 实验 | 状态 | 结果 |
|-----|------|------|------|
| **cuda:0** | eval_pi05_l2norm_k05_long_seed45_strict_cqa1 (PID 981950) | **运行中** ~3h | GPU util 21%, 10346 MiB |
| **cuda:1** | eval_pi05_attn_k095_long_seed45_strict_cqa1 (PID 966040) | **运行中** ~3.2h | GPU util 47%, 10243 MiB |
| **cuda:2** | eval_pi05_random_k075_long_seed45_strict_cqa1 (PID 911227) | **已完成** ✅ | **SR=64.6%**, 239.2min, EXIT_CODE=0 |
| **cuda:3** | eval_pi05_l2norm_k09_long_seed45_strict_cqa1 (PID 913746) | **已完成** ✅ | **SR=80.0%**, 204.8min, EXIT_CODE=0 |

### 已完成实验 per-task 明细

**Random k=0.75 (cuda:2) — SR=64.6%**
T0=92%, T1=76%, T2=68%, T3=72%, T4=72%, T5=40%, T6=62%, T7=74%, T8=10%, T9=80%

**L2norm k=0.9 (cuda:3) — SR=80.0%**
T0=94%, T1=100%, T2=88%, T3=100%, T4=84%, T5=90%, T6=16%, T7=90%, T8=48%, T9=90%

两个已完成实验已 update_registry（conclusion=success, metrics 已写入）。GPU 2/3 现在空闲可用。GPU 0/1 预计还需 ~1h 完成。

---
