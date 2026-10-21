# code qlora instruct script

**Depth Profiling: Classifying Recursive Generation Depth in Base-Model LLM Text** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_qlora_instruct_script_20260519T075021_result.json`
- **Structured JSON:** [`15c4e352bf793caf9ae2.json`](../../sessions/15/15c4e352bf793caf9ae2.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

脚本部署完成，dry-run 通过。数据加载验证：

| Generator | Samples | Depth 分布 |
|---|---|---|
| qwen3-1.7b-instruct | 4,963 | 均匀 (~990-996) |
| olmo-2-0425-1b-instruct | 4,429 | 略递减 (995→768) |
| qwen3-1.7b (base) | 2,291 | 递减 (498→398) |
| olmo-2-1b (base) | 2,379 | 递减 (497→450) |

与 base 脚本的关键差异：LoRA r=32/alpha=64 (base 用 r=16/alpha=32), seed=123, 单 generator within-model CV, 新增 binary F1。

---

**4 个训练命令：**

```bash
# GPU 0: OLMo instruct
CUDA_VISIBLE_DEVICES=0 python /root/gen-depth-fingerprint/qlora_instruct.py \
    --generator olmo-2-0425-1b-instruct \
    --data_path /root/gen-depth-fingerprint/data/olmo-2-0425-1b-instruct/generations_shard0.jsonl \
    --backbone /root/autodl-tmp/models/qwen3-0.6b \
    --device cuda:0 \
    --output /root/gen-depth-fingerprint/results/qlora_olmo-2-0425-1b-instruct.json

# GPU 1: Qwen instruct
CUDA_VISIBLE_DEVICES=1 python /root/gen-depth-fingerprint/qlora_instruct.py \
    --generator qwen3-1.7b-instruct \
    --data_path /root/gen-depth-fingerprint/data/qwen3-1.7b-instruct/generations_shard0.jsonl \
    --backbone /root/autodl-tmp/models/qwen3-0.6b \
    --device cuda:0 \
    --output /root/gen-depth-fingerprint/results/qlora_qwen3-1.7b-instruct.json

# GPU 2: OLMo base
CUDA_VISIBLE_DEVICES=2 python /root/gen-depth-fingerprint/qlora_instruct.py \
    --generator olmo-2-1b \
    --data_path /root/gen-depth-fingerprint/data/olmo-2-1b/generations_shard0.jsonl \
    --backbone /root/autodl-tmp/models/qwen3-0.6b \
    --device cuda:0 \
    --output /root/gen-depth-fingerprint/results/qlora_olmo-2-1b.json

# GPU 3: Qwen base
CUDA_VISIBLE_DEVICES=3 python /root/gen-depth-fingerprint/qlora_instruct.py \
    --generator qwen3-1.7b \
    --data_path /root/gen-depth-fingerprint/data/qwen3-1.7b/generations_shard0.jsonl \
    --backbone /root/autodl-tmp/models/qwen3-0.6b \
    --device cuda:0 \
    --output /root/gen-depth-fingerprint/results/qlora_qwen3-1.7b.json
```

注意：每个命令用 `CUDA_VISIBLE_DEVICES` 绑定物理 GPU，脚本内统一用 `--device cuda:0`（即该进程可见的第一块卡）。4 个任务可并行提交到 4 张 RTX 5090 上。

---
