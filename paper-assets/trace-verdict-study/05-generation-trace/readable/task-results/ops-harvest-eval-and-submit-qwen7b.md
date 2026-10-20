# ops harvest eval and submit qwen7b

**Trace Verbosity Degrades SFT Verdict Prediction: A Case Study in Information Density Effects** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_harvest_eval_and_submit_qwen7b_20260518T093556_result.json`
- **Structured JSON:** [`3e814357de19fc92092c.json`](../../sessions/3e/3e814357de19fc92092c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。

```
[tail1024_v3 结果]
训练状态: 完成 (EXIT_CODE=0, epoch 3.0, 2h26m57s)
Epoch 1 (checkpoint-148) accuracy: 98.24% (pass_f1=0.988, fail_f1=0.968)
Epoch 3 (final)          accuracy: 97.56% (pass_f1=0.983, fail_f1=0.955)
Checkpoint 路径: /root/autodl-tmp/trace-verdict-study-checkpoints/codellama13b_full_trace_tail1024_seed42_v3/
Log 路径: ~/runs/trace-verdict-study/codellama13b_full_trace_tail1024_seed42_v3.log

注意: Epoch 1 比 Epoch 3 高 0.68pp，存在过拟合。

[Qwen-7B head-2048]
提交状态: 成功
PID: 425384
Log: ~/runs/trace-verdict-study/qwen7b_full_trace_head2048_seed42.log
GPU: cuda:0
```

---
