# diag cutoff 25k s0 eval

**Does Auxiliary Spatial Supervision Make Vision-Language-Action Models Safer? A Factorial Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diag_cutoff_25k_s0_eval_20260523T204658_result.json`
- **Structured JSON:** [`f2f3e1f8876cdb336d54.json`](../../sessions/f2/f2f3e1f8876cdb336d54.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

诊断完成。

**根因**: 第一次提交时使用了错误参数 `--num_trials_per_task 50`，`evaluate_safelibero.py` 不认识该参数，argparse 返回 exit code 2。正确参数是 `--num_rollouts 50`。

**当前状态**: 两个 eval 已用正确参数重新提交，正在正常运行中（cutoff_25k_s0_eval 在 GPU 3，reverse_cutoff_s0_eval 在 GPU 2）。无需额外修复操作。

报告已写入 `artifacts/diag_eval_failure_20260523.md`。

---
