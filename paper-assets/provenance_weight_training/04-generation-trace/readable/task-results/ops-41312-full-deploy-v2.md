# ops 41312 full deploy v2

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_41312_full_deploy_v2_20260518T014202_result.json`
- **Structured JSON:** [`26052cd11b42660aa66e.json`](../../sessions/26/26052cd11b42660aa66e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。westd-41312 四张 GPU 已满载运行：

| GPU | 实验 | PID | 状态 |
|-----|------|-----|------|
| cuda:0 | contamination_60_adaptive_seed456 | 158632 | 训练中 (~2.2s/it, ETA ~3.7h) |
| cuda:1 | contamination_60_uniform_seed456 | 158709 | 训练中 |
| cuda:2 | grid_b0_1_seed123 | 158918 | 训练中 |
| cuda:3 | grid_b0_1_seed456 | 159304 | 训练中 (~2.1s/it, ETA ~3.6h) |

所有实验正常输出 weighting metrics，预计约 3.5-4 小时完成。

---
