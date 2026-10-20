# ssh verify 30476 training start

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_verify_30476_training_start_20260517T112733_result.json`
- **Structured JSON:** [`8b56fb7bb0a9a491c618.json`](../../sessions/8b/8b56fb7bb0a9a491c618.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

4 个实验全部正常运行：

| 实验 | PID | 进程存活 | 训练输出 | 进度 | 速度 |
|------|-----|---------|---------|------|------|
| random_reweight_seed123_r2 | 10035 | Y | Y | 41/6103 (1%) | ~2.17s/it |
| bs8_auto_nmin_r3 | 10119 | Y | Y | 38/6103 (1%) | ~2.31s/it |
| batch_adaptive_tau_rho06_r3 | 10209 | Y | Y | 36/6103 (1%) | ~2.29s/it |
| rho02_adaptive_tau09_r3 | 10727 | Y | Y | 33/6103 (1%) | ~2.42s/it |

无 import error 或 traceback。所有实验都在正常输出 weighting metrics 和 loss，预计各需约 3.5-4 小时完成。

---
