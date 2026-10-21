# fix gpu collision cleanup

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_fix_gpu-collision-cleanup_20260516T040107_result.json`
- **Structured JSON:** [`21d82670b21ed08d0463.json`](../../sessions/21/21d82670b21ed08d0463.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 冲突清理
- PID 628171 (plan018-additive-random-b01-s45): **not_found**（已自行消亡）
- tmux session plan018-additive-random-b01-s45: **not_found**

## sweep-isr-b02-s42 (cuda:1)
- PID: 626802, 状态: **alive**, 运行 7min, CPU 105%
- 当前 step: **50/500**
- GPU 占用: **80077 MiB**, 利用率 100%

## sweep-isr-b01-s45 (cuda:0)
- PID: 604569, 状态: **dead**
- 最后记录 step: **219/500**（停在 03:59:49 UTC）
- tmux session: 不存在
- 有 checkpoint-200，无 train.log
- GPU 占用: **0 MiB**

## GPU 总览
- cuda:0: 0 MiB, 0%
- cuda:1: 80077 MiB, 100%

---

**问题**: sweep-isr-b01-s45 在 step 219 意外死亡，cuda:0 完全空闲。可能是 plan018 误提交时的 GPU 冲突波及，或 OOM。需要决定是否在 cuda:0 上重启（从 checkpoint-200 resume 或从头重训）。

---
