# check experiment progress all

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_experiment-progress-all_20260515T140231_result.json`
- **Structured JSON:** [`e1e7df3cd08a629ce3b0.json`](../../sessions/e1/e1e7df3cd08a629ce3b0.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 实验状态报告 (2026-05-15 ~22:05 Beijing / ~14:05 UTC)

---

### 1. repo-level-cls-8b-s42-resume (cuda:1, PID 295794)
| 项目 | 值 |
|------|-----|
| 当前 step | **5361 / 6633 (80.8%)** |
| Loss | 0.2286 @ step 5350, eval_loss 0.4021 @ step 5200 |
| 速度 | ~8.2 s/step |
| 最新 checkpoint | **checkpoint-5200** (21:40 Beijing) |
| 进程状态 | **running** — 16h14m uptime, 100% CPU, 4.1GB RSS |
| GPU 利用率 | **96%**, 27313/32607 MiB |
| 预估完成 | **~17:00 UTC May 15** (~01:00 Beijing May 16) |

---

### 2. cwm8b-ckpt400-test-eval (cuda:3, PID 367292)
| 项目 | 值 |
|------|-----|
| 当前样本 | **272 / 9784 (2.8%)** |
| Running accuracy | **70.2%** |
| 速度 | ~23 s/sample |
| 产出 | `results_incremental.jsonl` (969KB) |
| 进程状态 | **running** — 1h46m uptime (wrapper PID, python 子进程在跑) |
| GPU 利用率 | **51%**, 17003/32607 MiB |
| 预估完成 | **~May 18 03:00 UTC** (~60h remaining, 非常慢) |

**注意**: 2.8% 进度 + 23s/sample 意味着需要 ~60 小时才能跑完。这个速度异常慢。

---

### 3. repo-level-cwm-8b-conda (cuda:2, PID 266816)
| 项目 | 值 |
|------|-----|
| 当前 step | **~4700 / 6633 (~70.9%)** — 正在跑 eval (5728/9335) |
| 最新 checkpoint | **checkpoint-4600** (21:32 Beijing) |
| 速度 | ~39 min / 100 steps (含 eval) |
| 进程状态 | **running** — 20h18m uptime, 100% CPU, 5.0GB RSS |
| GPU 利用率 | **95%**, 30733/32607 MiB |
| 预估完成 | **~03:00 UTC May 16** (~11:00 Beijing May 16) |

**注意**: 日志文件实际是 `repo-level-cwm-8b-conda-v2.log`，不是 `repo-level-cwm-8b-conda-v4.log`（后者 5月13日已停更）。cmdline 显示 `--device cuda:0`，通过 CUDA_VISIBLE_DEVICES 映射到物理 GPU 2。

---

### nvidia-smi 全卡概览

| GPU | 利用率 | 显存 | 用途 |
|-----|--------|------|------|
| 0 | **16%** | 18931/32607 MiB | 空闲/轻负载 |
| 1 | **96%** | 27313/32607 MiB | cls-8b-s42-resume 训练 |
| 2 | **95%** | 30733/32607 MiB | cwm-8b-conda 训练 |
| 3 | **51%** | 17003/32607 MiB | cwm8b-ckpt400 eval |

---
