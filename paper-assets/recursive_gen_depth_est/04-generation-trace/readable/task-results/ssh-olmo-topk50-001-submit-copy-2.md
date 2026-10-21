# ssh olmo topk50 001 submit

**How Deep Is Your Data? Estimating Recursive Generation Depth via Statistical Fingerprints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_olmo_topk50_001_submit_20260515T001042_result.json`
- **Structured JSON:** [`8bbf4cd279731010ba47.json`](../../sessions/8b/8bbf4cd279731010ba47.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

已提交成功。

- **exp_id**: `olmo_topk50_001`
- **GPU**: cuda:1 (gpu-6000pro-2)
- **tmux session**: `olmo_topk50_001`
- **日志**: `~/runs/recursive_gen_depth_est/olmo_topk50_001.log`
- **PID**: 226461
- **plan_id**: plan_002c

Pipeline 流程：symlink depth-0 LoRA → 生成 depth-1 (top-k k=50) → finetune depth-1 → 生成 depth-2 → finetune depth-2 → 生成 depth-3。

---
