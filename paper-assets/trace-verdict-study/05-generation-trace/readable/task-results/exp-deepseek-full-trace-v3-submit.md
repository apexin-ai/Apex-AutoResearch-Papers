# exp deepseek full trace v3 submit

**Trace Verbosity Degrades SFT Verdict Prediction: A Case Study in Information Density Effects** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_exp_deepseek_full_trace_v3_submit_20260515T205517_result.json`
- **Structured JSON:** [`02196cc62ab00dc1856a.json`](../../sessions/02/02196cc62ab00dc1856a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

提交完成。汇报：

**deepseek_full_trace_seed42_v3 已在 cuda:1 上启动**

- **PID**: 163109
- **GPU 1 显存**: 22,078 MiB / 97,887 MiB，util 100%
- **GPU 0**: PID 160932 (deepseek_eo_seed456) 未受影响，22,414 MiB
- **tmux session**: `deepseek_full_trace_seed42_v3`
- **总步数**: 444 steps (3 epochs, 4720 train samples, batch 4 × grad_accum 8 = effective batch 32)
- **数据**: Train 4720 / Eval 1190
- **代码确认**: to_chat_text() label-preserving truncation ✓，load_best_model_at_end TEMP_DISABLED ✓
- **Registry**: 已更新为 RUNNING

注意：任务描述中用了 `--model` (HF ID)，但脚本参数是 `--model_path` 且 HuggingFace 不可达，已改用本地路径 `/root/autodl-tmp/models/deepseek-coder-6.7b-instruct/deepseek-ai/deepseek-coder-6.7b-instruct/`。

---
