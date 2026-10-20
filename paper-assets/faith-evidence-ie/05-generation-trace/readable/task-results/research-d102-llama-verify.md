# research d102 llama verify

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_d102_llama_verify_20260518T053411_result.json`
- **Structured JSON:** [`3a1cbb35e733c7f8eb78.json`](../../sessions/3a/3a1cbb35e733c7f8eb78.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 汇报

### LLaMA-8B RSFT 实际 top_k 值：**k=3（确认）**

**判断依据：**
- `rsft_report.json` 明确记录 `"selection_strategy": "top_k", "top_k": 3`
- 数据量验证：23704 candidates / 2963 docs → top_k=3 后选 8829 samples（2952 docs × ~3 ≈ 8829）
- 训练日志确认加载了 8829 samples

### Re-filter k=1 结果

| | k=3（原始） | k=1（re-filtered） |
|---|---|---|
| **样本数** | 8829 | 2952 |
| **唯一文档数** | 2952 | 2952 |
| **F1 均值** | 0.6768 | 0.7098 |
| **CED 均值** | 0.6509 | 0.6860 |
| **Combined 均值** | 0.7311 | 0.7583 |

### 关键路径

- 原始 k=3 训练数据：`/root/autodl-tmp/rsft_scored_llama_3_1_8b/rsft_train.jsonl`（8829 samples）
- **新 k=1 训练数据：`/root/autodl-tmp/rsft_scored_llama_3_1_8b_k1/rsft_train.jsonl`（2952 samples）**
- 已完成 k=3 训练输出：`/root/autodl-tmp/rsft_output_llama_3_1_8b_r3/`

### 推荐 LLaMA k=1 重训命令

```bash
CUDA_VISIBLE_DEVICES=X source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && \
python -m freige.training.rsft_trainer \
    --base_model /root/autodl-tmp/models/meta-llama/Meta-Llama-3.1-8B \
    --sft_adapter /root/autodl-tmp/sft_output_llama_3_1_8b \
    --rsft_data_path /root/autodl-tmp/rsft_scored_llama_3_1_8b_k1/rsft_train.jsonl \
    --output_dir /root/autodl-tmp/rsft_output_llama_3_1_8b_k1 \
    --num_epochs 3 \
    --learning_rate 2e-5 \
    --per_device_batch_size 1 \
    --gradient_accumulation_steps 8 \
    --warmup_steps 100 \
    --max_length 2048 \
    --lora_rank 64 \
    --lora_alpha 128 \
    --bf16 \
    --wandb_run_name llama_8b_rsft_ced_k1 \
    --seed 42
```

注：batch size 参数从日志推算（3312 steps = 8829×3/8，effective batch=8），原始训练大概率用了 `per_device_batch_size=1, gradient_accumulation_steps=8`。k=1 数据量约为 k=3 的 1/3，预计 ~1104 steps，训练时间约 1 小时。

---
