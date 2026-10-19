# check bjb1 fresh progress v2

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_bjb1-fresh-progress-v2_20260515T013614_result.json`
- **Structured JSON:** [`9ea8d339e73b80a214e4.json`](../../sessions/9e/9ea8d339e73b80a214e4.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部 registry 已更新。以下是完整进度报告：

---

## bjb1-18228 Eval 进度快照 (2026-05-15T09:40Z)

| exp_id | tasks_done | running_avg | 进程状态 | ETA |
|--------|-----------|-------------|---------|-----|
| **eval-argmin-only-spatial** | 7/10 | **42.9%** (30/70) | alive (PID 231421, GPU1) | ~3h |
| **eval-tiny-correction-spatial** | 7/10 | **40.0%** (28/70) | alive (PID 232820, GPU2) | ~3h |
| **eval-acr-spatial-v4-small** | 4.5/10 | **52.5%** (21/40) | alive (PID 253085, GPU2) | ~6h |
| **eval-acr-spatial-v4-obs-only-r2** | 3.5/10 | **63.3%** (19/30) | alive (PID 270097, GPU0) | ~7h |
| **eval-acr-spatial-v4-scalar** *(新发现)* | 刚启动 | - | alive (PID 288939, GPU2) | ~10h |

### Per-task 明细

**eval-argmin-only-spatial** (reconvla, K=10 argmin, no CRM):
| Task | Success |
|------|---------|
| T1 between_plate_ramekin | 60% (6/10) |
| T2 next_to_ramekin | **100%** (10/10) |
| T3 from_table_center | 0% (0/10) |
| T4 on_cookie_box | 30% (3/10) |
| T5 in_top_drawer | 10% (1/10) |
| T6 on_ramekin | 10% (1/10) |
| T7 next_to_cookie_box | **90%** (9/10) |

**eval-tiny-correction-spatial** (CRM v2 perdof, max_norm=0.05):
| Task | Success |
|------|---------|
| T1 between_plate_ramekin | **70%** (7/10) |
| T2 next_to_ramekin | **90%** (9/10) |
| T3 from_table_center | 0% (0/10) |
| T4 on_cookie_box | 30% (3/10) |
| T5 in_top_drawer | 0% (0/10) |
| T6 on_ramekin | 0% (0/10) |
| T7 next_to_cookie_box | **90%** (9/10) |

**eval-acr-spatial-v4-small** (CRM v3-norm perdof, max_norm=0.1):
| Task | Success |
|------|---------|
| T1 between_plate_ramekin | 60% (6/10) |
| T2 next_to_ramekin | **100%** (10/10) |
| T3 from_table_center | 10% (1/10) |
| T4 on_cookie_box | 40% (4/10) |

**eval-acr-spatial-v4-obs-only-r2** (CRM v3-norm obs_only, max_norm=0.1):
| Task | Success |
|------|---------|
| T1 between_plate_ramekin | **90%** (9/10) |
| T2 next_to_ramekin | **100%** (10/10) |
| T3 from_table_center | 0% (0/10) |

### eval-tiny-correction-spatial 诊断结论

**进程没死。** bash wrapper PID 232815 死了（可能 tmux session 被清理），但 python 子进程 PID 232820 仍在正常运行（07:48h uptime, 139% CPU, 9.1GB RSS, GPU2 占用 1450 MiB）。已完成 7/10 tasks，预计 ~3h 自然跑完。**不需要重启。**

Registry 曾被错误标记为 DONE+killed，已在 metrics 中注明实际仍在运行。

### GPU 分配

| GPU | 占用 | 实验 |
|-----|------|------|
| GPU0 | 14250/24564 MiB | eval-acr-spatial-v4-obs-only-r2 |
| GPU1 | 1423/24564 MiB | eval-argmin-only-spatial |
| GPU2 | 2914/24564 MiB | eval-tiny-correction + eval-v4-small + eval-v4-scalar (3进程共享!) |
| GPU3 | 1459/24564 MiB | 空闲（v4-small 实际在 GPU2 而非 registry 记录的 cuda:3） |

### 注意事项
1. **GPU2 三进程共享** — tiny-correction(232820) + v4-small(253085) + v4-scalar(288939) 都在 GPU2 上，可能互相影响性能
2. eval-acr-spatial-v4-scalar 是新发现的实验（PID 288939，刚启动 2 分钟），已注册到 registry
3. 所有实验预计在 **今天内完成**（最晚 ~19:40Z）

---
