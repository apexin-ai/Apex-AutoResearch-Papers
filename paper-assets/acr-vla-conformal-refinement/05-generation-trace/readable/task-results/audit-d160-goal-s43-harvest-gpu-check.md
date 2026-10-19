# audit d160 goal s43 harvest gpu check

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_audit_d160-goal-s43-harvest-gpu-check_20260526T072219_result.json`
- **Structured JSON:** [`e0dc97a884e2cbcd38c0.json`](../../sessions/e0/e0dc97a884e2cbcd38c0.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## Goal s43 JSON
- 状态: 找到（两个候选）
- 文件:
  - `/root/acr-vla-conformal-refinement/logs/eval_goal_vla_only_seed43.json`（May 23 21:34, 1326 B）
  - `/root/acr-vla-conformal-refinement/logs/eval_goal_vla_only_seed43_r4.json`（May 23 00:15, 1325 B）
- SR:
  - `seed43.json`: **0.825**（200 rollouts，10 tasks × 20）
  - `seed43_r4.json`: **0.98**（200 rollouts，10 tasks × 20）
- 完整性: 两份都完整（10/10 task 全部填齐，200 rollouts）
- 注意: 未找到 `eval-supp-goal-vla-only-wrapper-s43` 的专属 JSON；s42 有 `eval-supp-goal-vla-only-s42.log` 但 s43 无对应 supp log。判断哪个对应 wrapper 配置需要核对 r4 后缀含义（疑似 wrapper/重跑变体，与常规 vla_only SR 0.825 差异显著）。

## bjb1 GPU 可用性

### bjb1-32546（6× RTX 4090）
| GPU | 状态 | 进程 PID | VRAM 使用 | Util |
|---|---|---|---|---|
| 0 | 占用 | 599835 (python) | 12.6/24 GiB | 25% |
| 1 | 占用 | 600104 (python) | 12.6/24 GiB | 37% |
| 2 | 占用 | 600373 (python) | 12.6/24 GiB | 60% |
| 3 | 占用 | 600978 (python) | 12.7/24 GiB | 27% |
| 4 | 占用 | 601242 (python) | 12.7/24 GiB | 25% |
| 5 | 占用 | 601320 (python) | 12.7/24 GiB | 25% |

tmux: pi05-crm-k2-{goal,object}-s{42,43,44}（6 个 session 全在跑）

### bjb1-18228（4× RTX 4090）
| GPU | 状态 | 进程 PID | VRAM 使用 | Util |
|---|---|---|---|---|
| 0 | 占用 | 2558 (python) | 12.8/24 GiB | 24% |
| 1 | 占用 | 2916 (python) | 12.8/24 GiB | 20% |
| 2 | 占用 | 42110 (python) | 13.5/24 GiB | 25% |
| 3 | 占用 | 3764 (python) | 12.7/24 GiB | 24% |

tmux: pi05-adaptive-goal-s43-bjb1-18228（仅 1 个 session 但 4 个 GPU 都有 python 进程）

### 可用 GPU 总结
**当前 0 个 GPU 可用**。bjb1-32546 全部 6 卡跑 pi05-crm-k2，bjb1-18228 全部 4 卡跑 pi05-adaptive-goal 相关任务。SmolVLA 5 个补跑实验需要等待现有 pi05 任务释放，或抢占。建议等当前 pi05 批次完成后再排队。

---
