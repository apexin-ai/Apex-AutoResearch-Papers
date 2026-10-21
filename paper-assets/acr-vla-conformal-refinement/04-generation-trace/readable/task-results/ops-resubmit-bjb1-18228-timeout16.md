# ops resubmit bjb1 18228 timeout16

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_resubmit-bjb1-18228-timeout16_20260518T212506_result.json`
- **Structured JSON:** [`9e4ae2fa1c4bf0f51447.json`](../../sessions/9e/9e4ae2fa1c4bf0f51447.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。

## 结果汇报

| 任务 | 状态 |
|------|------|
| 1. Kill obs_only_norm003_seed49 | ✅ `tmux kill-session -t eval-obs-only-object-norm003-seed49` 成功 |
| 2. 重提交 seed49 (cuda:3, 16h timeout) | ✅ `eval-obs-only-norm003-seed49-t16` 已启动 |
| 3. 重提交 seed45 (cuda:3, 16h timeout) | ✅ `eval-obs-only-norm003-seed45-t16` 已启动 |

## GPU 3 状态

当前 2410 MiB（模型加载中），之前的 perdof default seed43 orphan 似乎已结束。GPU 3 现在只有 seed49 + seed45 两个新进程，空间充裕。

## 空闲 GPU slots

| GPU | 可用空间 | 可新增实验数 |
|-----|---------|-------------|
| 0 | ~13 GB free | 2 个（已有 2 进程） |
| 1 | ~13 GB free | 2 个（已有 2 进程） |
| 2 | ~15.5 GB free | 2-3 个（已有 2 进程） |
| 3 | ~22 GB free → 模型加载后约 ~13 GB | 可能还能加 1-2 个 |

Orphan 进程（无 tmux，agent-ml 启动）：
- GPU 2: perdof norm003 seed44
- GPU 3: perdof default seed43（可能已结束，内存已释放）

---
