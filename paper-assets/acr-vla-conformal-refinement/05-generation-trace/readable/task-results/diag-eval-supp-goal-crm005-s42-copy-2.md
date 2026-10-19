# diag eval supp goal crm005 s42

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diag_eval-supp-goal-crm005-s42_20260523T042931_result.json`
- **Structured JSON:** [`2c85f08d31b850e6fe6c.json`](../../sessions/2c/2c85f08d31b850e6fe6c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 诊断结果：**假阳性 — 实验仍在正常运行**

**进程状态**：PID 524322（bash wrapper）和 PID 524332（python evaluate.py）都还活着，python 进程状态 `Rl`（正在运行），已运行 18 分钟。

**GPU cuda:2**：被 PID 524332 占用，5139MiB 显存，29% GPU 利用率 — 正在活跃计算。

**实验进度**：已完成 3/10 个任务的评估：
| 任务 | 成功率 |
|------|--------|
| open_the_middle_drawer_of_the_cabinet | 85% (17/20) |
| put_the_bowl_on_the_stove | 95% (19/20) |
| put_the_wine_bottle_on_top_of_the_cabinet | 80% (16/20) |
| open_the_top_drawer_and_put_the_bowl_inside | 进行中 (4/5 at rollout 5) |

**根本原因**：这是 cron 监控的误报。评估脚本 (`evaluate.py`) 不向 W&B 写入 metrics，cron 连续 5 次检测不到 W&B 更新就标记为 failed，但进程实际运行正常。

**其他状态**：
- Checkpoint 存在（1.3MB）
- 磁盘 44% used，空间充足

**建议**：不需要修复。等实验自然完成即可（按当前速度预计还需约 30-40 分钟完成剩余 6.x 个任务）。后续可考虑让 eval 脚本也定期写一个心跳文件，避免 cron 误判。

---
