# ops resubmit bjb1 32546 timeout16

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_resubmit-bjb1-32546-timeout16_20260518T212518_result.json`
- **Structured JSON:** [`17d7972c9f1057bb78c9.json`](../../sessions/17/17d7972c9f1057bb78c9.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两个 session 已确认运行。汇总如下：

---

## 任务 1: GPU 状态

| GPU | Util | 显存占用 | 进程数 |
|-----|------|----------|--------|
| 0 | 20% | 4270/24564 MiB | 1 → 2 (新加 seed44) |
| 1 | 99% | 7141/24564 MiB | 2 |
| 2 | 98% | 7607/24564 MiB | 2 |
| 3 | 21% | 5182/24564 MiB | 1 |
| 4 | 89% | 6676/24564 MiB | 2 |
| 5 | 21% | 4270/24564 MiB | 1 → 2 (新加 seed46) |

当前 11 个 tmux session 在跑。

## 任务 2: seed44 重提交 ✓
- `eval-obs-only-norm003-seed44-t16` → GPU 0, timeout 57600s

## 任务 3: seed46 重提交 ✓
- 原 session `eval-obs-only-object-norm003-seed46` 已不存在
- `eval-obs-only-norm003-seed46-t16` → GPU 5, timeout 57600s

## 任务 4: 最近 24h 收割结果

| 实验 | SR |
|------|----|
| obs_only_norm03_seed46 | **0.17** |
| obs_only_default_seed46 | 0.15 |
| obs_only_norm005_seed43_r2 | 0.14 |
| obs_only_norm005_seed44 | 0.16 |
| obs_only_norm005_seed45 | 0.14 |
| obs_only_norm01_seed46 | **0.18** |
| perdof_default_seed46 | 0.00 |
| perdof_norm005_seed44 | 0.09 |
| perdof_norm01_seed43 | 0.12 |
| perdof_norm01_seed47_r2 | 0.14 |
| perdof_norm02_seed43_bjb1 | 0.09 |

## 任务 5: 空闲 GPU slots
- **GPU 3**: 1 进程, 21% util, ~19 GB 空闲 — 可部署新实验
- GPU 0/5 刚各加了 1 个任务，仍有 ~16 GB 空闲但已各 2 进程
- GPU 1/2/4 各 2 进程, 高利用率, 不建议再加

**最佳可用 slot: GPU 3**（目前只有 1 个进程且利用率低）。

---
