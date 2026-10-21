# ops extract qlora hyperparams

**What Can IRT Person-Fit Statistics Reveal About SFT-Stage Benchmark Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_extract-qlora-hyperparams_20260522T080829_result.json`
- **Structured JSON:** [`576ae5261ab62a1c444e.json`](../../sessions/57/576ae5261ab62a1c444e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

三个模型的 train.py 和 data preparation 逻辑全部读完。以下是汇总结果。

---

## QLoRA 训练超参数汇总

### 三模型共用超参数

| 超参数 | 值 |
|--------|-----|
| **Learning rate** | 2e-4 |
| **Epochs** | 3 |
| **per_device_train_batch_size** | 4 |
| **gradient_accumulation_steps** | 4 |
| **Effective batch size** | 16 |
| **LoRA r** | 16 |
| **LoRA alpha** | 32 |
| **LoRA dropout** | 0.05 |
| **LoRA target_modules** | `["q_proj", "k_proj", "v_proj", "o_proj"]` |
| **LoRA bias** | none |
| **Optimizer** | AdamW（SFTConfig/TRL 默认） |
| **Weight decay** | 0.0（SFTConfig 默认） |
| **LR scheduler** | linear（SFTConfig 默认） |
| **Warmup ratio** | 0.1 |
| **Max sequence length** | 512 |
| **Precision** | bf16 if supported, else fp16 |
| **Quantization bits** | 4-bit (load_in_4bit) |
| **Quant type** | nf4 |
| **Compute dtype** | float16 |
| **save_strategy** | epoch |
| **dataloader_num_workers** | 2 |

### 三模型差异

| 项目 | Pilot (Qwen2.5-7B) | Llama (Llama-3.1-8B) | Mistral (Mistral-7B-v0.3) |
|------|---------------------|----------------------|---------------------------|
| **Base model** | Qwen2.5-7B-Instruct | Meta-Llama-3.1-8B-Instruct | Mistral-7B-Instruct-v0.3 |
| **report_to** | wandb | wandb | **none** |
| **Conditions** | clean_s1~s10, contam_5/15/25/50 | clean, contam_15/25/50 | clean, clean_s2~s10, contam_15/50 |
| **Seeds** | 多 seed (42,123,456,301-307) | 42 only | 多 seed (42,123,456,301-307) |

### Data Mixing 方式

**Concat + shuffle**。污染数据直接拼接到 Alpaca 训练集后，然后整体 shuffle，写入同一个 `train.jsonl`。不是 interleave 也不是分 epoch。

具体比例（以 Pilot 的 `prepare_data.py` 为准）：
- **Clean**: 5000 条 Alpaca
- **contam_15**: 5000 Alpaca + 2106 MMLU (15%) = ~7106 条
- **contam_50**: 5000 Alpaca + 7021 MMLU (50%) = ~12021 条
- 15% items 是 50% items 的严格子集

---
