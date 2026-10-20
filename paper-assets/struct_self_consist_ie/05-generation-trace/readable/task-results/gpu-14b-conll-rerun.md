# gpu 14b conll rerun

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_gpu_14b_conll_rerun_20260521T104141_result.json`
- **Structured JSON:** [`5a5fa882e4a4fe975603.json`](../../sessions/5a/5a5fa882e4a4fe975603.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

实验已启动并注册为 RUNNING。

**总结**：
- **exp_id**: `exp_14b_inference_conll_v2`
- **服务器**: autodl-5090-c, cuda:2 (31.1/32.6 GB)
- **PID**: 308788
- **进度**: 3453 samples × 8 = 27624 prompts，~18 it/s
- **预计完成**: ~25 分钟
- **注意**: 因显存紧张加了 `--gpu_memory_utilization 0.95 --enforce_eager`，KV cache 仅 1.09 GiB (max concurrency 1.45x)，速度比宽裕显存场景慢但能跑完
- **日志**: `output/14b_conll_v2_run.log`

---
