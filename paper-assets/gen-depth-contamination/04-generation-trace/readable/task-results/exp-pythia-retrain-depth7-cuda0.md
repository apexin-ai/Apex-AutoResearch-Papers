# exp pythia retrain depth7 cuda0

**Generational Depth Estimation of Recursive Synthetic Text: Measuring the Discrimination Boundary** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_exp_pythia-retrain-depth7-cuda0_20260519T014932_result.json`
- **Structured JSON:** [`fdb9121a9d2c0592338c.json`](../../sessions/fd/fdb9121a9d2c0592338c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

实验已启动并验证成功。总结：

- **实验 ID**: `exp_pythia_retrain_depth7`
- **GPU**: cuda:0 (RTX 4090 D)，PID 115855，5442MiB 显存，81% 利用率
- **当前状态**: 正在 fine-tune depth_4 数据（depth 0-4 已有数据自动跳过）
- **LoRA targets**: `query_key_value`（Pythia GPT-NeoX 架构自动检测）
- **流程**: depth 4 → fine-tune → generate depth 5 → ... → depth 7 → feature extraction (Qwen2.5-1.5B scorer) → 5-fold GroupKFold AUC analysis
- **日志**: `/root/autodl-tmp/gen-depth-contamination/logs/exp_pythia_retrain_depth7.log`
- **Registry**: RUNNING

---
