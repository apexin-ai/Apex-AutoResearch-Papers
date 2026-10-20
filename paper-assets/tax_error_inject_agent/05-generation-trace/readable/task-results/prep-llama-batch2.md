# prep llama batch2

**When Does Unpaired Error Injection Help LLM Agents? Hypotheses from a Failed Transfer to Embodied Planning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_prep_llama-batch2_20260516T062929_result.json`
- **Structured JSON:** [`968eabec35d0dce66f67.json`](../../sessions/96/968eabec35d0dce66f67.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 验证结果

**LLaMA-3.1-8B-Instruct 训练已在运行中，无需 dry-run。**

### 当前状态

| 条件 | GPU | 状态 | 进度 | 峰值显存 | 预计剩余 |
|------|-----|------|------|----------|----------|
| TaxEI (s42) | cuda:1 | RUNNING | 180/3387 | 30.76 GiB | ~2h |
| Random (s42) | cuda:2 | RUNNING | 200/3387 | 29.91 GiB | ~2h |
| Vanilla (s42) | cuda:0 | **未启动** | — | — | — |
| v4-taxei-rp-s7 (Qwen3) | cuda:3 | RUNNING | — | ~27.8 GiB | — |

### 关键确认项

- **模型完整性**: `/root/autodl-tmp/models/Meta-Llama-3.1-8B-Instruct/` — 4 shards + tokenizer ✓
- **ms-swift 兼容**: 零代码修改，`swift sft --model &lt;path>` 直接支持 ✓
- **显存安全**: 峰值 30.76 GiB < 32 GB，无 OOM ✓
- **训练速度**: ~2.3 s/step

### 数据文件

| 条件 | 数据 | 行数 | 预计总步 |
|------|------|------|----------|
| TaxEI | sft_taxei_v4.jsonl | 9029 | 3387 |
| Random | sft_random_v4.jsonl | 9029 | 3387 |
| Vanilla | sft_vanilla_v4.jsonl | 4358 | ~1635 |

### 缺失: llama31-vanilla-s42 启动命令

GPU 0 空闲，可立即启动：

```bash
CUDA_VISIBLE_DEVICES=0 swift sft \
  --model /root/autodl-tmp/models/Meta-Llama-3.1-8B-Instruct \
  --dataset /root/autodl-tmp/tax_error_inject_agent/data/mini_pipeline_v4/sft_vanilla_v4.jsonl \
  --output_dir /root/autodl-tmp/tax_error_inject_agent/output/llama31-vanilla-s42 \
  --lora_rank 16 --num_train_epochs 3 \
  --per_device_train_batch_size 4 --gradient_accumulation_steps 2 \
  --learning_rate 1e-4 --max_length 4096 \
  --seed 42 --data_seed 42 --logging_steps 10 \
  --gradient_checkpointing true --bf16 true --save_strategy epoch
```

预计耗时 ~63 分钟（1635 steps × 2.3s/step）。

### 结论

Dry-run 验证无需额外执行——实际训练已证明 LLaMA-3.1-8B + ms-swift LoRA 配置在 RTX 5090 上完全可行。唯一缺失是 **Vanilla 条件未启动**，GPU 0 空闲可随时补上。

---
