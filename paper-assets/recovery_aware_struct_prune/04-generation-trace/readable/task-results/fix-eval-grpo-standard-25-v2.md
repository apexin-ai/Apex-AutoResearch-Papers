# fix eval grpo standard 25 v2

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_fix_eval_grpo_standard_25_v2_20260516T211019_result.json`
- **Structured JSON:** [`6c5e4dd4c91e3cb3747d.json`](../../sessions/6c/6c5e4dd4c91e3cb3747d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

eval 已在正确运行中：
- **PID**: 47509（活跃，179% CPU）
- **模型路径**: `/root/autodl-tmp/recovery_aware_struct_prune/grpo_standard_25`（正确）
- **样本数**: 1319（完整 GSM8K test set）
- **GPU**: cuda:1
- **输出**: `/root/autodl-tmp/recovery_aware_struct_prune/results/eval_grpo_standard_25_n1319.json`
- **启动时间**: 05:05，正在推理中（~3s/sample，预计总时长 ~1.1 小时）

之前的"wrong model"问题已确认：旧结果文件用了 `grpo_standard_25_qwen_math` 路径而非 `grpo_standard_25`。fix worker 已用正确路径重启，无需额外操作。

---
