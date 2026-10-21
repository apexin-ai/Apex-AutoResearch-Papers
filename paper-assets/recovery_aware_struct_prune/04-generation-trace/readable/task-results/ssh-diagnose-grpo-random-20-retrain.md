# ssh diagnose grpo random 20 retrain

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_diagnose_grpo_random_20_retrain_20260523T161729_result.json`
- **Structured JSON:** [`6331853ad33595e11ee7.json`](../../sessions/63/6331853ad33595e11ee7.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

诊断完成。

**失败原因**：提交命令中 `--save_only_model True` 不是 `train_grpo_v5.py` 支持的参数，argparse 直接拒绝，EXIT_CODE=2。

**修复**：去掉该参数重跑即可，其他条件（checkpoint、磁盘、依赖）均正常。已追加至 memory.md。

---
