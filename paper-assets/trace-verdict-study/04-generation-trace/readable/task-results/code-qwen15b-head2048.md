# code qwen15b head2048

**Trace Verbosity Degrades SFT Verdict Prediction: A Case Study in Information Density Effects** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_qwen15b_head2048_20260517T181635_result.json`
- **Structured JSON:** [`4393256b2018337c178e.json`](../../sessions/43/4393256b2018337c178e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

训练+评估已提交并运行中。

**摘要**：
- **数据确认**：`full_trace_head_train.jsonl` (4720) / `full_trace_head_test.jsonl` (1190) 存在于 `/root/autodl-tmp/trace-verdict-study-data/`
- **Condition 确认**：`full_trace_head` 已注册在 `train_sft.py` 和 `evaluate.py`
- **GPU**：cuda:1 空闲，进程已启动，正在 tokenize
- **任务**：训练完成后自动执行评估，结果写入 `/root/autodl-tmp/trace-verdict-study-checkpoints/qwen15b_full_trace_head2048_seed42/final/eval_results.json`
- **日志**：`/root/trace-verdict-study/logs/qwen15b_full_trace_head2048_seed42.log`
- **WandB**：`qwen15b_full_trace_head2048_seed42`

---
