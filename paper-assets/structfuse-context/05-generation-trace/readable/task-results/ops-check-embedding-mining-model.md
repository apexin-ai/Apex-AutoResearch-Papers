# ops check embedding mining model

**StructFuse: Structure-Grounded Hard Negative Mining for Contrastive Code Context Retrieval** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_check-embedding-mining-model_20260515T104241_result.json`
- **Structured JSON:** [`a985cfec7cdd07cda91b.json`](../../sessions/a9/a985cfec7cdd07cda91b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

证据齐全。

## 结论：**(A) 各自用自己的 base model**

| 实验 | embedding mining 用的模型 | 来源 |
|------|--------------------------|------|
| **Qwen** | `/root/autodl-tmp/structfuse/models/Qwen/Qwen2.5-Coder-3B` | `build_full_m2_data.sh` 第 26 行 |
| **StarCoder** | `/root/autodl-tmp/models/bigcode/starcoder2-3b/bigcode/starcoder2-3b` | `run_starcoder_data_build.sh` 第 12 行 |

两个脚本都调用同一个 `build_m1_training_data.py`，通过 `--model-path` 传入各自的 base model 来计算 embedding distance，然后用距离最近的文件作为 hard negatives。

补充细节：`run_starcoder_data_build.sh` 只重新生成了 `train_embedding_distance_s{42,43,44}.jsonl`，而 `random`、`dataflow_aware` 和 **val** embedding distance 数据直接从 Qwen 数据目录复制过来（这些策略不依赖模型 embedding）。

---
