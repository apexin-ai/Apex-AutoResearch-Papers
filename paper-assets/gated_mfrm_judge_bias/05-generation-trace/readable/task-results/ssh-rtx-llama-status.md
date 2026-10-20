# ssh rtx llama status

**Fair Scores via Joint Calibration: A Gated Many-Facet Rasch Model for Disentangling Judge Bias and Contamination in LLM Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_rtx_llama_status_20260523T021114_result.json`
- **Structured JSON:** [`23dbfc8c9f62252dc3b9.json`](../../sessions/23/23dbfc8c9f62252dc3b9.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**Llama Collection Status:**

```
Shard A (cuda:2, port 8001, judge-llama-a):
  Progress: 850/2664 (31.9%)
  Speed: 0.1 items/s
  ETA: ~334 min ≈ 5.6h

Shard B (cuda:1, port 8004, judge-llama-b):
  Progress: 740/2135 (34.7%)
  Speed: 0.1 items/s
  ETA: ~294 min ≈ 4.9h

Infrastructure:
  vLLM instances: 2× running (AWQ, cuda:1 + cuda:2, 91GB each)
  GPU util: 100% on both GPUs
  tmux sessions: judge-llama-a, judge-llama-b, vllm-llama, vllm-llama-2
  Started: 07:37 today

Bottleneck: Shard A (finishes last)
Overall ETA: ~5.6h from now
```

两个 shard 都在正常运行，各约完成 1/3。Shard A 因 target_models 多（5 vs 4），预计比 Shard B 晚约 40 分钟完成。

---
