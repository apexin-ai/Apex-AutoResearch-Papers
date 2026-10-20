# ssh grpo status check

**What Can IRT Person-Fit Statistics Reveal About SFT-Stage Benchmark Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_grpo-status-check_20260521T111713_result.json`
- **Structured JSON:** [`996c9fcfb597bde50a45.json`](../../sessions/99/996c9fcfb597bde50a45.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

报告已写入 `artifacts/gpu_status_35694.md`。汇总：

**GRPO 训练正常运行中** — PID 97791，step 2553/14042（18.2%），~5.28s/step，预计 5/22 ~12:00 UTC 完成（还剩 ~17 小时）。

**GPU 状态：** 仅 GPU 2 在用（9.6GB/98GB），GPU 0/1/3 全部空闲。

**Zombie 进程已清理：** PID 98622、96745 均已消失，无需操作。

**值得注意：** 训练中 grad_norm=0 的 step 频率较高（frac_reward_zero_std=1.0），说明很多 batch 内所有 completion 获得相同 reward，导致 advantage=0、无梯度更新。有效训练步比例可能偏低。

---
