# diagnose post restart gpu check

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_post-restart-gpu-check_20260519T174115_result.json`
- **Structured JSON:** [`4ff58f59fb4f42382c33.json`](../../sessions/4f/4ff58f59fb4f42382c33.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## GPU 状态总表

### bjb2-28827（6/6 实验 ✅）
| GPU | 实验 | 显存 | GPU% | 运行时间 | 状态 |
|-----|------|------|------|---------|------|
| 0 | eval-vla-only-goal-seed44-r2 | 3704/24564 MiB | 19% | 36m | ✅ ALIVE |
| 1 | eval-argmin-object-k5-seed44-r2 | 4721/24564 MiB | 21% | 36m | ✅ ALIVE |
| 2 | eval-vla-only-goal-seed45 | 5058/24564 MiB | 16% | 10m | ✅ ALIVE |
| 3 | eval-obs-only-spatial-norm02-seed46-r2 | 4190/24564 MiB | 30% | 36m | ✅ ALIVE |
| 4 | eval-openvla-object-baseline-seed42 | 22986/24564 MiB | 60% | 38m | ✅ ALIVE |
| 5 | fmvd-calibration-phase1 | 4304/24564 MiB | 27% | 36m | ✅ ALIVE |

### bjb1-32546（5/6 实验 ⚠️）
| GPU | 实验 | 显存 | GPU% | 运行时间 | 状态 |
|-----|------|------|------|---------|------|
| 0 | eval-vla-only-long-seed42 | 3449/24564 MiB | 23% | 1h2m | ✅ ALIVE |
| 1 | **eval-vla-only-spatial-seed47** | **2/24564 MiB** | **0%** | — | **❌ MISSING** |
| 2 | eval-vla-only-long-seed43 | 3449/24564 MiB | 25% | 1h2m | ✅ ALIVE |
| 3 | eval-vla-only-long-seed44 | 3449/24564 MiB | 20% | 1h2m | ✅ ALIVE |
| 4 | eval-vla-only-goal-seed42 | 1896/24564 MiB | 21% | 1h2m | ✅ ALIVE |
| 5 | eval-vla-only-goal-seed43 | 1896/24564 MiB | 22% | 1h2m | ✅ ALIVE |

### bjb1-18228（4/4 实验 ✅）
| GPU | 实验 | 显存 | GPU% | 运行时间 | 状态 |
|-----|------|------|------|---------|------|
| 0 | eval-obs-only-object-norm005-seed48 | 1942/24564 MiB | 21% | 11h46m | ✅ ALIVE |
| 1 | eval-vla-only-long-seed45 | 6283/24564 MiB | 22% | 11m | ✅ ALIVE |
| 2 | eval-perdof-object-norm005-seed47 | 1942/24564 MiB | 23% | 11h46m | ✅ ALIVE |
| 3 | eval-perdof-object-norm003-seed47 | 1942/24564 MiB | 22% | 11h46m | ✅ ALIVE |

### bjb2-40593（1/1 实验 ✅）
| GPU | 实验 | 显存 | GPU% | 运行时间 | 状态 |
|-----|------|------|------|---------|------|
| 0 | eval-obs-only-spatial-norm02-seed43 | 2499/24564 MiB | 12% | 15h57m | ✅ ALIVE |

---

## FMVD Phase 1 详情
- **进程状态**: ALIVE (PID 901435)
- **进度**: **15/50 episodes（3/10 tasks 完成）**，正在运行中
  - Task 1 `alphabet_soup`: 0/5 成功
  - Task 2 `cream_cheese`: 0/5 成功
  - Task 3 `salad_dressing`: 1/5 成功（ep4 OK, 137 steps）
  - 已耗时 ~2034s（~34 min），每 episode ~135s
- **JSON 输出**: 尚未生成（运行完才写）
- **预计剩余**: 35 episodes × ~135s ≈ 79 min

## OpenVLA 详情
- **进度**: **42/50 trials（84%）**
- 当前速度 ~48-54s/trial
- **预计剩余**: ~8 trials × ~50s ≈ 7 min

---

## 异常

1. **❌ bjb1-32546 cuda:1 — eval-vla-only-spatial-seed47 未运行**
   - GPU 1 显存 2 MiB / 0% 利用率
   - 无对应 log 文件，无 exit file → **从未部署过**
   - 需要手动启动

2. **⚠️ bjb1-32546 残留旧 tmux**: `eval-acr-object-v4-obs-only`（4d16h 前创建，cuda:2），与当前 eval-vla-only-long-seed43 可能冲突（两者都用 cuda:2）

3. **⚠️ bjb2-40593 残留旧 tmux**: `eval-scalar-seed45-r2`（1d5h 前）和 `eval-obs-only-spatial-norm02-seed43`（16h 前，仍在 cuda:0 运行）

---
