# ops prep 14b rsft generate

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_prep_14b_rsft_generate_20260519T173059_result.json`
- **Structured JSON:** [`cc96d4de4750ee9130e3.json`](../../sessions/cc/cc96d4de4750ee9130e3.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

汇报如下：

### 1. 14B SFT adapter 路径
`/root/autodl-tmp/sft_output_14b/adapter_config.json` — LoRA r=64, alpha=128, base_model 指向 `/root/autodl-tmp/models/Qwen/Qwen3-14B`

### 2. 14B 基座模型路径
`/root/autodl-tmp/models/Qwen/Qwen3-14B`

### 3. 单卡 32GB 能否做 bf16 generation？
**N** — 14B bf16 ≈ 28GB 模型权重，加上 KV cache + batch 推理开销会超过 32GB。`rsft_generate.py` 使用 `device_map="auto"`，设 `CUDA_VISIBLE_DEVICES=X,Y` 分两卡即可（每卡 ~14GB 模型 + KV cache 余量充足）。也可用 `--quantize`（4bit NF4，~7GB），单卡即可但生成质量可能下降。

**推荐：2 卡 bf16**，与 eval_14b.sh 一致。

### 4. 前置步骤：需先合并 adapter
`rsft_14b.sh` 里的 RSFT 训练依赖合并后的模型 `/root/autodl-tmp/models/Qwen3-14B-sft-merged`，**该目录不存在**。但 generation 阶段 `rsft_generate.py` 支持 `--sft_adapter` 参数，可运行时 merge，无需预合并。合并步骤留到 RSFT 训练前执行即可。

### 5. 建议 generation 命令

```bash
# 先确认 GPU 0,2 空闲 (当前 GPU1 占 11GB, GPU3 占 6.6GB)
CUDA_VISIBLE_DEVICES=0,2 python -m freige.training.rsft_generate \
    --base_model /root/autodl-tmp/models/Qwen/Qwen3-14B \
    --sft_adapter /root/autodl-tmp/sft_output_14b \
    --data_path /root/autodl-tmp/data/docred \
    --output_dir /root/autodl-tmp/rsft_generations_14b \
    --num_generations 8 \
    --temperature 0.7 \
    --batch_size 2 \
    --max_new_tokens 1024 \
    --seed 42
```

### 6. 磁盘空间
65GB 可用，充足。

### GPU 当前状态
| GPU | 占用 | 空闲 |
|-----|------|------|
| 0 | 0 MB | 32GB ✓ |
| 1 | 11.3 GB | 20.7GB |
| 2 | 0 MB | 32GB ✓ |
| 3 | 6.6 GB | 25.5GB |

**GPU 0+2 完全空闲，适合做 14B generation。**

---
