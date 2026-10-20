# code deepseek tail2048

**Trace Verbosity Degrades SFT Verdict Prediction: A Case Study in Information Density Effects** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_deepseek_tail2048_20260517T145312_result.json`
- **Structured JSON:** [`e1881e6f6c91778803e6.json`](../../sessions/e1/e1881e6f6c91778803e6.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

实验已提交并注册为 RUNNING。

**总结：**
- **tmux session**: `deepseek_tail2048` on westd-11235
- **GPU**: cuda:0 (RTX PRO 6000 Blackwell, 98GB)
- **数据**: 复用已有 `full_trace_tail` 数据 (4720 train / 1190 test)
- **训练**: 444 步 (3 epochs)，~18.5s/step，预计 ~2h15m
- **流程**: 训练完成后自动执行 evaluate.py，结果写入 `eval_results.json`
- **日志**: `/root/autodl-tmp/trace-verdict-study-checkpoints/deepseek_full_trace_tail2048_seed42/train_eval.log`
- **Registry**: `deepseek_full_trace_tail2048_seed42` → RUNNING

---
