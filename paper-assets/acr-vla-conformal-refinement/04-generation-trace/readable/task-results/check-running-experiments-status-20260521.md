# check running experiments status 20260521

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_running-experiments-status-20260521_20260521T070753_result.json`
- **Structured JSON:** [`ecb87451dbb493080fac.json`](../../sessions/ec/ecb87451dbb493080fac.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

汇总如下：

---

## bjb2-28827 — eval-k20-obs-only-object-seed45

| GPU | Util | VRAM |
|-----|------|------|
| 0 | 0% | 1/24G |
| 1-4 | 27-30% | 2.0/24G |
| **5** | **32%** | **2.1/24G** |

- **进度: 9/10 tasks 完成**，正在跑第 10 个 (orange_juice)
- 已完成 task SR: 0%, 10%, 40%, 30%, 0%, 10%, 10%, 20%, 40%
- **进程存活**: PID 23401 ✅ (运行 2h)

---

## bjb1-18228 — eval-k20-obs-only-spatial-seed43 & seed44

| GPU | Util | VRAM |
|-----|------|------|
| 0-3 | **全部 0%** | **0/24G** |

- **seed43: 10/10 tasks 完成 ✅** — Overall SR: **34.0%** (34/100), 结果已存 `eval_k20_spatial_seed43.json`
- **seed44: 10/10 tasks 完成 ✅** — Overall SR: **34.0%** (34/100), 结果已存 `eval_k20_spatial_seed44.json`
- **进程已退出**: PID 706941, 707148 均不存在
- GPU 全部空闲，两个实验均已完成

---

## bjb1-32546 — eval-k20-obs-only-spatial-seed42

| GPU | Util | VRAM |
|-----|------|------|
| 0 | 28% | 2.0/24G |
| 1 | 2% | 2.0/24G |
| **2** | **34%** | **2.2/24G** |
| 3-5 | 23-33% | 2.0/24G |

- **进度: 9/10 tasks 完成**，正在跑第 10 个 (wooden_cabinet)
- 已完成 task SR: 90%, 100%, 0%, 30%, 0%, 0%, 90%, 0%, 40%
- **进程存活**: PID 873171 ✅ (运行 2h)

---

## bjb2-40593 — π0.5 fix Worker

| GPU | Util | VRAM |
|-----|------|------|
| 0 | 0% | 0/24G |

- **无 π0.5 相关进程在运行**，没有 python 实验进程
- 最新日志 `pi05_action_queue_quicktest.json` (13:36 今天) 是一个 quick test 结果，SR=0.0%（vla_only baseline, 5 rollouts）
- `pi05_wrapper.py` 和 `evaluate.py` 在 13:29-13:30 有更新（有 `.bak.actionqueue` 备份），说明 Worker 做了代码修改但目前没有实验在跑
- GPU 完全空闲

---

## 总结

| 实验 | 服务器 | 状态 | 进度 |
|------|--------|------|------|
| k20-object-seed45 | bjb2-28827 | 🏃 运行中 | 9/10, 即将完成 |
| k20-spatial-seed43 | bjb1-18228 | ✅ 完成 | 10/10, SR=34.0% |
| k20-spatial-seed44 | bjb1-18228 | ✅ 完成 | 10/10, SR=34.0% |
| k20-spatial-seed42 | bjb1-32546 | 🏃 运行中 | 9/10, 即将完成 |
| π0.5 fix | bjb2-40593 | ⏸ 空闲 | 代码已改，无实验在跑 |

bjb1-18228 的 GPU 已全部空闲，可以复用。bjb2-28827 和 bjb1-32546 各还剩 1 个 task，预计很快完成。

---
