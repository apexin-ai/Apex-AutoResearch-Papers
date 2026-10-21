# ssh gpu audit bjb1 32546

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_gpu-audit-bjb1-32546_20260520T011723_result.json`
- **Structured JSON:** [`a8ee3885665b3c2dbd67.json`](../../sessions/a8/a8ee3885665b3c2dbd67.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## GPU 健康审计 — bjb1-32546

### 逐卡报告

| GPU | 利用率 | 显存占用 | 实验 | 状态 |
|-----|--------|----------|------|------|
| **0** | 23% | 3,363 / 24,564 MiB | eval-adaptive-k-p75-seed44 (PID 140968) | ✅ 正常运行 |
| **1** | 0% | 2 / 24,564 MiB | — | 🟢 **空闲可用** |
| **2** | 91% | 7,645 / 24,564 MiB | eval-adaptive-k-p50-seed44 (PID 141177 + 146926) | ⚠️ **双进程** |
| **3** | 0% | 2 / 24,564 MiB | — | 🟢 **空闲可用** |
| **4** | 74% | 6,721 / 24,564 MiB | eval-adaptive-k-p90-seed42 (PID 141515 + 147198) | ⚠️ **双进程** |
| **5** | 23% | 3,825 / 24,564 MiB | eval-adaptive-k-p25-seed42 (PID 141788) | ✅ 正常运行 |

### Tmux Sessions（4 个）

- `eval-adaptive-k-p25-seed42` — 08:15 创建
- `eval-adaptive-k-p50-seed44` — 08:17 创建
- `eval-adaptive-k-p75-seed44` — 08:15 创建
- `eval-adaptive-k-p90-seed42` — 08:17 创建

### 问题

1. **eval-vla-only-goal-seed47-r2 (cuda:1) — 未运行。** 无 tmux session，GPU 1 空闲。
2. **eval-vla-only-goal-seed48-r2 (cuda:3) — 未运行。** 无 tmux session，GPU 3 空闲。
3. **GPU 2 双进程冲突：** eval-adaptive-k-p50-seed44 有两个 python 进程（PID 141177 启动于 08:15，PID 146926 启动于 08:17），各占 ~3805 MiB，合计 7645 MiB。看起来被提交了两次。
4. **GPU 4 双进程冲突：** eval-adaptive-k-p90-seed42 同样有两个 python 进程（PID 141515 启动于 08:15，PID 147198 启动于 08:17），各占 ~3343 MiB。

### 空闲可用

**GPU 1 和 GPU 3 完全空闲**，可立即使用。

---
