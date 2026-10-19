# monitor bjb1 status check

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_monitor_bjb1-status-check_20260515T031524_result.json`
- **Structured JSON:** [`af6f8f97abf05a4a51a5.json`](../../sessions/af/af6f8f97abf05a4a51a5.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## Part 1: bjb1-18228 Spatial Eval 进度

所有 4 个进程均存活。

| 实验 | PID | 运行时间 | Tasks Done | 当前成功率 | vs 上次快照 |
|------|-----|---------|------------|-----------|------------|
| **eval-argmin-only-spatial** (reconvla) | 231421 | 9h28m | **8/10** | **37.5%** (30/80) | 无变化，正在跑 task 9 |
| **eval-acr-spatial-v4-small** (perdof, norm=0.1) | 253085 | 6h46m | **5→6/10** (task 6 进行中) | **42%** (21/50 已完成) | task 6 进行中：0/5 after 5 rollouts |
| **eval-acr-spatial-v4-obs-only-r2** (obs_only, norm=0.1) | 270097 | 4h54m | **4→5/10** | **48%** (24/50) | +1 task (T5=10%), 率从 57.5%→48% |
| **eval-acr-spatial-v4-scalar** (scalar, norm=0.1) | 288939 | 1h41m | **2/10** | **80%** (16/20) | 无变化 |

已完成 task 明细（有变化的标 **new**）：

**argmin-only (reconvla)** — 8 tasks done:
| Task | Rate |
|------|------|
| between_plate_and_ramekin | 60% |
| next_to_ramekin | 100% |
| from_table_center | 0% |
| on_cookie_box | 30% |
| in_top_drawer | 10% |
| on_ramekin | 10% |
| next_to_cookie_box | 90% |
| on_stove | 0% |

**obs-only-r2** — 新完成 T5：
| Task | Rate |
|------|------|
| between_plate_and_ramekin | 90% |
| next_to_ramekin | 100% |
| from_table_center | 0% |
| on_cookie_box | 40% |
| **in_top_drawer** | **10%** ← new |

---

## Part 2: bjb1-32546 未注册实验

两个进程都存活，都是 **VLA-only baseline**（无 CRM）跑 **object benchmark**：

| 项目 | PID 17222 (cuda:4) | PID 18808 (cuda:5) |
|------|--------------------|--------------------|
| **模式** | vla_only, baseline_mode=**single** | vla_only, baseline_mode=**mean** |
| **K** | 1 | 10 |
| **运行时间** | 17 min | 15 min |
| **output_file** | `logs/eval_object_vla_only.json` | `logs/eval_object_vla_mean.json` |
| **日志路径** | `/root/acr-vla-conformal-refinement/logs/eval_object_vla_only.log` | `/root/acr-vla-conformal-refinement/logs/eval_object_vla_mean.log` |
| **进度** | 1/10 tasks done (T1=0%), T2 进行中 (1/5 after 5 rollouts) | 0/10, 刚加载完环境 |
| **完整命令** | `python -u src/evaluate.py --benchmark object --mode vla_only --baseline_mode single --n_rollouts 10 --K 1 --output_file logs/eval_object_vla_only.json` | `python -u src/evaluate.py --benchmark object --mode vla_only --baseline_mode mean --n_rollouts 10 --K 10 --output_file logs/eval_object_vla_mean.json` |
| **其他参数** | seed=42, max_steps=300 | seed=42, max_steps=300, CUDA_VISIBLE_DEVICES=5, HF_HUB_OFFLINE=1 |

注意：`eval-acr-spatial-v4-default-r2.log` (bjb1-18228) 记录了一个已失败的 job（`python: command not found`, EXIT_CODE=127），不是当前运行的 PID 253085。PID 253085 的实际日志在 `/root/autodl-tmp/logs/eval_acr_spatial_v4_small.log`。

---
