# submit gsm8k qw rand s025 v2

**Phase-Modulated Compound Sparsity Severity in 7B-Scale Mathematical Reasoning Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_submit_gsm8k_qw_rand_s025_v2_20260515T232634_result.json`
- **Structured JSON:** [`3c139e2febf6fb1898f2.json`](../../sessions/3c/3c139e2febf6fb1898f2.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**`gsm8k_qw_rand_s025_v2` 已经在运行中，无需重复提交。**

## 结果汇总

### s030_v2 原始命令（从日志推断，与 s025_v2 同系列）
```bash
python -m pacs.profiling.run_profiling \
  --model_path /root/autodl-tmp/pacs/checkpoints/Qwen2.5-7B-Instruct \
  --data_path data/gsm8k.json \
  --output_dir ./profiling_output_gsm8k_qw_rand_s030_v2 \
  --sparsity_levels 0.30 \
  --masking_method random \
  --save_generations
```
s030_v2 已完成（EXIT_CODE=0，Verdict: PASS）。

### s025_v2 当前状态
- **tmux session**: `gsm8k_qw_rand_s025_v2`（创建于 2026-05-16 07:23:37）
- **进度**: 18/50 problems（约 36%）
- **命令**:
```bash
python -m pacs.profiling.run_profiling \
  --model_path /root/autodl-tmp/pacs/checkpoints/Qwen2.5-7B-Instruct \
  --data_path data/gsm8k.json \
  --output_dir ./profiling_output_gsm8k_qw_rand_s025_v2 \
  --sparsity_levels 0.25 \
  --masking_method random \
  --save_generations
```

已经有人（或之前的 agent）提交了这个任务，正在正常运行中。

---
