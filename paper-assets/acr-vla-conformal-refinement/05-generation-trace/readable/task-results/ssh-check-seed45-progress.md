# ssh check seed45 progress

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_check-seed45-progress_20260516T170549_result.json`
- **Structured JSON:** [`9fa49993a47308fc3dfc.json`](../../sessions/9f/9fa49993a47308fc3dfc.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 状态汇总

### 实验 A: eval-obs-only-object-norm02-seed45 (bjb1-32546)

**进度: 6.5/10 tasks** — 正在跑第 7 个 task (butter), rollout 5/10 已完成

日志最后修改: 00:48:57 (约 17 分钟前)，进程可能仍在运行(rollout 无中间输出)

已完成 tasks:
| Task | Success Rate |
|------|-------------|
| alphabet_soup | 0% (0/10) |
| cream_cheese | 0% (0/10) |
| salad_dressing | 10% (1/10) |
| bbq_sauce | 40% (4/10) |
| ketchup | 10% (1/10) |
| tomato_sauce | 10% (1/10) |
| butter | 进行中... |

运行时间: ~9.3h (启动 15:44)，每 task ~1.4h → **预估 ETA: ~06:00 CST (还需 ~5h)**

---

### 实验 B: eval-argmin-object-seed45 (bjb2-28827)

**进度: 5.5/10 tasks** — 正在跑第 6 个 task (tomato_sauce), rollout 5/10 已完成

日志最后修改: 01:03:01 (约 3 分钟前)，**进程活跃**

已完成 tasks:
| Task | Success Rate |
|------|-------------|
| alphabet_soup | 0% (0/10) |
| cream_cheese | 0% (0/10) |
| salad_dressing | 10% (1/10) |
| bbq_sauce | 40% (4/10) |
| ketchup | 0% (0/10) |
| tomato_sauce | 进行中... |

运行时间: ~9.3h (启动 15:44)，每 task ~1.7h → **预估 ETA: ~08:30 CST (还需 ~7.5h)**

---

### 初步观察

两个实验在前 5 个 task 的结果几乎一致 (obs_only 和 argmin 在 ketchup 上有 10% vs 0% 的微小差异)。目前累计 success: 实验A 7/60, 实验B 5/50。最终 overall SR 看起来会比较接近。

---
