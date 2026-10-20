# eval sft baseline noquant

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_sft_baseline_noquant_20260515T183640_result.json`
- **Structured JSON:** [`0eb7f4e1f84bf41c2d40.json`](../../sessions/0e/0eb7f4e1f84bf41c2d40.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

D058 执行完毕，汇总：

**1. eval_sft_baseline_noquant**
- PID: **237912**（实际 GPU 进程 PID 237917）
- GPU: cuda:1, 8172 MiB 已占用
- 状态: RUNNING，推理进行中（62 batches, 985 docs）
- Registry 已更新 spec（含完整 provenance）

**2. flat-NLI 实际 seed 值**
- 从 `/root/autodl-tmp/rsft_output_flat_nli/training_args.bin` 解析：**seed=42**，data_seed=None
- 日志中没有显式打印 seed（rsft_trainer.py 不 log seed），但 TrainingArguments 中记录的值是 42（argparse 默认值）
- Reviewer 看到 registry 中 seed=null 是因为 registry 未填，实际训练确实用了 seed=42

---
