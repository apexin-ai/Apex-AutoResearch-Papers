# ops qwen7b s0 cqa1 eval launch

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_qwen7b-s0-cqa1-eval-launch_20260520T224626_result.json`
- **Structured JSON:** [`9ef88511539f268c692e.json`](../../sessions/9e/9ef88511539f268c692e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Eval 已成功启动：

- **tmux session**: `qwen7b_s0_eval`
- **GPU 0**: 15904MiB / 24564MiB，95% utilization
- **主进程 PID**: 411322 (python evaluate.py)
- **脚本 PID**: 411308 (eval_qwen7b_s0_mmlu_cqa1.sh)

当前正在执行 MMLU eval（d000 first dosage）。ARC 会在 MMLU 全部完成后自动开始。

预计完成时间：
- MMLU: ~50min（5 dosage × ~10min）
- ARC: ~25min（5 dosage × ~5min）
- 总计 ~75min，约 08:00 UTC 完成

---
