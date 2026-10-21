# diagnose verify exp029 seed2 westd startup v4

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_verify-exp029-seed2-westd-startup-v4_20260518T225919_result.json`
- **Structured JSON:** [`14caf8955b6008044785.json`](../../sessions/14/14caf8955b6008044785.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**成功。**

| 项目 | 状态 |
|------|------|
| PID 414163 | 存活，`Ss+`，运行 1m24s |
| tmux session | `exp029_seed2_westd_resume` 正常 |
| Checkpoint resume | step 15 加载成功（model/optimizer/rng/lr_scheduler，rank 0+1 均完成） |
| W&B run ID | `9xs5vfbe`（run name: `exp029-episode-level-seed2`） |
| W&B URL | `https://wandb.ai/xiaoyucorynne-/cost-verify-agent-rl/runs/9xs5vfbe` |
| 当前阶段 | resume 后初始 eval（eval_in_distribution，140 games），eval 完成后进入 step 16 训练 |

**GPU 利用率（westd-47453）：**

| GPU | 利用率 | 显存 |
|-----|--------|------|
| 0 | 0% | 11.1 / 97.9 GB |
| 1 | 0% | 11.1 / 97.9 GB |
| 2 | 100% | 27.5 / 97.9 GB |
| 3 | 91% | 27.5 / 97.9 GB |

GPU 0,1 利用率为 0% 是正常的——当前在 eval 阶段，ALFWorld 环境交互主要在 CPU 端执行。GPU 2,3 被 `hsweep_h10` session 占用。

---
