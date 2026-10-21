# eval cls8b s42 ckpt1600 val8192 v2

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_cls8b-s42-ckpt1600-val8192-v2_20260515T034640_result.json`
- **Structured JSON:** [`26f485d563758ce16097.json`](../../sessions/26/26f485d563758ce16097.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

评估正在正常运行。

- **Exp ID**: `cls8b-s42-ckpt1600-val8192-v2`
- **PID**: 325097
- **Server**: seetacloud-westd-4x5090, cuda:0
- **进度**: 160/9335, running_acc=84.4%
- **日志**: `/tmp/eval_cls8b_ckpt1600_val8192_v2.log`
- **修复**: 使用本地模型路径 `/root/autodl-tmp/.hf_cache/Qwen/Qwen3-8B` + `HF_HUB_OFFLINE=1` + `network_turbo`，完全绕过网络依赖

模型加载成功，推理正常进行。按 ~1.5s/sample 估算，9335 条约需 ~3.5 小时完成。

---
