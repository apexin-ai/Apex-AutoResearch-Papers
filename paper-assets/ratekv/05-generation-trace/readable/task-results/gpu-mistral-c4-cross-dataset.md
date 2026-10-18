# gpu mistral c4 cross dataset

**When Does Non-Uniform KV Cache Quantization Help? Cardinality Constraints and a Heterogeneity Diagnostic** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_gpu_mistral_c4_cross_dataset_20260514T121705_result.json`
- **Structured JSON:** [`3026b234fee3702bd4ba.json`](../../sessions/30/3026b234fee3702bd4ba.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

实验已提交并标记为 RUNNING（PID=221916, cuda:1）。

- 脚本: `run_mistral_c4_cross_dataset.py` 已上传到 `/root/ratekv/`
- C4 profiling 阶段正在进行（模型已加载完毕）
- 参数: budget=0.25, max_2bit=4, N_HEADS=256, 设备 cuda:1
- WT2 参考: `mistral_k_ablation_results.json`(k=4 MCKP) + `mistral_hires_results.json`(uniform PPL)
- 输出: `mistral_c4_eval_results.json`
- Registry 状态: RUNNING

---
