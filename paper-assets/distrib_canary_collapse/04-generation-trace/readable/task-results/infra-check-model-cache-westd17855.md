# infra check model cache westd17855

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_infra_check_model_cache_westd17855_20260518T164248_result.json`
- **Structured JSON:** [`cde6df81a0e6805c3b43.json`](../../sessions/cd/cde6df81a0e6805c3b43.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 汇总报告

### 1. HF 模型缓存状态

| 模型 | 状态 | 说明 |
|------|------|------|
| EleutherAI/pythia-6.9b | **incomplete** | 2 个 `.incomplete` blob 文件残留 |
| openai-community/gpt2-medium | **incomplete** | 1 个 `.incomplete` blob 文件残留 |
| EleutherAI/pythia-1.4b | **ready** | 无 incomplete/lock 异常 |

pythia-6.9b 和 gpt2-medium 的下载中断了，需要重新触发下载（HF 会自动续传）。

### 2. 6.9B 完整启动命令

```bash
CUDA_VISIBLE_DEVICES=0 python iterative_train.py \
    --model_name EleutherAI/pythia-6.9b \
    --data_dir data/wikitext103_5k \
    --output_dir "results/generalize/pythia69b_wiki_rtxpro_s${SEED}" \
    --num_generations 10 \
    --steps_per_gen 5000 \
    --synthetic_ratio 1.0 \
    --seed "$SEED" \
    --batch_size 4 \
    --max_length 512 \
    --lr 5e-5 \
    --gen_batch_size 4 \
    --gen_max_new_tokens 256 \
    --gradient_checkpointing \
    --bf16 \
    --optim adamw_torch
```

默认 SEED=42，通过 `bash launch_6.9b.sh &lt;seed>` 传参。数据用 wikitext103_5k（不是 c4_5k）。

### 3. batch_size 参数名

| 参数 | 用途 | 默认值 |
|------|------|--------|
| `--batch_size` | 训练 per_device_train_batch_size | 4 |
| `--gen_batch_size` | 生成合成数据时的 batch size | 16（launch_6.9b.sh 覆盖为 4） |

### 4. C4 数据目录

`data/c4_5k/` 存在，含 `train/`、`eval/`、`prompts/` 三个子目录。

---
