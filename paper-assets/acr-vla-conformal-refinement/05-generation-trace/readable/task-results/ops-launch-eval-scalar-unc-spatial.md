# ops launch eval scalar unc spatial

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_launch-eval-scalar-unc-spatial_20260514T022205_result.json`
- **Structured JSON:** [`eac0e0776c1776cb99a2.json`](../../sessions/ea/eac0e0776c1776cb99a2.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

启动成功。

- **PID**: 143206
- **命令**: `CUDA_VISIBLE_DEVICES=3 python -u src/evaluate.py --mode crm_scalar --benchmark spatial --n_rollouts 10 --seed 42 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm/scalar_unc/crm_best.pt --output_file /root/autodl-tmp/eval_results/eval-scalar-unc-spatial.json`
- **日志**: `/root/autodl-tmp/eval_results/eval-scalar-unc-spatial.log`
- **状态**: SmolVLA 和 CRM (scalar_unc, 327,966 params) 均已加载，10 个 spatial tasks 就绪，正在执行 rollouts。

---
