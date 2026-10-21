# ops check running experiments progress

**Trace Verbosity Degrades SFT Verdict Prediction: A Case Study in Information Density Effects** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_check_running_experiments_progress_20260518T113813_result.json`
- **Structured JSON:** [`6bb96be995f8d9dab8ce.json`](../../sessions/6b/6bb96be995f8d9dab8ce.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

```
cuda:0 qwen7b_head2048:       step 398/444, ~epoch 2.7, GPU util 100%, ~12m remaining (16.5s/it)
cuda:1 codellama_tail2048_v3: ✅ 已完成 — 444/444, epoch 3.0, train_loss=0.785, 耗时 3h41m
```

注意：
- GPU 1 已空闲（0MiB / 0% util），codellama13b 训练已结束，模型保存至 `/root/autodl-tmp/trace-verdict-study-checkpoints/codellama13b_full_trace_tail2048_seed42_v3/final`
- codellama13b 的 `eval_loss=nan`，需要排查评估是否正常

---
