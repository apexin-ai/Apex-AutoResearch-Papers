# code qwen15b tail2048

**Trace Verbosity Degrades SFT Verdict Prediction: A Case Study in Information Density Effects** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_qwen15b_tail2048_20260517T151242_result.json`
- **Structured JSON:** [`79633447faca065bf9d0.json`](../../sessions/79/79633447faca065bf9d0.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

训练已正常运行。

**状态总结**：
- tmux session: `qwen15b_tail2048`
- GPU: cuda:1
- 训练进度: 6/444 steps（3 epochs × 148 steps/epoch）
- 预计时间: ~44 min 训练 + 评估
- 数据: 4720 train / 1190 test
- Log: `/root/autodl-tmp/trace-verdict-study-checkpoints/qwen15b_full_trace_tail2048_seed42.log`
- Registry: `qwen15b_full_trace_tail2048_seed42` → RUNNING

训练完成后会自动运行 `eval/evaluate.py`，结果写入 `eval_results.json`。

---
