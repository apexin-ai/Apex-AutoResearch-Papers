# ssh seed2 pipeline check

**The Probe Reward Trap: Behavioral Death Before Distributional Collapse in Sycophancy Calibration** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_seed2-pipeline-check_20260521T114216_result.json`
- **Structured JSON:** [`d607132a7469bb60102a.json`](../../sessions/d6/d607132a7469bb60102a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。汇总：

| 项目 | 状态 |
|------|------|
| **exp-003-s2 训练** | step 4106/8000 (51%)，~25s/step，预计还需 ~27h |
| **checkpoint-4000** | 已生成（718MB），已 SCP 到 28034 |
| **28034 GPU** | 4x GPU 全部空闲（2 MiB） |
| **eval 提交** | tmux `eval_s2_ckpt4000`，GPU 0，模型加载中 |
| **registry** | `exp-003-eval-s2-ckpt4000` → RUNNING |
| **cron 监控** | 每 8 分钟检查 eval 完成状态（job b8999889） |

---
