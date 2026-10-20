# code 14b experiment prep

**Phase-Modulated Compound Sparsity Severity in 7B-Scale Mathematical Reasoning Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_14b_experiment_prep_20260516T060557_result.json`
- **Structured JSON:** [`48e743388329957db70e.json`](../../sessions/48/48e743388329957db70e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

所有信息收集完毕。以下是完整报告。

---

## 14B 模型架构参数

| 参数 | 值 |
|------|-----|
| hidden_size | 5120 |
| num_hidden_layers | 48 |
| num_attention_heads | 40 |
| num_key_value_heads | 8 (GQA) |
| head_dim | 128 |
| intermediate_size | 13824 |
| vocab_size | 152064 |
| dtype | bfloat16 |

## VRAM 估算

| 组件 | 大小 |
|------|------|
| 模型权重 (bf16) | ~29.6 GB |
| KV cache/token | 0.187 MB (2×8×128×2×48) |
| KV cache 8192 tokens | ~1.5 GB |
| 总计 (含 overhead) | **~33-35 GB** |

**单卡够用。**

## 当前 GPU 占用

| GPU | 已用 | 空闲 | 进程 |
|-----|------|------|------|
| 0 | 73.3 GB | 24.6 GB | c8 LLaMA s025 (PID 315057) |
| 1 | 15.3 GB | **82.4 GB** | python (PID 312143) |
| 2 | 91.1 GB | 6.8 GB | c8 main (PID 310735) |
| 3 | 91.1 GB | 6.8 GB | c8 main (PID 310736) |

**仅 GPU 1 可用**（82 GB 空闲 > 35 GB 需求）。GPU 0 等 c8 s025 完成后也可用。

## 数据文件

`math500_sampled_n250.json` **不存在**。c8 LLaMA 的做法是：
```
--data_path data/math500.json --max_problems 250
```
代码逻辑：`max_problems > 50` 时跳过 stratified sampling，直接取前 250 条。14B 实验应沿用此方式。

## 代码兼容性

无需修改。`device_map=device` 传入 `cuda:1`，bf16 加载，eager attention。c8 LLaMA 和既有 Qwen 7B 实验均未用 `--use_chat_template`，14B 保持一致。

## 5 个实验命令

公共前缀：
```bash
cd /root/autodl-tmp/pacs && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base
```

### 1. importance_s015
```bash
CUDA_VISIBLE_DEVICES=1 nohup python3 -u -m pacs.profiling.run_profiling \
    --model_path checkpoints/Qwen2.5-14B-Instruct \
    --data_path data/math500.json \
    --output_dir ./profiling_output_14b_importance_s015 \
    --sparsity_levels "0.15" --masking_method importance \
    --max_new_tokens 8192 --min_phase_length 10 \
    --max_problems 250 --save_generations --gpu 0 \
    > profiling_output_14b_importance_s015.log 2>&1 &
```

### 2. importance_s020
```bash
CUDA_VISIBLE_DEVICES=1 nohup python3 -u -m pacs.profiling.run_profiling \
    --model_path checkpoints/Qwen2.5-14B-Instruct \
    --data_path data/math500.json \
    --output_dir ./profiling_output_14b_importance_s020 \
    --sparsity_levels "0.20" --masking_method importance \
    --max_new_tokens 8192 --min_phase_length 10 \
    --max_problems 250 --save_generations --gpu 0 \
    > profiling_output_14b_importance_s020.log 2>&1 &
```

### 3. importance_s025
```bash
CUDA_VISIBLE_DEVICES=1 nohup python3 -u -m pacs.profiling.run_profiling \
    --model_path checkpoints/Qwen2.5-14B-Instruct \
    --data_path data/math500.json \
    --output_dir ./profiling_output_14b_importance_s025 \
    --sparsity_levels "0.25" --masking_method importance \
    --max_new_tokens 8192 --min_phase_length 10 \
    --max_problems 250 --save_generations --gpu 0 \
    > profiling_output_14b_importance_s025.log 2>&1 &
```

### 4. importance_s030
```bash
CUDA_VISIBLE_DEVICES=1 nohup python3 -u -m pacs.profiling.run_profiling \
    --model_path checkpoints/Qwen2.5-14B-Instruct \
    --data_path data/math500.json \
    --output_dir ./profiling_output_14b_importance_s030 \
    --sparsity_levels "0.30" --masking_method importance \
    --max_new_tokens 8192 --min_phase_length 10 \
    --max_problems 250 --save_generations --gpu 0 \
    > profiling_output_14b_importance_s030.log 2>&1 &
```

### 5. random_s020 (control)
```bash
CUDA_VISIBLE_DEVICES=1 nohup python3 -u -m pacs.profiling.run_profiling \
    --model_path checkpoints/Qwen2.5-14B-Instruct \
    --data_path data/math500.json \
    --output_dir ./profiling_output_14b_random_s020 \
    --sparsity_levels "0.20" --masking_method random \
    --max_new_tokens 8192 --min_phase_length 10 \
    --max_problems 250 --save_generations --gpu 0 \
    > profiling_output_14b_random_s020.log 2>&1 &
```

注意：`CUDA_VISIBLE_DEVICES=1` + `--gpu 0` 组合使物理 GPU 1 映射为逻辑 cuda:0。

## GPU 分配建议

- **立即可跑**：GPU 1 跑第一个 14B run（importance_s015）
- **串行链式**：写一个类似 `chain_s030_after_s025.sh` 的脚本，5 个 run 依次在 GPU 1 上排队
- **并行加速**：等 GPU 0 的 c8 LLaMA s025 完成后（s030 chain 也在 GPU 0），可以把部分 14B run 分到 GPU 0 并行
- 预计每个 run 耗时 4-8 小时（14B 比 8B 慢约 1.5-2x），5 个 run 串行约 20-40 小时

---
