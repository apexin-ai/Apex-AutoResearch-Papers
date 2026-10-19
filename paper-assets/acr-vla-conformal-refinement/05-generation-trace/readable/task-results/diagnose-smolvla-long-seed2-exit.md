# diagnose smolvla long seed2 exit

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_smolvla-long-seed2-exit_20260522T153836_result.json`
- **Structured JSON:** [`3f8687efa8edc743ea0c.json`](../../sessions/3f/3f8687efa8edc743ea0c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 结果

### SmolVLA Long seed2 (vla-only eval)
**异常终止** — 被外部强制 kill，不是正常退出也不是程序报错。

证据：
- 日志仅 19 行，只完成 2/10 个 task 就中断，正在跑第 3 个 task 时停止
- 无 traceback、无 error、无 EXIT_CODE
- 无退出码文件 (`/tmp/agent-ml-exit/` 中没有对应文件)
- tmux session 已不存在

**seed0、seed1 情况相同** — 都在 23:01 前后同时停止，都只完成了 2 个 task。

已完成的部分结果（seed2）：
- Task 1 (alphabet_soup+tomato_sauce): 10% (1/10)
- Task 2 (cream_cheese+butter): 70% (7/10)

### 原因推断
vla-only eval 在 ~23:01 被 kill，4 分钟后（23:05）lerobot eval 在相同 GPU (0/1/2) 上启动。大概率是另一个 agent session 杀掉 vla-only session 后启动了 lerobot baseline eval。

### lerobot eval（当前在跑）
| seed | 进度 | running SR |
|------|------|-----------|
| seed0 | 18/20 | 77.8% |
| seed1 | 17/20 | 64.7% |
| seed2 | 17/20 | 58.8% |

GPU 3/4/5 上还有 pi05 goal precompute 任务在跑。

**vla-only long seed0/1/2 需要重跑。**

---
