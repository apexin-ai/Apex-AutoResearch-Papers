# monitor stale experiments check

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_monitor_stale-experiments-check_20260524T082347_result.json`
- **Structured JSON:** [`77783ac5ac4e1d4fe4d9.json`](../../sessions/77/77783ac5ac4e1d4fe4d9.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 中完全不存在 "eval-smolvla-lerobot-*" 命名的实验（包括搜 "lerobot"、"goal-seed43"、"spatial-seed43" 都无结果）。现在汇总结果。

---

## 任务 1: Stale lerobot 实验

**`eval-smolvla-lerobot-goal-seed43-v3` 和 `eval-smolvla-lerobot-spatial-seed43-v3` 在 registry 中不存在。** 搜索了所有实验（包含关键字 "lerobot"、"goal-seed43"、"spatial-seed43"），均无匹配。可能是名称记错、已被删除、或属于其他项目。

---

## 任务 2: bjb2-28827 Spatial 实验进度

**全部 5 个进程存活**（已通过 `ps -p` 确认），运行时间约 1h30m。

LIBERO-Spatial 共 10 个 task × 20 rollouts/task。根据 tmux 输出的当前 task 位置：

| 实验 | GPU | PID | 当前 task | 进度估算 |
|---|---|---|---|---|
| crm-norm005-spatial-s46 | 0 | 121241 | on_ramekin r15/20 | ~task 6/10 |
| vla-only-spatial-s45 | 2 | 96831 | on_stove r5/20 | ~task 8/10 |
| crm-norm005-spatial-s45 | 3 | 97070 | on_stove r5/20 | ~task 8/10 |
| adapt-tau025-spatial-s45 | 4 | 97307 | on_stove r5/20 | ~task 8/10 |
| vla-only-spatial-s46 | 5 | 97550 | next_to_cookie_box ~r15/20 | ~task 7/10 |

**预计全部在 30-60 分钟内完成。** crm-norm005-s46 因晚启动 23 分钟，进度最慢。

无已完成的实验需要收割，全部仍在跑。

---
