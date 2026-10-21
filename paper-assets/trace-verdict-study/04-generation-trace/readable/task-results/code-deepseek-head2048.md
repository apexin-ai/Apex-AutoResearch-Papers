# code deepseek head2048

**Trace Verbosity Degrades SFT Verdict Prediction: A Case Study in Information Density Effects** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_deepseek_head2048_20260517T175705_result.json`
- **Structured JSON:** [`a6f266662e88b4cbef0b.json`](../../sessions/a6/a6f266662e88b4cbef0b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

实验已提交并运行中。

**完成的工作：**
1. 创建了 `format_head_truncation.py`（基于 tail 版本，改为保留 trace **前** 2048 tokens）
2. 生成了 `full_trace_head_train.jsonl` (4720 samples) 和 `full_trace_head_test.jsonl` (1190 samples)，5610/5910 样本被截断
3. 在 `train_sft.py` 和 `evaluate.py` 中添加了 `full_trace_head` condition
4. 训练+评估已提交到 GPU 0，GPU utilization 100%，22GB VRAM

**运行信息：**
- PID: 371041 / 371047
- 日志: `/root/trace-verdict-study/logs/deepseek_head2048_seed42.log`
- W&B: `trace-verdict-study / deepseek_full_trace_head2048_seed42`
- Checkpoint: `/root/autodl-tmp/trace-verdict-study-checkpoints/deepseek_full_trace_head2048_seed42/`
- 训练完成后自动运行评估，结果保存到 `eval_results.json`

---
